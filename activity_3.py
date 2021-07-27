# Activity 3 - Data Processing
#
# NOTES: 
# 1) Files are stored in a folder called data. Depending on file system you may need to change
#    the slashes so python can find the files.  
# 2) It's reccomded that you use this file for a reference and build the file durning the demo. 
#

# this will be a list of list (array) of the file 

def read_file(player):
    # returns file_array with data from file where the player is found
    player_array = []
    filename = 'data/NBA_Shot_Locations_1997-2020.csv'

    # open file and save to a variable reader then process that line before moving on in the file
    with open(filename, 'r') as reader:
        for line in reader:
            line = line.split(',')
            # only adding line to file if the player is in the line and they took a jump shot
            if player in line and 'Jump Shot' in line:
                # just pulling out the data we need [name, shot type, 2 or 3 points]
                player_array.append([line[3], line[9], line[10]])
    
    # done reading file so we close it
    reader.close()
    

    return player_array

def write_file(better_player, player_1, player_2):
    filename = 'data/best_player.csv'
    write_to_file = open(filename, 'w')
    
    # loading our list to be exported
    data_to_print = []

    # adding better player 
    data_to_print.append([better_player])
    data_to_print.append(list(player_1.keys()))
    data_to_print.append(list(player_1.values()))
    data_to_print.append(list(player_2.values()))

    # looping through each element in the list and adding the string and a comma to create a CSV file
    for item in data_to_print:
        for i in item:
            write_to_file.write(str(i) + ',')
        write_to_file.write('\n')

    # closing file after data is written to it
    write_to_file.close()


def process_data(player):
    # returns a dictionary 
    two_points = 0
    three_points = 0
    three_precentage = 0.00
    total_points = 0

    # read file and get everything where the player is listed
    list_of_player_data = read_file(player)
    
    for item in list_of_player_data:
        if  '2PT Field Goal' in item:
            two_points += 1
        elif '3PT Field Goal' in item:
            three_points +=1
    
    three_precentage = three_points / (two_points + three_points)
    total_points = (two_points * 2) + (three_points * 3)

    return { 
            'name' : player, 
            '2 points' : two_points,
            '3 points' : three_points,
            '3 point precentage' : three_precentage,
            'total points' : total_points }

def best_player(player_1, player_2):
    winner = ''
    score = 0

    if player_1['2 points'] > player_2['2 points']:
        score += 1
    if player_1['3 points'] > player_2['3 points']:
        score += 1
    if player_1['3 point precentage'] > player_2['3 point precentage']:
        score += 1
    if player_1['total points'] > player_2['total points']:
        score += 1

    if score < 2:
        winner = winner + f'{player_2["name"]} is the clear winner!' 
    elif score > 2: 
        winner = winner + f'{player_1["name"]} is the clear winner!'
    elif score == 2:
        winner = 'There is no clear winner. These players are evenly matched'
        if player_1['total points'] > player_2['total points']:
            winner = winner + f'\n{player_1["name"]} has scored more total points!'
        else: 
            winner = winner + f'\n{player_2["name"]} has scored more total points!'
    return winner


def main():
    person_1 = 'Kobe Bryant' 
    person_2 = 'Kevin Durant' 
    # 'LeBron James'
    # 'Michael Jordan'
    # 'Stephen Curry'
    # 'Dell Curry'

    # person 1 (number of two pointers, number of 3 pointers, precentage of 3 pointers, total points)
    person_1_data = process_data(person_1)
    #print(person_1_data)

    # person 2 (number of two pointers, number of 3 pointers, precentage of 3 pointers, total points)
    person_2_data = process_data(person_2)
    #print(person_2_data)

    # compair two (precentage of 3 pointers, total points)
    winner = best_player(person_1_data, person_2_data)
    #print(winner)

    # export findings to new CSV file
    write_file(winner, person_1_data, person_2_data)

    print('success')

if __name__ == "__main__":
   main()