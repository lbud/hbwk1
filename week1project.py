import shutil, os

source = os.listdir("files/")




foldernames = range(97, 123)

foldernames[:] = [chr(foldername) for foldername in foldernames]

[os.mkdir(foldername) for foldername in foldernames]




[shutil.move("files/" + filename, filename[0] + '/') for filename in source]