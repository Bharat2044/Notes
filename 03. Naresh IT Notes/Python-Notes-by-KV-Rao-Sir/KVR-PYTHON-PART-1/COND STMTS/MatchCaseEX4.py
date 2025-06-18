#MatchCaseEX4.py
wkn=input("Enter the Week Name:").upper()
match(wkn[0:3]):
    case "MON"|"TUE"|"WED"|"THU"|"FRI":
        print("{} is Working Day".format(wkn))
    case "SAT":
        print("{} is Week-End".format(wkn))
    case "SUN":
        print("{} is HOLIDAY Day".format(wkn))
    case _:
        print("{} is not week day".format(wkn))

