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

    def extract_created_at_year_and_month(self):
        files_with_dates = self.extract_created_at_date()
        months = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12",
        }

        for item in files_with_dates:
            year = item[1].split(' ')[-1]
            month = item[1].split()[1]
            item[1] = f"{year}_{months[month]}"
            item[0] = f"{self.directory}/{item[0]}"
        print(files_with_dates)
        return files_with_dates

    def extract_first_letters_of_files(self):
        files = self.extract_file_names()
        files_with_letters = [ [ i[0], i[1].strip()[0].upper() ] for i in files]

        return files_with_letters

    def extract_file_extensions(self):
        files = os.listdir(self.directory)

        files_with_extensions = [ [ f"{self.directory}/{f}" ,os.path.splitext(f)[1][1::].upper() ] for f in files  ]
        return files_with_extensions
