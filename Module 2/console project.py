import random

#Rock, paper, scissors, well
# cocepts used: random choice (import), tuple/list, loops
# the player and the computer each choose rock, paper, scrissors, or well
# use tuple or list to store the options 
                                    #колодязь
options = ('rock','paper','scissors','well')

#computer_options = random.choice(options)

                         #before the game
choices_outside_game = {
'Press 1 to start the new game':'1',
'Press 2 to exit the game':'2'} #1-2: when cycle/game is finished

computer_move = 'computer'
player_move = 'player'


winner = 'winner'
# function set one match, and return winners 
def game_match():
    computer_move = random.choice(options)#get one: rock','paper','scissors','well'
    player_move = input('Choose paper, rock, scissors, or well: ').lower() # привели до нижнього регістру 
    
    if computer_move == player_move:
        winner = 'no-one'
        print('TIE' '\n no-one gets a point')
    elif computer_move == 'scissors' and player_move == 'paper': 
        winner = 'computer'
    elif computer_move == 'rock' and player_move == 'scissors': 
        winner = 'computer'
    elif computer_move == 'paper' and player_move == 'rock':
        winner = 'computer'
    elif computer_move == 'well' and player_move in  ('scissors', 'rock'):
        winner = 'computer'
    else:
        winner = 'player'
    return winner
comp_score = 0
player_score = 0

def game():
    global comp_score , player_score

    winner = game_match()
    if 'computer' == winner:
        comp_score += 1 
    elif "player" == winner:
        # player_score =+ 1 там дивись в чому моменти були 1) синтаксис зайві відступи та послідовність =+
        # ⚝⚝⚝⚝⚝ так, відпочивай) ти добре попрацювала!
        player_score += 1 
    
    print(f'{comp_score}:{player_score}')

def paper_rock_scissors_well():# 
    
    
    for key in choices_outside_game:# " 
        print(key)
    
    user_answer = input('Enter your number: ') 
    exit_command = "2"
    
    while user_answer !=  exit_command:# 
        if user_answer == '1':
            game()
            
            for key in choices_outside_game: 
                print(key)
            user_answer = input('Enter your number: ')
        elif user_answer == "2":
            print('You haven not started the game yet')
            continue
        else:
            print('ERROR \n Please choose the listed number: ')
 
        
paper_rock_scissors_well()
    