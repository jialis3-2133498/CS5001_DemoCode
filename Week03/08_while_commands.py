def main():
    command = None 
    while(command != 'stop'):
        command = in_lower("What do you want me to do?")
        print(f"Okay, I'll{command}")
    print("Whew! Good to be done!") 

def in_lower(
        user_prompt : str):
    return input(user_prompt).lower()

main()