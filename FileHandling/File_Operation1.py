"""
obj = open(filename/filepath, mode)
obj.(Operation)

mode :
r : (read)read the content of the file
w : (write)write a content to the file
a : (append)  append the content to the any existing file
"""
# read mode : we can read data of any existing file available on the system.
"""
file = open("read_data.txt", "r")
data = file.read()
print(data)
file.close()
"""

# write mode
# Case 1: If we don't have required file on current location, then the new file will be created with the given name
"""
content = "Its very Friday , we are going to enjoy weekend"
file = open("read_data_write.txt", "w")
data = file.write(content)
print(data)
file.close()
"""
# Case 2: When we open a existing file with write and add some content to it, then existing content
# of the file will overwrite

"""
content = "Its Friday , we are going to enjoy weekend"
file = open("read_data.txt", "w")
file.write(content)
file.close()
"""

# Append mode : add the content to the existing file
# case1 : when we open non-existing with append mode, then new file will be created and will add data to the file
"""
content = "Its Friday , we are going to enjoy weekend"
file = open("read_data_append2.txt", "a")
file.write(content)
file.close()
"""

# case2 : when we open existing file with append mode, then new data will add at end of file
"""
content = "\nIts Friday , we are going to enjoy weekend"
file = open("read_data_append.txt", "a")
file.write(content)
file.close()

print("filname :", file.name)
print("filname mode:", file.mode)
#print("filname module:", str.__module__())
"""
"""
class ABC():
   pass
obj = ABC()
print(obj.__module__)
"""


########### Open file with binary ################
# with mode : r
"""
file = open("read_data.txt", 'r')
data = file.read()
print(data, ":", type(data))
file.close()
"""
# open file with read and binary
"""

file = open("read_data.txt", 'rb')
data = file.read()
print(data, ":", type(data))
file.close()  # b'Its Friday , we are going to enjoy weekend\r\n\r\n' : <class 'bytes'>

"""

# read file with read, binary, plus operation
# plus operator provide open the file in both read and write mode.
"""
file = open("read_data.txt", 'rb')
data = file.write(b"Good Morning aahjkhdfadf")
print(data, ":", type(data))
file.close()  # b'Its Friday , we are going to enjoy weekend\r\n\r\n' : <class 'bytes'>
"""

# Context Manager
# Context manager has its own enter and exit method, so no need to close file explicitly. it will close automaticaly once
# program is done
"""
with open("read_data_context.txt", "r") as file:
    data = file.read()
    print(data)
"""
#print(file.read())


# read specific number of character from the file

def read_char(filename, char_count):
    with open(filename, 'r') as file:
        data = file.read(char_count)

    return data

#result = read_char('read_data.txt', 10)
#print("result :", result)

# read line from given file

def read_line(filename, line_count):
    with open(filename, 'r') as file:
        for i in range(line_count):
            line = file.readline()
            print(line)

#read_line('read_data.txt', 5)

# read list of lines

def read_all_lines(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

#result = read_all_lines("read_data.txt")
#print(result) : it will print list of all the lines

# write a program to read last 5 lines

def read_last_lines(filename, line_count):
    all_lines = read_all_lines(filename)
    for i in range(-line_count, 0, 1):
        print(all_lines[i], ":", i)

#read_last_lines("read_data.txt", 5)

# tell method(obj.tell()) : tell provides the current location of the cursur
# seek method(obj.seek()) : this method help to move cursur from one location to another location
# offet : number  of byte movement
# set_index: 0 : read from begining of the file
#            1 : read from current cursur movement
#            2 : read from end of the file

def check_cursur_movement(filename):
    with open(filename, 'rb') as file:
        # current location before read
        print("current_location:", file.tell())
        char10 = file.read(10)
        print("char10:", char10)
        print("current_location_After_10char:", file.tell())
        # set cursur location on 20th char
        #file.seek(20, 0)  # move cursur from begining of the file
        file.seek(20, 1) # move cursur from current cursur location
        print("current_location_After_20char:", file.tell())
        char10 = file.read(10)
        print(char10)
        print("current_location_After_30char:", file.tell())
        file.seek(-20, 2)  # move cursur from end of the file location
        print("tell location from end of the file:", file.tell())
        remaining = file.read()
        print("remaining :", remaining)

check_cursur_movement("read_data.txt")