
import datetime
import os
from zipfile import ZipFile

date = datetime.datetime.now()
date_format = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
hour_format = str(date.hour) + ':' + str(date.minute) + ':' + str(date.second)

DEFAULT_USER_FOLDER = os.path.expanduser("~")
DEFAULT_FOLDER_NAME = "raioss"
DEFAULT_FOLDER      = DEFAULT_USER_FOLDER + DEFAULT_FOLDER_NAME
DEFAULT_ZIP_NAME    = f"{DEFAULT_FOLDER_NAME}_-_{date_format}_{hour_format}.zip"

def main():

    go_default_folder(DEFAULT_USER_FOLDER, DEFAULT_FOLDER_NAME)
    
    zip_all_files(DEFAULT_ZIP_NAME)

    return

def go_default_folder( user_folder : str, name_folder : str ):

    if os.path.exists(user_folder + os.path.sep + name_folder):
        os.chdir(user_folder + os.path.sep + name_folder)
        return
    else:
        os.chdir(user_folder)
        os.mkdir(name_folder)
        go_default_folder(user_folder, name_folder)

def zip_all_files(output_name : str, folder : str = "."):
    # Zip all files from folder.

    # List of files
    files = os.listdir()

    # Create a zip file
    with ZipFile(f"{folder}{os.path.sep}{output_name}", 'w') as zip:
        
        print(f"Creating zip file \"{output_name}\"!")

        for file in files:
            # Escape zip file
            if '.zip' in file:
                continue
            
            print(f"Zipping file \"{file}\"")
            
            zip.write(file)
        
        print('Zip file created!')
        
    return

if __name__ == "__main__":
    main()