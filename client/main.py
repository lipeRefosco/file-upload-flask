
from array import array
import datetime
import os
from zipfile import ZipFile

date = datetime.datetime.now()
date_format = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
hour_format = str(date.hour) + ':' + str(date.minute) + ':' + str(date.second)

DEFAULT_USER_DIRECTORY = os.path.expanduser("~")
DEFAULT_DIRECTORY_NAME = "raioss"
DEFAULT_DIRECTORY      = DEFAULT_USER_DIRECTORY + DEFAULT_DIRECTORY_NAME
DEFAULT_ZIP_NAME    = f"{DEFAULT_DIRECTORY_NAME}_-_{date_format}_{hour_format}.zip"

def main():

    go_default_directory(DEFAULT_USER_DIRECTORY, DEFAULT_DIRECTORY_NAME)
    
    zip_all_files(DEFAULT_ZIP_NAME)

    return

def go_default_directory( user_directory : str, name_directory : str ):

    if os.path.exists(user_directory + os.path.sep + name_directory):
        os.chdir(user_directory + os.path.sep + name_directory)
        return
    else:
        os.chdir(user_directory)
        os.mkdir(name_directory)
        go_default_directory(user_directory, name_directory)

def zip_all_files(output_name : str, directory : str = "."):
    # Zip all files from directory.

    # List of files
    files = os.listdir()

    # Create a zip file
    with ZipFile(f"{directory}{os.path.sep}{output_name}", 'w') as zip:
        
        print(f"Creating zip file \"{output_name}\"!")

        for file in files:
            # Escape zip file or directory
            if '.zip' in file or os.path.isdir(file):
                continue
            
            print(f"Zipping file \"{file}\"")
            
            zip.write(file)
        
        print('Zip file created!')
    
    remove_all_original_files(files)

    return

def remove_all_original_files(list_files = array):
    for file in list_files:

        # Remove directory
        if os.path.isdir(file):
            continue

        os.remove(file)

    return

if __name__ == "__main__":
    main()