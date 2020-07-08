class Homework:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    # Creating the class
    def raise_exception_task(self):
        # Start of our Errors and Exceptions code
        #while True:
            try:
                # Asking a input from the user
                first_value = str(input("Enter your name: "))

                # Creating a file called homework to write in
                file = open("homework.txt", "w")
                # Writing the user input into the file
                file.write(first_value)

                # Opening the homework.txt file just created. using w+ to read and write.
                with open("homework.txt", "w+") as file:
                    self.text_storage = file.read()
                    file = open("homework2.txt", "w")
                    file.write(self.text_storage)
                # Checking the length of the input if 0 raise Exception
                if len(first_value) == 0:
                    raise Exception
            except Exception:
                print("We do not accept empty names!!")
            else:
                print("Thank you for entering your name")


file_path="homework.txt"

textfileobject = Homework(file_path)
textfileobject.raise_exception_task()

# Accept from the user some text. Ensure user enters something else raise an exception.

# After that write that text to a file and then read from this file to  write to another file simultaneously

# 	2. Reading an image to  writing to another file simultaneously