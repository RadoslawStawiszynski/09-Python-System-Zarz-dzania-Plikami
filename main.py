# STAWISZYNSKI RADOSLAW , NR INDEKSU 159088, 
# ROK 2022/2023, WYDZIAL INFORMATYKA, GRUPA D1, SEM 2

from file_manager import FileManager

# Funkcja do wyświetlania menu
def display_menu():
    print("=== Menu ===")
    print("1. Utwórz plik")
    print("2. Utwórz katalog")
    print("3. Wyświetl pliki w katalogu")
    print("4. Zmodyfikuj plik")
    print("5. Skopiuj plik")
    print("6. Usuń plik")
    print("7. Skopiuj katalog")
    print("8. Usuń katalog")
    print("0. Wyjście")

if __name__ == "__main__":
    file_manager = FileManager()

    while True:
        display_menu()
        choice = input("Wybierz numer funkcji (0-8): ")

        if choice == "0":
            print("Zamykanie programu. Do widzenia!")
            print()
            break

        elif choice == "1":
            file_path = input("Podaj ścieżkę i nazwę nowego pliku (np. C:/Users/informatyka/Desktop/eco_plik.txt): ")
            content = input("Czy chcesz wprowadzić zawartość pliku? (T/N): ").lower()
            
            if content == "t":
                content = input("Podaj zawartość pliku: ")
                file_manager.create_file(file_path, content)
            else:
                file_manager.create_file(file_path)
            print()

        elif choice == "2":
            dir_path = input("Podaj ścieżkę do nowego katalogu (np. C:/Users/informatyka/Desktop/eco_data/): ")
            file_manager.create_directory(dir_path)
            print()

        elif choice == "3":
            dir_path = input("Podaj ścieżkę do katalogu: ")
            file_manager.list_files(dir_path) 
            print()

        elif choice == "4":
            file_path = input("Podaj ścieżkę do pliku do modyfikacji: ")
            new_content = input("Podaj nową zawartość pliku: ")
            file_manager.modify_file(file_path, new_content)
            print()

        elif choice == "5":
            source_path = input("Podaj ścieżkę do pliku źródłowego: ")
            destination_path = input("Podaj ścieżkę do pliku docelowego: ")
            file_manager.copy_file(source_path, destination_path)
            print()

        elif choice == "6":
            file_path = input("Podaj ścieżkę do pliku do usunięcia: ")
            file_manager.delete_file(file_path)
            print()

        elif choice == "7":
            source_path = input("Podaj ścieżkę do katalogu źródłowego: ")
            destination_path = input("Podaj ścieżkę do katalogu docelowego: ")
            file_manager.copy_directory(source_path, destination_path)
            print()

        elif choice == "8":
            dir_path = input("Podaj ścieżkę do katalogu do usunięcia: ")
            file_manager.delete_directory(dir_path)
            print()

        else:
            print("Nieprawidłowy numer funkcji. Spróbuj ponownie.")
            print()
