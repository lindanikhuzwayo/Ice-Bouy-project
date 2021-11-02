import sys
import difflib
import fileinput

compare_files_error = 0



def file_len(file_name):
  with open(file_name) as f:
    for i, l in enumerate(f):
      pass
  return i+1
 
gldn=open(sys.argv[1],"r")
rcvd=open(sys.argv[2],"r")
 
depth_glden=file_len(sys.argv[1])
depth_rcvd=file_len(sys.argv[2])
print("depth of gldn.txt --> %s" %depth_glden)
print("depth of rcvd.txt --> %s" %depth_rcvd)

if(depth_rcvd > depth_glden):
  compare_files_error=1
  print('FAIL :: depth(received.txt) file is more than depth(golden.txt)')

for line2 in range (0,depth_rcvd,1):
  rcvd_line=rcvd.readline()
  glden_line=gldn.readline()
  if glden_line!=rcvd_line:
    compare_files_error=1
    break

if(compare_files_error == 0):
  print('COMPARISION SUCCESSFUL --> compare_files.py::compare_files_error = %s'%compare_files_error)
else:
  print('COMPARISON FAILED --> compare_files.py::compare_files_error = %s'%compare_files_error)

#sys.exit(compare_files_error)

gldn.close()
rcvd.close()

#Add the sys.exit() as per the requirement