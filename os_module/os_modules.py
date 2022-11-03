import os
import shutil

# get current working directory using os module

cur_dir = os.getcwd()
print(cur_dir)

# Create directory on specific or current location

#os.mkdir("MyTechFocus") # create directory on current path
#os.mkdir("D:\\execute_code\\Tushar")

# Delete directory
# os.rmdir("D:\\execute_code\\Tushar")






# Get list of files/folder from target directory
"""
data = os.listdir("E:\\Filesdata")
print(data)
for file in data:
    print(file)

"""

# Check given data is files or folder

output = os.path.isdir("E:\\Filesdata\\count_name.txt")
print("output :", output)  # False

output3 = os.path.isdir("E:\\Filesdata\\BI10")
print("output3 :", output3) #

output2 = os.path.isfile("E:\\Filesdata\\count_name.txt")
print("output2 :", output2)  # True

# Join two path
path1 = "E:\\Filesdata"
path2 = "BI11"

"""
BI11_path = os.path.join(path1, path2)
print(BI11_path)
os.mkdir(BI11_path)
"""

""""
patha = "D:\\report"
pathb = "Python\\fol2"

path11 = os.path.join(patha, pathb)
print(path11)

os.mkdir(path11)
"""
# write a python program to create 10 nested folder
"""
base_path = "D:\\report"

for i in range(1, 10):
    folder_name = f'fld{i}'
    new_path = os.path.join(base_path, folder_name)
    os.mkdir(new_path)
    base_path = new_path
"""

########################################
# Copy file from one location to another location

file_path = "D:\\report\\report.html"
target_path = "D:\\report\\fld1\\fld2\\fld3\\fld4\\fld5\\fld6\\fld7\\fld8\\report.html"

shutil.copy(file_path, target_path)

# Write a python to copy all the files from source to target location

def copy_file_src_tar(src_path, tar_path):
    data_list = os.listdir(src_path) # get all the file/folder from source location
    for data in data_list: # apply loop on list of data (files/folders)
        src_data_path = os.path.join(src_path, data)  # Get source path each file/folder
        #tar_data_path = os.path.join(tar_path, data)  # Get target path of each file/folder
        if os.path.isfile(src_data_path): # Check given path is file or not
            shutil.copy(src_data_path, tar_data_path) # if given path is file , then copy it on tar location.
        else:
            continue


copy_file_src_tar("E:\\Filesdata", "D:\\report\\Python")

# Write program to get count the each type file in given directory
output = {'txt': 3, 'png': 5, 'jpeg': 6}

# Write a python program to copy different extension in different specific folder.