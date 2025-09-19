
# def main():
#     word_input = None
#     while ((word_input != 'yes') or (word_input != 'no')):
#         word_input = in_lower("You must answer yes or no: ")  
#     print("Thank you for your satisfactory answer")

# def in_lower(user_input):
#     return input(user_input).lower()
# main()



# def main():
#     answer = input("Please answer yes or no.")
#     while(not (answer == 'yes' or answer == 'no')):
#         answer = input("You must answer yes or no: ")
#     print("Thank you for your satisfactory answer")
# main()

def main():
    answer = input("Please answer yes or no: ")
    while(answer != 'yes' and answer != 'no'):
        answer = input("You must answer yes or no: ")
    print("Thank you for your satisfactory answer")
main()