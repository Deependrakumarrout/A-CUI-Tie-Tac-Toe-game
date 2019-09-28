
import subprocess
while True:
    subprocess.run(["python","Tic Tac Toe main.py"])
    print("\nDo you want to restart the game again? ")
    user_choice=""
    print("press Y [for yes]  OR   N [for no]:")
    while user_choice != "y".lower() and user_choice != "n".lower():
        user_choice = input("Enter the valid key:")
        if user_choice == 'y'.lower():
            print("\nprocessing...")
            print("\t[User Start Again]")
            continue

    if user_choice=="n".lower():
        print("\nPlayer don't want to restart again")
        break
