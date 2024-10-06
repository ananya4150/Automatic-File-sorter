import shutil
import os

path = input("Enter the path of folder you want to organize: ")
files = os.listdir(path)     #storing all file names in the location as a list

for file in files:
	filename,extension = os.path.splitext(file)   # splitting the file name in name and its extension
	extension = extension[1:]  # removing '.'

	if os.path.exists(path+'/'+extension): # checks if the folder of that extension exists 
		shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
	else:
		os.makedirs(path+'/'+extension)
		shutil.move(path+'/'+file,path+'/'+extension+'/'+file)