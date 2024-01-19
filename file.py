import os
import shutil

source = "C:/Users/96659/Downloads"
destination = "C:/Users/96659/Desktop/File Organisation 1"
allfiles = os.listdir(source)
#print(allfiles)

for filename in allfiles:
    name,extension = os.path.splitext(filename)
    print(name)
    print(extension)
