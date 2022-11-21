import sys
from Test import *

numArgs = len(sys.argv)
i = 0
uso = "python main.py (-pdf|-txt|-dir) (source_file|source_directory) [-d saveFile] \n"


if numArgs < 3:
    print(uso)
    exit()

sourceFile = sys.argv[2]

match sys.argv[1]:
    case "-pdf" :
        sourceType = "pdf"
    case "-txt" :
        sourceType = "txt"
    case "-dir" :
        sourceType = "dir"
    case _ :
        print(uso)
        exit()

if numArgs >= 5:
    if sys.argv[3] != "-d":
        print(uso)
        exit()
    else :
        saveFile = sys.argv [4]



