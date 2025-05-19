# Menu-driven file handling program with basic exception handling

#function for write
def write_file():

    try:

        with open("employees.txt", "w") as file:

            file.write("ID,Name,Department,Salary\n")

            file.write("101,Alice,HR,50000\n")

            file.write("102,Bob,IT,60000\n")

        print("File written successfully.")

    except FileNotFoundError:

        print("Error: The file was not found.")

    except PermissionError:

        print("Error: You do not have permission to write to the file.")

    except ValueError:

        print("Error: Invalid value while writing to the file.")

    except TypeError:

        print("Error: Type mismatch while writing to the file.")

    except Exception:

        print("An error occurred while writing to the file.")

#function for read
def read_file():

    try:

        with open("employees.txt", "r") as file:

            print("Reading file contents:")

            for line in file:

                print(line.strip())

    except FileNotFoundError:

        print("Error: The file was not found.")

    except PermissionError:

        print("Error: You do not have permission to read the file.")

    except ValueError:

        print("Error: Invalid value while reading the file.")

    except TypeError:

        print("Error: Type mismatch while reading the file.")

    except Exception:

        print("An error occurred while reading the file.")

#function for append
def append_file():

    try:

        with open("employees.txt", "a") as file:

            file.write("103,Charlie,Finance,55000\n")

        print("File appended successfully.")

    except FileNotFoundError:

        print("Error: The file was not found.")

    except PermissionError:

        print("Error: You do not have permission to append to the file.")

    except ValueError:

        print("Error: Invalid value while appending to the file.")

    except TypeError:

        print("Error: Type mismatch while appending to the file.")

    except Exception:

        print("An error occurred while appending to the file.")

#main function
def main():

    while True:

        print("\nMenu:")

        print("1. Write a file")

        print("2. Read a file")

        print("3. Append a file")

        print("4. Exit")

        try:

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:

                write_file()

            elif choice == 2:

                read_file()

            elif choice == 3:

                append_file()

            elif choice == 4:

                print("Exiting the program.")

                break

            else:

                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:

            print("Invalid input. Please enter a valid number.")

        except Exception:

            print("An unexpected error occurred.")

if __name__ == "__main__":

    main()
 