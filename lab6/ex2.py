import os

i=0
for (root,directories,files) in os.walk("."):
    for fileName in files:
        full_fileName = os.path.join(root,fileName)
        x,y = (os.path.splitext(fileName))
        i=i+1
        x = x+f"{i}"+y
        os.rename(fileName, x)
        
