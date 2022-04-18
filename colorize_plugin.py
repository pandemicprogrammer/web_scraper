#Script to set console output to purple
#Marie Valentonis 4.18.2022

# Import Colorama
from colorama import init, Fore, Back, Style

# Initializes Colorama, autoreset=True for terminal color reset
init(autoreset=False)

#Set color              \ESCAPEcode[FG/BGcode;CONSTANT;STOPPER]
print('\033[38;5;93m')

#Add auto reset point        print('\033[38;5;93[0;0m') 
