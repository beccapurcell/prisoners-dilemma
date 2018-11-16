
# choices = ['betray', 'remain silent']
# consequences = [0, -1, -2, -3]
# prisoners = ['Prisoner1', 'Prisoner2']

#################################################################
def prisoner_choice(prisoner: str, choice: str):
    result_string = '%s has chosen to %s.' % (prisoner, choice)
    return result_string

#################################################################
def create_player():
    player_name = input("What is your name, prisoner? >>> ")
    return player_name

#################################################################
def play(playerName:str):
    choice = input("Will you 'remain silent' or 'betray'? >>> ")
    result = prisoner_choice(playerName, choice)
    return result

#################################################################

print(play(create_player()))
