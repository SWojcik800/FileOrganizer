import os
import time


class DataExtractor:

    def __init__(self, directory: str):
        self.directory = directory


    def extract_date(self, option: str):
        files = os.listdir(self.directory)

        if option == "createdAt":
            get_time = lambda x: time.ctime(os.path.getctime(x))
        if option == "modifiedBy":
            get_time = lambda x: time.ctime(os.path.getmtime(x))

        files_with_times= [ [ i, get_time(self.directory + "/" + i) ] for i in files ]

        return files_with_times

    def to_years(self, data):

        data = [ [ self.directory + "/" + i[0], i[1].split(' ')[-1]] for i in data ]
        return data

    def extract_created_at_date(self):
        files_with_c_times = self.extract_date("createdAt")
        return files_with_c_times

    def extract_modified_by_date(self):
        files_with_m_times = self.extract_date("modifiedBy")
        return files_with_m_times

    def extract_file_names(self):
        files = os.listdir(self.directory)

        files_with_names = [[f"{self.directory}/{i}", i] for i in files]
        return files_with_names


    def extract_first_letters_of_files(self):
        files = self.extract_file_names()
        files_with_letters = [ [ i[0], i[1].strip()[0].upper() ] for i in files]

        return files_with_letters
