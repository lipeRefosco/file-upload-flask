import os
import datetime
from time import sleep
import requests
from zipfile import ZipFile

DEFAULT_USER_DIRECTORY = os.path.expanduser("~")
DEFAULT_DIRECTORY_NAME = "raioss"
DEFAULT_DIRECTORY      = DEFAULT_USER_DIRECTORY + os.path.sep + DEFAULT_DIRECTORY_NAME
DEFAULT_URL            = "http://191.252.113.94/upload"


def main():

    go_default_directory(DEFAULT_USER_DIRECTORY, DEFAULT_DIRECTORY_NAME)

    while True:

        if have_new_file():

            # Start date time
            date = datetime.datetime.now()
            date_format = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
            hour_format = str(date.hour) + '-' + str(date.minute) + '-' + str(date.second)
            
            default_zip_name = f"{DEFAULT_DIRECTORY_NAME}_-_{date_format}_-_{hour_format}.zip"
            file_list = os.listdir()

            print("\n\n\n", file_list)
            zip_all_files(file_list, default_zip_name)
            send_files(DEFAULT_URL, DEFAULT_DIRECTORY + os.path.sep + default_zip_name)
            remove_all_original_files(file_list, default_zip_name)
        
        else:
            print(f"Monitoring the directory {DEFAULT_DIRECTORY}")
        
        sleep(2)
    
    return

def go_default_directory( user_directory : str, name_directory : str ):

    if os.path.exists(user_directory + os.path.sep + name_directory):
        os.chdir(user_directory + os.path.sep + name_directory)
        return
    else:
        os.chdir(user_directory)
        os.mkdir(name_directory)
        go_default_directory(user_directory, name_directory)

def zip_all_files(list_files : list, output_name : str, directory : str = "."):
    # Zip all files from directory.

    # Create a zip file
    with ZipFile(f"{directory}{os.path.sep}{output_name}", 'w') as zip:
        
        print(f"Creating zip file \"{output_name}\"!")

        for file in list_files:
            # Escape directory
            if os.path.isdir(file):
                continue
            
            print(f"Zipping file \"{file}\"")
            
            zip.write(file)
        
        print('Zip file created!')
    
    return

def remove_all_original_files(list_files : list, default_zip_name : str):
    print('Removing all files...')

    list_files.append(default_zip_name)

    for file in list_files:
        # Remove directory
        if os.path.isdir(file):
            continue
        print(f"Removing file \"{file}\"")
        os.remove(file)

    return

def send_files(url : str, file_path : str):

    all_files = {'file' : open(file_path, 'rb')}
    res = requests.post(url, files=all_files)
    print(res.text)
    return

def have_new_file():
    actual_files = os.listdir()
    return True if len(actual_files) != 0 else False

if __name__ == "__main__":
    main()