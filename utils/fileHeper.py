import os

class FileHelper:
    @classmethod
    def not_exist_create_folder(self, folder_name=""):
        # check folder log
        path = os.path.join(folder_name)
        # Check Folder nếu chưa có thì tạo
        path_folder = os.path.join(path)
        if not os.path.exists(path_folder):
            os.makedirs(path_folder)
        
