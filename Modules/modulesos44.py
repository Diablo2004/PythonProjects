import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# List files in the current directory
files_in_directory = os.listdir('..')
print("Files in current directory:")
for file in files_in_directory:
    print(file)

# Create a new directory
#os.mkdir("FileHandling")
print("New directory 'FileHandling' created.")

print(f"Operating System: {os.name}")


# Get all environment variables
env_vars = os.environ
print("Environment Variables:")
for key, value in env_vars.items():
    print(f"{key}: {value}")

# Get a specific environment variable (e.g., PATH)
path_var = os.getenv("PATH")
print(f"\nSystem PATH: {path_var}")

file_path = "example.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted.")
else:
    print("File not found!")


#Get OS name    =   os.name
#Get environment variables  =   os.environ
#Get current directory   =	os.getcwd()
#Change directory   =	os.chdir(path)
#List files =   os.listdir(path)
#Create a directory =   os.mkdir(path)
#Create nested directories  =   os.makedirs(path)
#Rename a directory/file    =	os.rename(old, new)
#Remove a directory =   os.rmdir(path)
#Remove a file  =	os.remove(path)
#Get file size  =	os.path.getsize(path)
#Get absolute path	=    os.path.abspath(path)
#Check if file exists   =	os.path.exists(path)
#Execute system commands     =	os.system(command)
#Delete non-empty directory     =	shutil.rmtree(path)
