seat_type =input("Enter seat type (sleeper/AC/general?luxury): ").lower()

match seat_type:
    case "sleeper":
        print("sleeper - no AC")
    case "ac":
        print("AC")
    case "general":
        print("general")
    case "luxary":
        print("luxary")
    case _:
        print("invalid")