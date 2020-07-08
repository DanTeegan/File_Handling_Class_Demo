# Reading from and writing to files
# Exception handling
# CSV
# Assignments

# importing the class from the textfile file
from textfile import Text_file_handling

# Defining the path of the file
file_path="order.txt"

# Creating an object
textfileobject = Text_file_handling(file_path)

# print(textfileobject.read_text_file())
#
# textfileobject.write_text_file();
#
# print(textfileobject.write_text_file())
#
# print(textfileobject.read_text_file_using_with())

print(textfileobject.write_text_file_using_with())

