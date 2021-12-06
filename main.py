from User import User
import time


print("Welcome to the investment game Uchi-Dushie! Start playing to become a Sensei Master!")

name = None
while not name:
    name = input("What is your name? ")

print(f"Welkom {name}! Good luke, playing the Investment Game!")
user = User(name)

while True:
    print("------------ MAIN MENU INVESTMENT GAME ------------ ")
    print("[Option 0] Show my portfolio")
    print("[Option 1] Buy stock")
    print("[Option 2] Sell stock")
    action = input(">>> Enter the number of action you would like to take: ")
    try:
        if int(action) == 0:
            print("Your portfolio currently contains the following stocks:")
            print(user.get_portfolio())
            wait = input("Press enter to continue to the main menu.")
        elif int(action) == 1:
            print('hi')
        elif int(action) == 2:
            print('hi')
    except ValueError:
        print("!!!!! You didn't enter a menu option number, you can try again in 3 seconds.")
        time.sleep(3)
