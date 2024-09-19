#Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.
"""import os
def dir_tree(di):
    #print(di)
    for file in os.listdir(di):
        #print("\t")
        if os.path.isdir(file):
            print("|--",file)
            print("|"+"\t", end="")
            dir_tree(file)
        else:
            print("|--"+file)
print(os.getcwd())
dir_tree(os.getcwd())"""