class UserInterface:

    @staticmethod
    def show_dialog_window():
        print("Select option from below\n")
        print("1. Organise files by year \n")
        print("2. Organise files by first letter \n")

    @staticmethod
    def get_option():
        return int(input())

    @staticmethod
    def get_dir():
        return input()


