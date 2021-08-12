from services.user_interface import UserInterface
from  services.data_extractor import DataExtractor
from  services.file_manager import FileManager

def main():
    print("App running")

    UserInterface.show_dialog_window()
    option = UserInterface.get_option()

    if (option == 1):
        print("option one")
        dir_path = UserInterface.get_dir()
        
        extractor = DataExtractor(dir_path)

        files_with_dates = extractor.extract_created_at_date()
        files_with_years = extractor.to_years(files_with_dates)

        file_manager = FileManager(dir_path, files_with_years)
        file_manager.create_folders()
        file_manager.move_files()



if __name__ == "__main__":
    main()