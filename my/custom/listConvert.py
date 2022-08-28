''' 
1. To create your own list, just edit and save "OriginalList.txt". Each new line will be a new value in your list...

2. In Command Prompt or Terminal, change your workinig directory (cd) to the folder that contains this file...basically go to this folder like this below:
'''
#    cd /Path/To/The/Folder/.../FactGen/my/custom

'''
3. Once in this folder with new Virtual Environment created and activated, run this file by typing the command like this below:
'''
#    python listConvert.py    

'''
4. Now to see your own custom list in the GUI, go back/up two folders (cd ../../) to the parent folder and run the main file "FactGen.py" in the same way as before by typing the command like this below:
'''
#    python FactGen.py    

##################################################################################################
import os
import sys


clean_lines = []
def Clean(filename):
    """Temporarily creates a new file called "ReformattedList.txt", removing empty lines and 
    lines that contain only whitespace. This will not overwrite OriginalList.txt"""

    with open(filename, "r") as in_file:
        all_lines = in_file.readlines()
        clean_lines = [eachline.strip() for eachline in all_lines if eachline.strip()]

    with open("ReformattedList.txt", "x") as out_file:
        out_file.writelines('\n'.join(clean_lines))

Clean("OriginalList.txt")   #<-- Insert "OriginalList.txt" to clean file of white space and prepare it for python.py list [] format. This will output a file called "factListModule.py", which will be neccessary for generating facts.

##################################################################################################

def Reformat(filename):
    """Creates a new .py file called "factListModule.py" that contains all the 
    facts in a list [] format."""

    factlist = []
    with open(filename, "r") as in_file:
        #factlist = in_file.readlines(80996) #<-- Insert "ReformattedList.txt" file size in bytes
        #factlist = in_file.read().splitlines()   #OR
        factlist = list(in_file)                  #OR

    with open ("factListModule.py", "a+") as out_File:
        out_File.write("import os\nimport sys\n\n\nfactlist = ")

    with open ("factListModule.py", "a+") as out_file:
        print(factlist, file = out_file)

Reformat("ReformattedList.txt")

##################################################################################################

os.remove("ReformattedList.txt") # Comment this out if you want to view the "ReformattedList.txt" and/or want to use the .readlines() function.