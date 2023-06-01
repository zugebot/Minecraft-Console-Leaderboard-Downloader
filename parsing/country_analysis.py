# Jerrin Shirks

# native imports
from collections import Counter

# custom imports
from flags import FLAG_DICT


# This returns a dictionary of all flags for a leaderboard
# this can be rewritten, it is very old
if __name__ == "__main__":
    file = open("Glide_Time_Attack__Cavern.txt", "r")
    lines = file.readlines()
    countries = []
    for i in lines[1:]:
        # index = i.index("@")
        # fl = i[index+4:index+6]
        # score = i.split(" ")[3]
        fl = i.split(".")[1]
        countries.append(fl)

    countryCounter = Counter(countries)
    countries = []
    for i in countryCounter:
        countries.append([i, countryCounter[i]])
    countries.sort(key = lambda x: x[1])
    countries.reverse()

    for i in countries:
        try:
            fl = FLAG_DICT[i[0].upper()]
            percent = i[1] / len(countries)
            percent = str('{0:.2f}'.format(percent))
            percent = percent.zfill(5) + "%"
            print(fl, percent, i[1])
        except:
            ""
