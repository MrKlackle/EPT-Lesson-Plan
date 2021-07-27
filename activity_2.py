# Activity 2 - Guided Practice
#
# NOTES: 
# 1) Files are stored in a folder called data. Depending on file system you may need to change
#    the slashes so python can find the files.  
# 2) It's reccomded that you use this file for a reference and build the file durning the demo.
# 3) Focus on steps 1-2 then move on to step 3-4. 
#


####################################
# STEP 1 - opening file
####################################
filename = 'data/nba_teams_2013.csv'

# open file and save to a variable 
var_file = open(filename, 'r')


####################################
# STEP 2A - reading file
####################################
# prints the file object not the contents 
#print(var_file)
# prints the file like using a methord
#print(var_file.readline())


####################################
# STEP 2B - reading file
####################################
# loop to print out every line in the file
#for item in var_file:
  #print(item)


####################################
# STEP 2C - reading file
####################################
# same loop as above but we create a list by using the .split() methord on the string
# then we print the first item in the list
#for item in var_file:
    #item = item.split(',')
    #print(item[0])


####################################
# STEP 2D - reading file
####################################
# create a variable to save the data
var_to_save_data_to_print = []
# same for loop as in step 2C expect we're adding data to a list instead of printing
for item in var_file:
    item = item.split(',')
    var_to_save_data_to_print.append(item[0])

# after the loop we print the list to confirm we have the data we want in a list
print(var_to_save_data_to_print)
# end of step 2D


# done reading file so we close it
var_file.close()




####################################
# STEP 3 - writing file
####################################
# new filename and location
new_filename = 'data/nba_team_names.csv'
# opening the file object and assigning a variable name
var_file_to_write = open(new_filename, 'w')


####################################
# STEP 4A - write a string to file
####################################
# writing simple text string to the file making sure we can create and write to a file 
#var_file_to_write.write('This will be a file of all the NBA teams in a minute')


####################################
# STEP 4A - write a string to file
####################################
# creating the string we want to add to the file
# looping through each element in the list and adding the string and a comma to create a CSV file
for item in var_to_save_data_to_print:
    var_file_to_write.write(item + ',')

# closing file after data is written to it
var_file_to_write.close()
