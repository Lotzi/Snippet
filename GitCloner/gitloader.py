# GitHub Cloner in Python
import os
import shutil
from platform import uname
from github import Github
from git import Repo

# Git Settings
user = "Riffecx"
base = "git"

# Path to git Basedir
windoof = "C:\\dummy"
wsl = "/mnt/c/"
linux = "/"

# Set OS and change path
if "nt" in os.name:
    path = windoof
    sub = "\\"
else:
    path = linux
    sub = "/"
if 'Microsoft' in uname().release:
    path = wsl
    sub = "/"

# Test path
try:
    os.chdir(path)
except Exception as e:
    print(e)
    print("Folder not found")
    exit(0)

# Modify path
if path[:-2:] == "\\":
    if not path[:-3:] == ":\\":
        path = path[:-2:]

if path[:-1:] == "/":
    path = path[:-1:]

# Create Folder
os.chdir(path)
if os.path.isdir(base):
    try:
        shutil.rmtree(os.getcwd() + sub + base)
        os.mkdir(base)
    except Exception as e:
        print(e)
        print("Folder could not be deleted")
if not os.path.isdir(base):
    os.mkdir(base)

os.chdir(path + sub + base)

# Create Repo List
g = Github()
username = g.get_user(user)
repos = []
size = len("Repositoryfull_name") + 4 + len(user)
for repo in username.get_repos():
    repos.append(str(repo)[size:-2:])

# Git Module with Python
for runner in repos:
    module = f"https://github.com/{user}/{runner}.git"
    Repo.clone_from(module, os.getcwd() + sub + runner)
