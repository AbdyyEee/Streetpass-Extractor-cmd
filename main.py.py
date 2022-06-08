from subprocess import Popen
from sys import exit
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# TODO: Not use tkinter??
# TODO: Perhaps add a way to auto restart
# TODO: Implement gui, with PyQt6.
# TODO: Fix input formatting below 

usr_input = input(
    '\n       ---------------------------------------------------\n       -*-*-Command Line CECD Extractor-*-*-                                    \n       ---------------------------------------------------           \n\nProgramming written by AbdyyEee. \nUtlizes 3ds-save-tool for extraction \nFor use with Cecil_FF4s StreetPass 2 Rise From the Ashes. \n \nSelect Y to continue with extraction, or N to end the process. '
)
options_agree = ('Y', 'y')
options_disagree = ('N', 'n')
if usr_input in options_agree:
    print('Select the 00000000 file...')
    file_path = filedialog.askopenfilename(title='Select the 0000000 File.')
    print('Select the output folder.')
    output_path = filedialog.askdirectory(title='Select the output directory.')
    cmd = f'Python disa-extract.py {file_path} {output_path}'
    output = Popen(cmd, shell=True)

elif usr_input in options_disagree:
    exit()

keep_alive = input('')
