import random

play_again=True
while play_again:

#user_choose=input('Enter a choice: Rock, Paper, Scissors')
    while True:
        user_choose=input('Enter a choice: Rock, Paper, Scissors\n')
        user_choose=user_choose.lower()
        possible_answers=["rock", "paper", "scissors"]
        if user_choose in possible_answers:
            break


    possible_actions= ["Rock", "Paper", "Scissors"]
    computer_action= random.choice(possible_actions)
    print("Computer chooses " + computer_action)
    if user_choose == computer_action:
        print('You have drawn!')
    elif user_choose=="Rock" and computer_action=="Paper":
        print('You lose, computer wins')
    elif user_choose=="Rock" and computer_action=="Scissors":
        print('You Win, computer Looses')
    elif user_choose=="Paper" and computer_action=="Rock":
        print('You Win, computer Looses')
    elif user_choose=="Paper" and computer_action=="Scissors":
        print('You lose, computer wins')
    elif user_choose=="Scissors" and computer_action=="Rock":
        print("You lose, computer wins")
    else: 
        print('You Win, computer Looses')

    while True:
        play_input=input('Do you want to play again, Yes or No\n')
        play_input=play_input.lower()
        if play_input=="yes":
            play_again=True
            break
        elif play_input=="no":
            play_again=False
            break
        else:
            print("Incorrect Input")







