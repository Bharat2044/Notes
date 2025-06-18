#MatchCaseEX2.py
wkn=input("Enter the Week Name:")
match(wkn):
    case "MONDAY":
        print("{} is Working Day".format(wkn))
    case "TUESDAY":
        print("{} is Working Day".format(wkn))
    case "WEDNESDAY":
        print("{} is Working Day".format(wkn))
    case "THURSDAY":
        print("{} is Working Day".format(wkn))
    case "FRIDAY":
        print("{} is Working Day".format(wkn))
    case "SATURDAY":
        print("{} is Week-End".format(wkn))
    case "SUNDAY":
        print("{} is HOLIDAY Day".format(wkn))
    case _:
        print("{} is not week day".format(wkn))

