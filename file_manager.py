import os
import shutil
from datetime import datetime

class FileManager:
    def __init__(self, log_file="log.txt"):
        self.log_file = log_file

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        with open(self.log_file, 'a') as log:
            log.write(log_entry)

    def create_file(self, file_path, content=""):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            self.log(f"Utworzono plik: {file_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def create_directory(self, dir_path):
        try:
            os.makedirs(dir_path, exist_ok=True)
            self.log(f"Utworzono katalog: {dir_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def list_files(self, dir_path="."):
        try:
            files = os.listdir(dir_path)
            for file in files:
                print(file)
            self.log(f"Wyświetlono pliki w katalogu: {dir_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def modify_file(self, file_path, new_content):
        try:
            with open(file_path, 'w') as file:
                file.write(new_content)
            self.log(f"Zmodyfikowano plik: {file_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def copy_file(self, source_path, destination_path):
        try:
            shutil.copy2(source_path, destination_path)
            self.log(f"Skopiowano plik z {source_path} do {destination_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            self.log(f"Usunięto plik: {file_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def copy_directory(self, source_path, destination_path):
        try:
            shutil.copytree(source_path, destination_path)
            self.log(f"Skopiowano katalog z {source_path} do {destination_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def delete_directory(self, dir_path):
        try:
            shutil.rmtree(dir_path)
            self.log(f"Usunięto katalog: {dir_path}")
        except Exception as e:
            print(f"Błąd: {e}")
