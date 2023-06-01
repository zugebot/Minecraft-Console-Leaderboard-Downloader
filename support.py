# Jerrin Shirks

# native imports
import pprint


def printXml(data: dict, indent=1) -> None:
    pprint.pprint(data, indent=indent)


consoleDict = {
    'xbox1': {
        'link': '',
        'xml': '',
        'platform': '',
        'sv': '',
        'titleid': '',
        'boards': {
            1: {'filename': 'None', 'title': 'None'},
        }
    },
    'psv': {
        'link': '',
        'xml': '',
        'platform': 'psp2',
        'sv': '3.74',
        'titleid': 'NPWR06859_00',
        'boards': {
            1: {'filename': 'None', 'title': 'None'},
        }
    },
    'ps3': {'link': 'http://ranking-view-l01.u0.np.community.playstation.net/ranking_view/func/get_ranking',
            'xml': '<?xml version="1.0" encoding="utf-8"?><ranking platform="{}" sv="{}"><titleid>{}</titleid><board>{}</board><start>{}</start><list-max>{}</list-max><option message="false" info="false"/></ranking>',
            'platform': 'ps3',
            'sv': '4.89',
            'titleid': 'NPWR05636_00',
            'boards': {
                1: {'filename': 'ps3/regular/travelling_peaceful', 'title': 'Travelling Peaceful'},
                2: {'filename': 'ps3/regular/travelling_easy', 'title': 'Travelling Easy'},
                3: {'filename': 'ps3/regular/travelling_medium', 'title': 'Travelling Medium'},
                4: {'filename': 'ps3/regular/travelling_hard', 'title': 'Travelling Hard'},
                5: {'filename': 'ps3/regular/mining_peaceful', 'title': 'Mining Blocks Peaceful'},
                6: {'filename': 'ps3/regular/mining_easy', 'title': 'Mining Blocks Easy'},
                7: {'filename': 'ps3/regular/mining_medium', 'title': 'Mining Blocks Medium'},
                8: {'filename': 'ps3/regular/mining_hard', 'title': 'Mining Blocks Hard'},
                9: {'filename': 'ps3/regular/farming_peaceful', 'title': 'Farming Peaceful'},
                10: {'filename': 'ps3/regular/farming_easy', 'title': 'Farming Easy'},
                11: {'filename': 'ps3/regular/farming_medium', 'title': 'Farming Medium'},
                12: {'filename': 'ps3/regular/farming_hard', 'title': 'Farming Hard'},
                13: {'filename': 'ps3/regular/kills_easy', 'title': 'Kills Easy'},
                14: {'filename': 'ps3/regular/kills_medium', 'title': 'Kills Medium'},
                15: {'filename': 'ps3/regular/kills_hard', 'title': 'Kills Hard'},
            }
            },
    'ps4': {'link': 'http://ranking-view-k01.u0.np.community.playstation.net/ranking_view/func/get_ranking',
            'xml': '<?xml version="1.0" encoding="utf-8"?><ranking platform="{}" sv="{}"><titleid>{}</titleid><board>{}</board><start>{}</start><list-max>{}</list-max><option message="true" info="false" account="true"/></ranking>',
            'platform': 'ps4',
            'sv': '9.60',
            'titleid': 'NPWR05706_00',
            'boards': {
                1: {'filename': 'ps4/regular/travelling_peaceful', 'title': 'Traveling Peaceful'},
                2: {'filename': 'ps4/regular/travelling_easy', 'title': 'Traveling Easy'},
                3: {'filename': 'ps4/regular/travelling_medium', 'title': 'Traveling Normal'},
                4: {'filename': 'ps4/regular/travelling_hard', 'title': 'Traveling Hard'},
                5: {'filename': 'ps4/regular/mining_peaceful', 'title': 'Mining Blocks Peaceful'},
                6: {'filename': 'ps4/regular/mining_easy', 'title': 'Mining Blocks Easy'},
                7: {'filename': 'ps4/regular/mining_medium', 'title': 'Mining Blocks Normal'},
                8: {'filename': 'ps4/regular/mining_hard', 'title': 'Mining Blocks Hard'},
                9: {'filename': 'ps4/regular/farming_peaceful', 'title': 'Farming Peaceful'},
                10: {'filename': 'ps4/regular/farming_easy', 'title': 'Farming Easy'},
                11: {'filename': 'ps4/regular/farming_medium', 'title': 'Farming Normal'},
                12: {'filename': 'ps4/regular/farming_hard', 'title': 'Farming Hard'},
                13: {'filename': 'ps4/regular/kills_easy', 'title': 'Kills Easy'},
                14: {'filename': 'ps4/regular/kills_medium', 'title': 'Kills Normal'},
                15: {'filename': 'ps4/regular/kills_hard', 'title': 'Kills Hard'},

                100: {'filename': 'ps4/score_attack/cavern', 'title': 'Glide Score Attack : Cavern'},
                101: {'filename': 'ps4/score_attack/kraken', 'title': 'Glide Score Attack : Kraken'},
                102: {'filename': 'ps4/score_attack/yeti', 'title': 'Glide Score Attack : Yeti'},
                103: {'filename': 'ps4/score_attack/dragon', 'title': 'Glide Score Attack : Dragon'},
                104: {'filename': 'ps4/score_attack/temple', 'title': 'Glide Score Attack : Temple'},
                105: {'filename': 'ps4/score_attack/shrunk', 'title': 'Glide Score Attack : Shrunk'},
                106: {'filename': 'ps4/score_attack/mobs', 'title': 'Glide Score Attack : Mobs'},
                107: {'filename': 'ps4/score_attack/body', 'title': 'Glide Score Attack : Body'},
                108: {'filename': 'ps4/score_attack/canyon', 'title': 'Glide Score Attack : Canyon'},
                109: {'filename': 'ps4/score_attack/excalibur', 'title': 'Glide Score Attack : Excalibur'},
                110: {'filename': 'ps4/score_attack/icarus', 'title': 'Glide Score Attack : Icarus'},
                111: {'filename': 'ps4/score_attack/celts', 'title': 'Glide Score Attack : Celts'},

                200: {'filename': 'ps4/time_attack/cavern', 'title': 'Glide Time Attack : Cavern'},
                201: {'filename': 'ps4/time_attack/kraken', 'title': 'Glide Time Attack : Kraken'},
                202: {'filename': 'ps4/time_attack/yeti', 'title': 'Glide Time Attack : Yeti'},
                203: {'filename': 'ps4/time_attack/dragon', 'title': 'Glide Time Attack : Dragon'},
                204: {'filename': 'ps4/time_attack/temple', 'title': 'Glide Time Attack : Temple'},
                205: {'filename': 'ps4/time_attack/shrunk', 'title': 'Glide Time Attack : Shrunk'},
                206: {'filename': 'ps4/time_attack/mobs', 'title': 'Glide Time Attack : Mobs'},
                207: {'filename': 'ps4/time_attack/body', 'title': 'Glide Time Attack : Body'},
                208: {'filename': 'ps4/time_attack/canyon', 'title': 'Glide Time Attack : Canyon'},
                209: {'filename': 'ps4/time_attack/excalibur', 'title': 'Glide Time Attack : Excalibur'},
                210: {'filename': 'ps4/time_attack/icarus', 'title': 'Glide Time Attack : Icarus'},
                211: {'filename': 'ps4/time_attack/celts', 'title': 'Glide Time Attack : Celts'},
            }
            }
}
