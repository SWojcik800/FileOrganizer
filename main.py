from services.user_interface import UserInterface
from  services.data_extractor import DataExtractor
from  services.file_manager import FileManager

def main():
    print("App running")

    UserInterface.show_dialog_window()
    option = UserInterface.get_option()

    print("Select directory: \n")
    dir_path = UserInterface.get_dir()



    extractor = DataExtractor(dir_path)

    if (option == 1):

        files_with_dates = extractor.extract_created_at_date()
        files_with_years = extractor.to_years(files_with_dates)

        file_manager = FileManager(dir_path, files_with_years)
        file_manager.create_folders()
        file_manager.move_files()

        print("Task completed")

    if (option == 2):

        files_with_first_letters = extractor.extract_first_letters_of_files()
        file_manager = FileManager(dir_path, files_with_first_letters)

        file_manager.create_folders()
        file_manager.move_files_ignore_case()


        print("Task completed")

if __name__ == "__main__":
    main()