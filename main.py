from services.user_interface import UserInterface
from  services.data_extractor import DataExtractor
from  services.file_manager import FileManager
import helpers.config_parser as parser

def main():
    print("App running")

    use_settings_from_config_file = UserInterface.confirm("Use settings from config file")

    if (use_settings_from_config_file):
        config = parser.parse()
        dir_path = config['Path']
        option = int(config['Option'])

        if (UserInterface.confirm(f"Path: {dir_path}, Option: {option}")):
            extractor = DataExtractor(dir_path.strip())
        else:
            return

    else:
        UserInterface.show_dialog_window()
        option = UserInterface.get_option()
        print("Select directory: \n")
        dir_path = UserInterface.get_dir()


    extractor = DataExtractor(dir_path)

    if option == 1:

        files_with_dates = extractor.extract_created_at_date()
        print(files_with_dates)
        files_with_years = extractor.to_years(files_with_dates)

        file_manager = FileManager(dir_path, files_with_years)
        file_manager.move_files()

        print("Task completed")

    if option == 2:

        files_with_first_letters = extractor.extract_first_letters_of_files()
        file_manager = FileManager(dir_path, files_with_first_letters)
        file_manager.move_files_ignore_case()


        print("Task completed")

    if option == 3:
        files_with_dates = extractor.extract_created_at_year_and_month()
        file_manager = FileManager(dir_path, files_with_dates)
        file_manager.move_files()

        print("Task completed")

    if option == 4:
        files_with_extensions = extractor.extract_file_extensions()
        file_manager = FileManager(dir_path, files_with_extensions)
        file_manager.move_files_ignore_case()
        print("Task completed")

if __name__ == "__main__":
    main()