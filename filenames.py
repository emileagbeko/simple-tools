import os

def get_file_names(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_names.append(file)
    return file_names

## This function takes a folder_path as input and returns a list of file names present in that folder. 
## The function initializes an empty list of file_names to store the file names.

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder: ")
    if os.path.exists(folder_path):
        file_names_list = get_file_names(folder_path)
        print("List of file names in the folder:")
        for file_name in file_names_list:
            print(file_name)
    else:
        print("Folder path not found.")
