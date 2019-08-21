# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 14:34:34 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 22:45:15 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, Auxiliary, Game

def die(reason):
    print(reason)
    return -1

def printArt():
    print("Welcome to\n                                                                            ")
    print("88                                                                                      ")
    print("88                                                                                      ")
    print("88                                                                                      ")
    print("88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba, ")
    print("88P'    '8a ''     `Y8 88P'   `'8a a8'    `Y88 88P'   '88'    '8a ''     `Y8 88P'   `'8a")
    print("88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88")
    print("88       88 88,    ,88 88       88 '8a,   ,d88 88      88      88 88,    ,88 88       88")
    print("88       88 `'8bbdP'Y8 88       88  `'YbbdP'Y8 88      88      88 `'8bbdP'Y8 88       88")
    print("                                    aa,    ,88                                          ")
    print("                                     'Y8bbdP'                                           ")

def HANGMANPICS(g):
    ret = ""
    if g == 0: ret += "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="
    if g == 1: ret += "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========="
    if g == 2: ret += "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n========="
    if g == 3: ret += "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========="
    if g == 4: ret += "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n========="
    if g == 5: ret += "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n========="
    if g == 6: ret += "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
    return ret

def engine(w):
    guesses = 0
    max_guesses = 7
    initialized = Game.initWord(w)
    game_word = initialized[0]
    difficulty = initialized[1]
    game = Game.initGame(game_word)
    while True:
        print(''.join(game))
        inp = Auxiliary.processInput()
        if Game.update_game(game_word, inp, game) == 0:
            print("Incorrect Guess\n" + HANGMANPICS(guesses))
            guesses += 1
        if ''.join(game).replace(" ", "") == game_word: 
            print("You guessed " + game_word + " correctly!")
            return [2, difficulty]
        if guesses == max_guesses:
            print("GAME OVER! You did not guess the word " + game_word)
            return [1, difficulty]
    return [0, 0]

if __name__ == "__main__":
    score = 0
    if len(sys.argv) != 2: Auxiliary.exit(die("usage: python3 main.py [word_file]"))
    words = Game.parseFile(sys.argv[1])
    print("PARSED FILE: " + str(len(words)) + " words\n")
    if(len(words) == 0): Auxiliary.exit(die("Try Again!"))
    printArt()
    while True:
        print("SCORE: " + str(score))
        ret = engine(words)
        if ret[0] > 1:
            if ret[1] == 0: score += 50
            if ret[1] == 1: score += 250
            if ret[1] == 2: score += 500
        inp = input("Play Again? (Y/N)").lower()
        if inp == 'y': continue
        else: 
            print("FINAL SCORE: " + str(score))
            break
