class UserInterface:

    @staticmethod
    def show_dialog_window():
        print("Select option from below\n")
        print("1. Organise files by year \n")
        print("2. Organise files by first letter \n")
        print("3. Organise files by year and month \n")
        print("4. Organise files by extension \n")

    @staticmethod
    def confirm(message: str):
        print(f"{message} Y or N?")
        return input().lower() == 'y'

    @staticmethod
    def get_option():
        return int(input())

    @staticmethod
    def get_dir():
        return input()


