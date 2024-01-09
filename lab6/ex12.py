import os
import sys


def Test(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid Directory Path")
        
        print(f"Files with extension {extension} in directory {directory}:")
        flag = False
        for file in os.listdir(directory):
            if file.endswith(extension):
                filePath = os.path.join(directory, file)
                try:
                    content = open(filePath, "rt").read()
                    print(f"File: {filePath}:")
                    print(content)
                    flag=True
                except Exception as e:
                    print(f"Error accessing file {filePath}:" + str(e))
        if flag == False:
            print("There is no file with that extension")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occured {e}")



x = sys.argv[1]
y = sys.argv[2]
Test(x,y)