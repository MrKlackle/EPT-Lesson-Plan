# Mini Lesson WRITE - Read and wirte CSV file
#
# NOTES: 
# 1) Files are stored in a folder called data. Depending on file system you may need to change
#    the slashes so python can find the files.  
# 2) It's reccomded that you use this file for a reference and build the file durning the demo. 
#

var_file_to_write = open('data/my_new_file.txt', 'w')

# writing simple text string to the file making sure we can create and write to a file 
var_file_to_write.write('This is a string that will be written to a file. We will create a complex string in CSV format later!')

# closing file after data is written to it
var_file_to_write.close()