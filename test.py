from favicons import Favicons
import zipfile
import os
import random
from time import sleep

# creates a folder user the user_id
id = 5      #this is the user_id to different the user files in the media root
img_name = "captain.jpg"
folder_path = f"./output/user{id}"  #a path created using the user_id which is unique

# makes a folder
if os.path.isdir(folder_path):
    print("it's created already")
else:
    os.mkdir(folder_path)

YOUR_ICON = f"./uploads/{img_name}"     #this is the path to the image uploaded
WEB_SERVER_ROOT = f"./output/user{id}"  #this is the directory where we want the output to be

# from the favicons library this generates the favicon and html codes
with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
    # generate favicon
    favicons.generate()
    # As generator
    html = favicons.html_gen()
    #  as tuple
    html = favicons.html() # this would be passed as context to the templates

file_name = "html.txt" #this is the txt file to hold the html codes
html_file = open(os.path.join(WEB_SERVER_ROOT,file_name),"w")   #we open the file

html_file.writelines("Copy the required code snippet into your HTML file\n\n") 
#we write the codes generated
for code in html:
    html_file.writelines(code+"\n")
html_file.close()

# gets all the files in the user directory
all_files= os.listdir(folder_path)
# this exempts .zip files and grabs the generated favicons
needed_files = [file for file in all_files if file.endswith('.png') or file.endswith('.ico') or file.endswith('.jpeg') or file.endswith('.txt') ]


# creates a zipfile path
zip_name = f"{WEB_SERVER_ROOT}/user{id}.zip"

# check if the filename exists
if os.path.isfile(zip_name):
    # this creates a random number to prevent conflicts in names
    any = random.randint(0,1000)
    zip_name = f"{WEB_SERVER_ROOT}/user{id+any}.zip"
else:
    pass

# this zips the files in the needed files
with zipfile.ZipFile(zip_name, mode="w") as archive:
    for icon in needed_files:
        archive.write(f"{folder_path}/{icon}")
archive.close()

# waits for 5s before continuing the process of deleting
sleep(5)
# deletes the unneeded files
for file in needed_files:
    os.remove(os.path.join(WEB_SERVER_ROOT,file)) 


# Pls note this code will be worked upon to work well and algorithmically fast in a django environment
# Also it would be further broken into functions for better readability
# You are to test the program to check for vulnerabilities and understand it.