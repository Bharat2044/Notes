#MatchCaseEX3.py
wkn=input("Enter the Week Name:").upper()
match(wkn):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is Working Day".format(wkn))
    case "SATURDAY":
        print("{} is Week-End".format(wkn))
    case "SUNDAY":
        print("{} is HOLIDAY Day".format(wkn))
    case _:
        print("{} is not week day".format(wkn))

