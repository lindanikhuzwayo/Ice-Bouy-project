import os
import sys
 
file_size = os.path.getsize(sys.argv[2])
print("File size of " + sys.argv[2] + " is :", file_size, "bytes")

file_size2 = os.path.getsize(sys.argv[1])
print("File size of " + sys.argv[1] + " is :", file_size2, "bytes")



