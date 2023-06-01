# Jerrin Shirks

# native imports
from threading import Thread
import itertools
import json
import os
import time


# custom imports
from leaderboard import Leaderboard
from ps3_enum import PS3
from ps4_enum import PS4



def ensure_directories_exist(directory: str = "data"):
    """
    Ensures all data directories exist for storing leaderboards
    """
    directories = [
        f'{directory}/ps3/regular/',
        f'{directory}/ps4/regular/',
        f'{directory}/ps4/score_attack/',
        f'{directory}/ps4/time_attack/'
    ]
    for i_directory in directories:
        if not os.path.exists(i_directory):
            os.makedirs(i_directory)


if __name__ == "__main__":
    ensure_directories_exist()
    """
    # different ways to run it:
    
    # 1 [downloads a single board]
    Leaderboard.download(PS4.farming_easy)
    
    # 2 [downloads all ps3 boards (will take a while!) (also idk if this one will work lol)]
    for entry in PS3:
        Leaderboard.download(entry)
        
    glide leaderboards have at max 10,000 data entries, 
    while regular leaderboards for kills, mining, farming, and travelling have 1,000,000
    """
    Leaderboard.download(PS4.score_body)
