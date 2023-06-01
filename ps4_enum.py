# Jerrin Shirks

# native imports
from enum import Enum


class PS4(Enum):
    """
    This class represents the integer id's that the PSN leaderboard associates with each category for PS4.

    regular boards go 1 to 15.

    score attack for glide goes 100 to 111.

    time attack for glide goes 200 to 211.
    """
    title: str = "ps4"
    travelling_peaceful: int = 1
    travelling_easy: int = 2
    travelling_medium: int = 3
    travelling_hard: int = 4
    mining_peaceful: int = 5
    mining_easy: int = 6
    mining_medium: int = 7
    mining_hard: int = 8
    farming_peaceful: int = 9
    farming_easy: int = 10
    farming_medium: int = 11
    farming_hard: int = 12
    kills_easy: int = 13
    kills_medium: int = 14
    kills_hard: int = 15
    score_cavern: int = 100
    score_kraken: int = 101
    score_yeti: int = 102
    score_dragon: int = 103
    score_temple: int = 104
    score_shrunk: int = 105
    score_mobs: int = 106
    score_body: int = 107
    score_canyon: int = 108
    score_excalibur: int = 109
    score_icarus: int = 110
    score_celts: int = 111
    time_cavern: int = 200
    time_kraken: int = 201
    time_yeti: int = 202
    time_dragon: int = 203
    time_temple: int = 204
    time_shrunk: int = 205
    time_mobs: int = 206
    time_body: int = 207
    time_canyon: int = 208
    time_excalibur: int = 209
    time_icarus: int = 210
    time_celts: int = 211
