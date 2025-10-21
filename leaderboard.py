# zugebot

# native imports
import time
import json
import requests
import xmltodict
import itertools
from enum import Enum
from threading import Thread

# custom import
from support import *
from player import Player


class Leaderboard:
    def __init__(self, 
                 console: str | Enum = None,
                 board: int = 100, 
                 start: int = 1, 
                 list_max: int = 2) -> None:

        if isinstance(console, Enum):
            console: str = console.value

        self.console = console.lower().strip()
        self.board_id = board
        self.start = start
        self.list_max = list_max

        # THIS IS WHERE IT UPDATES IT'S ATTRIBUTES
        console_obj = consoleDict[self.console]

        self.platform = console_obj['platform']
        self.sv = console_obj['sv']
        self.title_id = console_obj['titleid']
                     
        self.title = console_obj["boards"][board]["title"]
        self.filename = console_obj["boards"][board]["filename"]

                     
        self.link = console_obj['link']
        self.xml = console_obj["xml"].format(self.platform,
                                             self.sv,
                                             self.title_id,
                                             self.board_id,
                                             self.start,
                                             self.list_max)

        # THIS IS WHERE IT LOADS THE DETAILS FROM THE SERVERS
        self.raw = requests.post(self.link, data=self.xml).text
        self.leaderboard = xmltodict.parse(self.raw)
        
        # If it is successful
        ranking = self.leaderboard['ranking']
        self.valid = (ranking['@result'] == '00')
        if self.valid:
            self.player_list = ranking['list']['record']
            self.total = ranking['total']
            self.update = ranking['update']
            self.players = [Player(p) for p in self.player_list]


    def getChunkList(self, count: int = 256) -> list:
        _max = int(self.total)
        return [[int(i/count), i, [_max - i, count][i + count < _max]] for i in range(1, _max, 256)]


    @staticmethod
    def download_all(board_enum: Enum) -> None:
        print("Just letting you know, this will take a while. A long while if this is PS4...")
        time.sleep(3)
        for entry in board_enum:
            Leaderboard.download(entry)

    @staticmethod
    def download(board_enum: Enum) -> None:
        """
        This runs hundreds of threads, where each thread retrieves 256 entries from the PSN servers.
        Every 100 threads, it waits 5 seconds for prior threads to catch up.
        After all threads are finished, it conjoins all the data into a dictionary and saves it to it's
        designated folder.
        :param board_enum: the enum that holds the console title + category to download.
        :type board_enum: Enum
        """

        def threaded_board_segment(_chunks, _board, _sect):
            print(f"Thread {_sect[0]}: starting args=(chunks, {_board}, {_sect})")
            tmp = Leaderboard(console="ps4", board=_board, start=_sect[1], list_max=_sect[2])
            _chunks[_sect[0]] = tmp.player_list
            print(f"Thread {_sect[0]}: ending")


        # extracts values from enum
        console_title: str = board_enum.title.value
        board_id: int = board_enum.value

        console_leaderboard = Leaderboard(console=console_title, board=board_id)

        print(f"Loading board with title '{console_leaderboard.title}'")
        print(f"Board size: {console_leaderboard.total}")

        threads = []
        sections = console_leaderboard.getChunkList()
        chunks = [{}] * (len(sections) + 1)

        for n, sect in enumerate(sections):
            thread = Thread(target=threaded_board_segment, args=(chunks, console_leaderboard.board_id, sect,))
            threads.append(thread)
            thread.start()

            if n % 100 == 0:
                print("Letting threads catch up...")
                time.sleep(5)

        for thread in threads:
            thread.join()

        print("\nDone fetching results...\n")

        data = {
            'ranking': {
                'list': {
                    '@number': str(console_leaderboard.total),
                    'record': list(itertools.chain(*chunks))
                },
                'total': str(console_leaderboard.total),
                'update': console_leaderboard.update
            }
        }

        with open(f"data/{console_leaderboard.filename}", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Saved to data/{console_leaderboard.filename}")


    def printPlayerXml(self) -> None:
        """
        This prints all the players as xml.
        """
        if not self.valid:
            return print("This Leaderboard object is not valid. Cannot print player xml.")
        printXml(self.player_list)


    def printLeaderboardXml(self) -> None:
        """
        This prints the leaderboard as xml.
        """
        printXml(self.leaderboard)

