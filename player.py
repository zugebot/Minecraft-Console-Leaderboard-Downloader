# Jerrin Shirks

# native imports
import binascii

# custom imports
from support import *
from ps3_enum import PS3
from ps4_enum import PS4


class Player:
    def __init__(self, data):
        """
        This is what each player in the leaderboard has in terms of values:
        "@serial,jid,rank,max-rank,score,name,data,date"
        """
        for i in data:
            j = i.replace("@", "")
            setattr(self, j, data[i])
        
        
    def getDetails(self, console):
        if console == PS3.title:
            return [
                self.serial,
                self.jid,
                self.rank,
                self.max_rank,
                self.score,
                self.name,
                self.data,
                self.date
                    ]
        elif console == PS4.title:
            return [
                self.serial,
                self.account,
                self.data,
                self.date,
                self.jid,
                # self.max_rank,
                str(binascii.hexlify(self.message.encode('utf-8')))[2:-1],
                self.name,
                self.rank,
                self.score,
                   ]

    def getGlideTime(self) -> str:
        """
        converts the integer glide time to a formatted time string.
        :return: a string formatted like this: "X:XX.XXX"
        :rtype: str
        """
        second = int(self.score[:-3])
        time_str: str = f"{second // 60}:{second % 60}.{self.score[-3:]}"
        return time_str

