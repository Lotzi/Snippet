# GitCloner 
You can download all public gits of a user with the tool. 
I only tinkered with the script because it was annoying to clone all git by hand. 

# How it works


## Folder architecture
The gits are each cloned into a git folder. These are set to the root dir. 
```python
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
```


## Get Repos
The repos are read out via the GitHub API. A public package is used for this purpose. 
```python
# Create Repo List
g = Github()
username = g.get_user(user)
repos = []
size = len("Repositoryfull_name") + 4 + len(user)
for repo in username.get_repos():
    repos.append(str(repo)[size:-2:])
```


## Clone Repos
We also use a public package for cloning. However, I create the urls myself here. It's quicker and easier to read. 
```python
for runner in repos:
    module = f"https://github.com/{user}/{runner}.git"
    Repo.clone_from(module, os.getcwd() + sub + runner)
```