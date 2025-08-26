import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

def organize_files(folder_path):
    # Create a log file with UTF-8 encoding
    log_file = os.path.join(folder_path, "file_organizer_log.txt")

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Ensures that only files are looked at
        if os.path.isfile(file_path):
            # Get file extension
            ext = os.path.splitext(filename)[1].lower()
            if not ext:
                ext = "no_extension"

            # Create category folder if it doesn't exist
            category_folder = os.path.join(folder_path, ext.replace(".", "").upper())
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            # Handle duplicate filenames
            dest_path = os.path.join(category_folder, filename)
            counter = 1
            while os.path.exists(dest_path):
                name, extension = os.path.splitext(filename)
                dest_path = os.path.join(category_folder, f"{name}({counter}){extension}")
                counter += 1

            # Move file
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} -> {category_folder}")
            with open(log_file, "a", encoding="utf-8") as log:
                log.write(f"Moved {filename} -> {category_folder}\n")

if __name__ == "__main__":
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    print("Please select the folder you want to organize...")
    folder_path = askdirectory(title="Select Folder to Organize")

    if folder_path:
        organize_files(folder_path)
        print("Folder organized successfully!")
    else:
        print("No folder selected. Exiting.")
