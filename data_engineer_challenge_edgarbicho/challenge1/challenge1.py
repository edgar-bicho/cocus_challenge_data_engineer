import sys
import glob
import os

def is_valid_arguments():

    if (len(sys.argv) != 3):
        print("Invalid number of arguments: expected 2, given:" , len(sys.argv)-1)
        return False
    if not os.path.exists(sys.argv[2]):
        print("Path provided does not exist:", sys.argv[2])
        return False
    return True


def search_files(path, pattern):
    ''' performs the search using path and pattern '''
    try:
        path_and_pattern = os.path.join(path, '**/'+pattern)

        # with option recursive = True to look inside subfolders
        # will match any files and zero or more directories and subdirectories
        files = glob.glob(path_and_pattern, recursive=True)
        
        # will remove directories and list only files
        files = [f for f in files if os.path.isfile(f)]

        return files
    except Exception as e:
        print("Something went wrong.", e)
        return []

if (__name__=="__main__"):
    # valid command line arguments number and path existance
    if not is_valid_arguments():
        quit()

    files = search_files(sys.argv[2], sys.argv[1])

    for file in files:
        print (file)

        
    

 


