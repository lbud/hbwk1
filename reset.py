import os, shutil, glob

foldernames = range(97, 123)
foldernames[:] = [chr(foldername) for foldername in foldernames]

[shutil.move(filename, 'files/') for foldername in foldernames for filename in glob.glob(foldername + '/*.txt')]

[os.rmdir(eachfolder) for eachfolder in foldernames]