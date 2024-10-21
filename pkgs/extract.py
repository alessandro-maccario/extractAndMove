import os
import shutil
from tkinter import filedialog
from CustomTkinterMessagebox import CTkMessagebox


class ExtractSourceDestination:
    def __init__(self) -> None:
        self.source_directory = None  # from where you are picking the file
        self.destination_directory = None  # to where the files will be moved
        self.rename_counter = -1  # check how many times the files have been renamed

    def search_source(self):
        # browse the correct folder
        self.source_directory = filedialog.askdirectory()
        # create the destination folder if it does not exist
        self.make_folder_if_not_exists()
        return self.source_directory

    def make_folder_if_not_exists(self):
        """If the folder where to store the data does not exists, create it"""
        self.destination_directory = self.source_directory + "/destination_folder/"
        if not os.path.exists(self.destination_directory):
            os.makedirs(self.destination_directory)
            print("Directory created!")
        else:
            print("Directory already exists, no further actions performed.")

        # extract and move
        self.extract_from_folders()

    def stop_execution(self):
        if self.rename_counter >= 1:
            CTkMessagebox.messagebox(
                "Already done",
                "Files already renamed and moved successfully!",
            )
            return True
        return False

    def extract_from_folders(self):
        """Extract files from each folder and move it to the destination folder"""
        # if, in the same session, the files have already been renamed, do not continue
        self.rename_counter += 1
        print(self.rename_counter)
        check_stop_execution = self.stop_execution()

        # Loop through each folder in the source directory
        for folder_name in os.listdir(self.source_directory):
            if check_stop_execution:  # if True, stop execution
                break

            # skip the destination folder, you do not have to look into it, but in the other folders
            if folder_name == "destination_folder":
                continue
            else:
                folder_path = os.path.join(self.source_directory, folder_name)

            # Check if it's a directory
            if os.path.isdir(folder_path):
                # Loop through the files in the folder
                for file_name in os.listdir(folder_path):
                    # split the filename in filename and filextension
                    file_name, file_extension = os.path.splitext(file_name)
                    source_name = os.path.join(
                        folder_path, f"{file_name}{file_extension}"
                    )
                    destination_name = os.path.join(
                        folder_path, f"{folder_name}_{file_name}{file_extension}"
                    )

                    # rename files based on folder's name, no need to save it in a variable
                    os.rename(source_name, destination_name)

                    # Copy the files to new destination
                    shutil.copy(destination_name, self.destination_directory)
                    print(f"Copied file: {file_name} to {self.destination_directory}")

        if not check_stop_execution:
            CTkMessagebox.messagebox("Success", "All files moved successfully!")
        else:
            pass
