# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Getch.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 14:38:05 by patrisor          #+#    #+#              #
#    Updated: 2019/08/20 14:38:50 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys,tty,termios

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
