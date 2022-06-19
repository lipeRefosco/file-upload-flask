
import os

DEFAULT_FOLDER_NAME = "raioss"

def main():

    path_user_folder = os.path.expanduser("~")

    go_default_folder(path_user_folder, DEFAULT_FOLDER_NAME)

    return

def go_default_folder( user_folder : str, name_folder : str ):

    if os.path.exists(user_folder + os.path.sep + name_folder):
        os.chdir(user_folder + os.path.sep + name_folder)

    else:
        os.chdir(user_folder)
        os.mkdir(name_folder)
        go_default_folder(user_folder, name_folder)

if __name__ == "__main__":
    main()