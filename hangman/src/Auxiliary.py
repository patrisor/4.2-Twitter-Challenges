# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Auxiliary.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 21:44:59 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 21:45:27 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import Getch

# Function Listens for key inputs
# Returns a string that was inputted
def get(prompt):
    print(prompt)
    inkey = Getch._Getch()
    while(1):
        k=inkey()
        if k!='':break
    return k

# Quits our game if input is 'q'
def quit(i):
    if i == "~":
        print("Goodbye!")
        exit(-1)
    return i

# Function processes Input and checks if it is valid
# Returns string inputted if valid
def processInput():
    while True:
        ret = quit(get("Guess a Character\n"))
        if not ret.isalpha():
            print("Invalid Input")
            continue
        return(ret)
