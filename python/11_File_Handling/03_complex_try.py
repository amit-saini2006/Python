def sereve_chia(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unkown":
            raise ValueError("we dont know the flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is sereved")
    finally:
        print("next customer please")

# sereve_chia("masala")
sereve_chia("unkown")