from shutil import copyfile

import sys
#g = "sjdsjdb.csv"
#print(g[:-4])
file_name = sys.argv[1]

copyfile("./" + file_name, "./"+file_name[:-4]+".txt")