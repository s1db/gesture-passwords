# import sys
# from os import system, name
# import os
# l = []

# def clear():
#     print(name)
#     # for windows
#     # if name == 'nt':
#     #     _ = system('cls')
#     # # for mac and linux(here, os.name is 'posix')
#     # else:
#     #     _ = system('clear')

# while True and os.system('cls' if os.name == 'nt' else 'clear') == 0:
#     x = sys.stdin.read(1)
#     print(x)
#     l.append(x)
#     if x == 'p':
#         break

# print(l)
import pwinput

p = []
while True:
    x = pwinput.pwinput(mask='', timeout=1)
    p.append(x)
    if x == 'p':
        break
# import curses, time
# l = []
# try:
#     while True: 
#         win = curses.initscr()
#         ch = win.getch()
#         l.append(ch)
#         if chr(ch) == "p":
#             break
#         curses.endwin()
#         # time.sleep(0.05)
# finally:
#     # curses.endwin()
#     l.append(ch)
#     print(l)

# c = input_char('Do you want to continue? y/[n]')
# if c.lower() in ['y', 'yes']:
#     print('yes')
# else:
#     print('no (got {})'.format(c))
