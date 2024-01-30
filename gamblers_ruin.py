# in the name of ALLAH

"""
this file inclued function or variable for simulation this game
"""

# import library that we need

from random_number_generator import integer_uniform_distribution
from random_number_generator import linear_congruential_generator

# set variable we need to simulation

number_of_player = 20
start_money = 25 #$

# create player number list with function that exist in random_number_generator

player_number_list = integer_uniform_distribution(number_of_player, 1)

# create 2D list to set money for each player

player_money_dict = {}

for player_number in player_number_list:
    player_money_dict[player_number] = start_money 


# now we need some function for doing some repetitive tasks

# this function check player and money of each player and then if money of some player is zero, function remove 
# ... this player and retrurn new player number and new player_money information to continue game
def remove_looser(main_dict, player_number_list):
    for player_number in player_number_list:
        if main_dict[player_number] == 0:
            player_number_list.remove(player_number)
            del main_dict[player_number]
    return main_dict, player_number_list

# this function get number of player that he/she should play in this round and generate random number between player number
# ... and give 1 $ to random player and return last seed to new seed

def game_round(player_round, seed):
    
    random_number, seed = linear_congruential_generator(player_number_list, 1, 2, seed)
    # if random_number == player_round:
    #     random_number, seed = linear_congruential_generator(player_number_list, 1, 2, (seed + 1) % len(player_number_list))
    player_money_dict[player_round] -= 1
    player_money_dict[random_number] += 1
    
    return seed % len(player_number_list)


# simulation gamblers_ruin
seed = 1

for _ in range(20):
    for player_number in player_number_list:
        seed = game_round(player_number,seed)
        player_money_dict, player_number_list = remove_looser(player_money_dict, player_number_list)
    # print(player_number_list)
print(player_money_dict, sum(player_money_dict.values()))
    
