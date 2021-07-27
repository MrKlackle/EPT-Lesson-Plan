# Mini Lesson READ - Read and wirte CSV file
#
# NOTES: 
# 1) Files are stored in a folder called data. Depending on file system you may need to change
#    the slashes so python can find the files.  
# 2) It's reccomded that you use this file for a reference and build the file durning the demo. 
#

# open file and save to a variable 
var_file = open('data/nba_teams_2013.csv', 'r')

# prints the file object not the contents 
print('file object:', var_file)
# prints the file like using a methord
print('readline:', var_file.readline())
# prints the file like using a methord
print('readlines:', var_file.readlines())

var_file.close()
