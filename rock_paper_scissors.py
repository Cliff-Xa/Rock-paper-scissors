import random
# introduction
print('--- Rock, Paper, Scissors Game ---')

# list of choices
choices = ['rock', 'paper', 'scissors']

# input name
name = input('enter your name: ').title()

# users_score
name_count = 0
machine_count = 0

# introduction
print(f'hello, {name}. Your choices are -rock, paper & scissors-')

while True:
    # user input
    user_choice = input('enter your choice: ').lower()

    # machine spins
    machine = random.choice(choices)

    # validate user input
    if user_choice not in choices:
        print('invalid choice')
        continue

    # in case of a tie
    if user_choice == machine:
        print('this is a tie')
        continue

    # determining winner
    if user_choice == 'paper':
        if machine == 'rock':
            print('you win')
            name_count += 1
        else:
            print('machine wins')
            machine_count += 1

    if user_choice == 'rock':
        if machine == 'scissors':
            print('you win')
            name_count += 1
        else:
            print('machine wins')
            machine_count += 1

    if user_choice == 'scissors':
        if machine == 'paper':
            print('you win')
            name_count += 1
        else:
            print('machine wins')
            machine_count += 1


    # ask to play again
    user_answer = input('do you want to play again? ').lower()

    # validat users answer
    if user_answer != 'y':
        print('thank for playing')
        if machine_count > name_count:
            print(f'machine wins with -- {machine_count} -- points')
        elif name_count > machine_count:
            print(f'You win with -- {name_count} -- points')
        else:
            print('This is a tie')

        break


