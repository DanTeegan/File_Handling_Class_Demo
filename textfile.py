class Text_file_handling:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage


    # Going to read in two ways and write in two ways
    def read_text_file(self):
        # Open file
        # Read the file
        # Close the file#
        # try:
        #     file = open(self.file_path, "r")
        # except Exception as e: # Except is catching the execption
        #     print(e)
        # else:
            # self.text_storage=file.read()
            # self.text_storage=file.read(3) # Reads 3 characters in the text file
            # print(file.read(29)) # Prints the amount of characters you would like
            # self.text_storage = file.readline()
            # self.text_storage = file.readline()
            # self.text_storage = file.readlines()
            # # Here we are closing the file
        #     file.seek(3) # Telling the pointer to go back to the particular position mentioned
        #     file.close()
        #     return self.text_storage
        # finally: # Finally means it will always run irrespective wheather an eception is thrown or not
        #     file.close()
        #     print("Always run")
        pass

    def write_text_file(self):
        # Open, Write, Close
        file = open("writer.txt", "w") # 2 arguments the file and "W" means we are writing in the text file
        file.write("My first python created file")
        file.close()

        file = open("writer.txt", "a+") # using "a+" means append and read it will append to the previous file
        file.write("\nMy name is daniel teegan i am overiding the file. PYTHON!!")
        self.text_storage=file.read() # Even though we are writing to make text visible in the terminal we add this statment
        file.close()

    def read_text_file_using_with(self):
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage


    def write_text_file_using_with(self):
        # Using with so you dont need to close files all the time
        with open("writer.txt", "w+") as file: #W+ means write mode and read mode
            # This will write the text
            file.write("Using writer with functionality")
            print(file.tell()) # This tells you the current position of your pointer
            file.seek(0) # Repositioning the pointer to the begining of the file
            self.text_storage=file.read()
            return self.text_storage

    def playing_with_python_OSmodule(self):
        import os # Here we need to import the module os
        print(os.getcwd()) # Checking the current working directory
        # os.remove("writer.txt") # This will remove the file writer.txt
        print(os.listdir()) # Lists the files and directories
        # os.rename("order.txt", "modified") # Changes the name of the file
        os.chdir("C:/Users/dante/PycharmProjects/File_Handling_Class_Demo") # Changing the directory. Remember to change the direction of slashs
        print(os.getcwd()) # current working directory/ Checking to see if our directory change was sucessful
        # flags = os.O_RDWR
        # os.open("modified.txt", flags)
        os.mkdir("Daniel") # Creates a folder in the chosen directory
        os.rmdir("Daniel") # Removes the folder from the directory

    def playing_with_exception(self):
        try:
            file=open(self.file_path, "r")

            a = 10
            b = 0
            a / b

        except FileNotFoundError as e: # Never write generalized exception class before the specific exception
            print(e)
        except Exception as e:
            print("File is not avaiable bro")
        else:
            self.text_storage=file.readline()
            file.close()
        finally:
            print("Will run for sure!!!")
            return self.text_storage


    def raise_exception(self):
        try:
            first_value = (input("Enter your name"))

            if(len(first_value))==0:
                raise Exception # You are throing an Exception which Python might not have
        except Exception:
            print("We do not accept empty names!!")
        else:
            print("Thank you for enetering your name", first_value)