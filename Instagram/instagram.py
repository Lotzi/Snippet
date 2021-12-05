import subprocess
import os
import sys
user = "user"
your_username = "your_username" # Optional


""" 
instaloader [--comments] [--geotags]
            [--stories] [--highlights] [--tagged] [--igtv]
            [--login YOUR-USERNAME] [--fast-update]
            profile | "#hashtag" | :stories | :feed | :saved
"""

# Download
if user == "user":
    print("Please enter a user.")
    sys.exit(0)
try:
    subprocess.run("instaloader "+user, shell=True, check=True)

    # Download with Login
    # subprocess.run("instaloader --login="+your_username+" "+user, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
finally:
    # CD to the downloaded folder
    os.chdir(user)

    # Delete JSON
    directory = "./"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".txt")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

    # Delete RAR XZ
    directory = "./"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".xz")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

    


