import os

class FileManager:
    def __init__(self, directory: str):
        self.directory = directory

    def ensure_directory_exists(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def save_file(self, file_path: str):
        self.ensure_directory_exists()
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
        return f"File saved to {self.directory}"
