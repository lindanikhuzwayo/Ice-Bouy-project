import os
import sys
#from csv_diff import load_csv, compare

file_size = os.path.getsize(sys.argv[2])
print("Decompressed file, " + sys.argv[2] + ", is :", file_size, "bytes")

#2018-09-19-03_57_11_VN100.csv

file_size2 = os.path.getsize(sys.argv[1])
print("Main file, " + sys.argv[1] + ", is :", file_size2, "bytes")



#from csv_diff import load_csv, compare
#diff = compare(
 #   load_csv(open("data.csv"), key="computer"),
  #  load_csv(open("final.csv"), key="computer")
#)

#compression_ratio = (file_size2 - file_size)/ file_size2

#print("Compression ratio is %", compression_ratio * 100)
#print('Compressed: %d%%' % (100.0 * compression_ratio))

#if(file_size2 > file_size):
 #   print("Yessirski compress")


#file_size3 = os.path.getsize('./g8.csv')
#print("File Size is :", file_size3, "bytes")


#if(file_size3 == file_size):
 #  print("Yessirski lossless compression")
#elif(file_size3 < file_size2):
 #  print("Lossy compression.Smaller by {} bytes".format(file_size2 - file_size3))
