import random
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
def play_round(playerName:str = 'Steven'):
    choice_input = input("Will you 'remain silent' or 'betray'? >>> ")
    player_result = prisoner_choice(playerName, choice_input)
    ai_result = prisoner_choice('ai', ai_choice())
    return player_result, ai_result

 #################################################################
def ai_choice():
    option_list = [0, 1]
    ai_choice = random.choice(option_list)
    if ai_choice == 0:
        choice = 'remain silent'
    if ai_choice == 1:
        choice = 'betray'

    return choice
    
#################################################################

print(play_round())
