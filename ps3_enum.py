# Jerrin Shirks

# native imports
from enum import Enum


class PS3(Enum):
    """
    This class represents the integer id's that the PSN leaderboard associates with each category for PS3.

    regular boards go 1 to 15.

    *Note that ps3 does not have in-game leaderboards for glide.
    """
    title: str = "ps3"
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
