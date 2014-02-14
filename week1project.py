import shutil, os

# create list of all sourec files
source = os.listdir("files/")

# make 26 folders, one for each letter of the alphabet using ascii vals
for i in range(97, 123):
    os.mkdir(chr(i))

# loop through filename list, move it to appropriate folder
for filename in source:
    shutil.move("files/" + filename, filename[0] + '/')