import csv


def DataStoring(records):
    
    ## Store Data
    ## Export list of lists to csv files
    ## Original data 
    with open('ori_position_1.csv', 'w', newline = '') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Assign attribute names
        wr.writerow(('player_name', 'position'))
        # Write in the position table
        wr.writerows(records[0])

    with open('ori_FGA.csv', 'w', newline = '') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Assign attribute names
        wr.writerow(('player_name', 'field_goal_attempt', 'games_played', 'minutes_played_per_game', 'year'))
        # Write in the FGA table
        wr.writerows(records[1])

    with open('ori_USG.csv', 'w', newline = '') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Assign attribute names
        wr.writerow(('player_name', 'usage_percentage', 'games_played', 'total_minutes_played', 'year'))
        # Write in the USG table
        wr.writerows(records[2])

    with open('ori_salary.csv', 'w', newline = '') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Assign attribute names
        wr.writerow(('player_name', 'salary', 'year'))
        # Write in the salary table
        wr.writerows(records[3])

    with open('ori_draft.csv', 'w', newline = '') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Assign attribute names
        wr.writerow(('pick_rank', 'player_name', 'year'))
        # Write in the draft table
        wr.writerows(records[4])

    with open('ori_EV.csv', 'w', newline = '') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        # Assign attribute names
        wr.writerow(('pick_rank', 'expected_value'))
        # Write in the expected value table
        wr.writerows(records[5])        