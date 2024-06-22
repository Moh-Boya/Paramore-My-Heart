import sys
import time
from time import sleep

def print_lirik(): #function
    baris = [
        ("Stay with me", 0.1),
        ("This is what I need please", 0.2),
        ("Sing us a song", 0.2),
        ("And we'll sing it back to you", 0.2),
        ("We could sing our own", 0.1),
        ("But what would it be without you", 0.1),
        ("I am nothing now", 0.1),
        ("And its been so long", 0.2),
        ("Since I've heard a sound", 0.1),
        ("The sound of my only hope", 0.1),
        ("This time I will be listening", 0.3),
    ]

    jeda = [1.5, 2.2, 0.8, 1.2, 1.2, 4.2, 2.2, 2.9, 1.5, 4.0, 2.0]  #array jeda baris

    for i, (line, char_jeda) in enumerate(baris): #loop bwt output
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda) #var buat 
        print('')
        sleep(jeda[i])  #make array jeda baris (idk why this line has traceback)

print_lirik() #manggil function
