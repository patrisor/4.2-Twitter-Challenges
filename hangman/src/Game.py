# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 21:43:53 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 22:18:55 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math, random, Auxiliary

# Function parses my list of words randomly
# (Thank you to the owner of https://github.com/dwyl/english-words.git for providing this giant list)
def parseFile(file_name):
    try: return [line.rstrip('\n') for line in open(file_name)]
    except IOError:
        print("File not Found")
        return []

# Counts the total amount of contents and divides by three to distribute easy, medium, and hard words
# Also Removes words too easy
def splitListEvenly(sorted_list):
    for w in range(len(sorted_list)):
        if len(sorted_list[w]) == 3: anchor = w
    sorted_list = sorted_list[anchor:]
    x = int(len(sorted_list) / 3)
    return [sorted_list[x * i : x * i + x] for i in range(0, math.ceil(len(sorted_list) / x))]

# Updates our game state
def update_game(w, i, g, hit = 0):
    for c in range(len(w)):
        if w[c] == i:
            g[c * 2] = i
            hit += 1
    return hit

# Function initializes our current game word from list of words based on list passed as parameter
# First the list is split evenly into difficulty, then word is randomly selected from that list
# RETURNS the word and difficulty level as list
def initWord(game_list):
    while True:
        hit = 0
        inp = Auxiliary.quit(input("Choose your difficulty:\n[EASY] [MEDIUM] [HARD]\n").lower())
        if inp == "easy" or inp == "medium" or inp == "hard":
            if inp == "medium" or inp == "hard": hit = (1 if inp == "medium" else 2)
            break
        print("Invalid Input")
        continue
    split_list = splitListEvenly(sorted(game_list, key=len))[hit]
    return [split_list[random.randint(0, len(split_list) - 1)], hit]

# Function generates game state from word passed as parameter
def initGame(game_word, ret = ''):
    for i in range(len(game_word)): ret += '_ '
    return list(ret)
