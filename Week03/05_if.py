# if (True):
#     print("Of course!")

# if (False):
#     print("Of course!") # It will not do anything because False boolean. If only accept true things 

# if (5 + 6 == 12):
#     print("Yes, it is ture")
# else:
#     print("No, it is not true") # Else only accepts things that are false in If

suit = input("Input a card suit: ").lower()
rank = input("Input a card rank: ").lower()
if (suit == "diamond" or suit == "heart"):
    color = "red"
else:
    color = "black"


if (rank == "king" or rank == "queen" or rank == "jack"):
    is_face_card = True
else:
    is_face_card = False

if (color == "red"):
    if is_face_card: # A nested if-statement
        print("You chose a red face card")
    else:
        print("You chose a red pip card")
else:
    if is_face_card:
        print("You chose a black face card")
    else:
        print("You chose a black pip card")

