import shutil
import os

class FileManager:

    def __init__(self, base_dir: str, formated_data: str ):
        self.formated_data = formated_data
        self.base_dir = base_dir
        self.folder_names = None



    def move_files(self):

        folder_names = set([i[1] for i in self.formated_data])
        self.folder_names = folder_names

        for item in self.formated_data:
            try:
                file = item[0]
                dest = f"{self.base_dir}/{item[1]}"

                if not (os.path.exists(dest) and os.path.isdir(dest)):
                    try:
                        os.mkdir(dest)
                    except:
                        pass

                #ignore created folders
                if (file in self.folder_names): continue


                shutil.move(file, dest)
                print(f"{file} MOVED TO {dest}")
            except:
                pass

    def move_files_ignore_case(self):

        for item in self.formated_data:
            item[1] = item[1].upper()

        self.move_files()





