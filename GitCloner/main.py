# GitHub Cloner in Python
import os
import shutil
from platform import uname
# from git import Repo
import base64
from github import Github
from pprint import pprint

# Git Settings
user = "jplight"
base = "git"

# Path to git Basedir
windoof = "C:\\dummy\\"
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
    shutil.rmtree(os.getcwd() + sub + base)
os.mkdir(base)
os.chdir(path + sub + base)

# Create Repo List
g = Github()
username = g.get_user(user)
repos = []
size = len("Repositoryfull_name") + 4 + len(user)
for repo in username.get_repos():
    repos.append(str(repo)[size:-2:])
for runner in repos:
    print(runner)

# Git Module with Python
# Repo.clone_from("https://github.com/Zeyecx/faultybot.git", os.getcwd()+sub+"faultybot")
