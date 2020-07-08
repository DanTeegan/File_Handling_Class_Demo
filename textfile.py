class Text_file_handling:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage


    # Going to read in two ways and write in two ways
    def read_text_file(self):
        # Open file
        # Read the file
        # Close the file
        file = open(self.file_path, "r")
        # self.text_storage=file.read()
        # self.text_storage=file.read(3) # Reads 3 characters in the text file
        # print(file.read(29)) # Prints the amount of characters you would like
        self.text_storage = file.readline()
        self.text_storage = file.readline()
        self.text_storage = file.readlines()
        # Here we are closing the file
        file.seek(3) # Telling the pointer to go back to the particular position mentioned
        file.close()
        return self.text_storage
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

