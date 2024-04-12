import random

#Gives credit to me and a mate that helped with planning
def credits():
    print("Made By Kaden Adams\n")
    print("With Help by Ash Clark")
    print("")




#checks if the user enters yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        elif response == "credits" or response == "secret":
            credits()
        else:
            print("please enter yes/no")

    # Main_Quiz

def get_float(question):
    while True:
        try:
            response = float(input(question))
            return response
        except:
            print('ERROR: Please enter a number! not Words!')

def instruction():
    print("_-_-_-_-_-_-_-_-_-_-_-_-INSTRUCTIONS-_-_-_-_-_-_-_-_-_-_-_")
    print("In this quiz you will be have to answer a series of       ")
    print("questions, depending on how many you get right will be    ")
    print("      your total at the end of the game.                  ")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ ")


# This bit of code displays the intro title
def display_intro():
    title = " Quiz "
    print("_" * len(title))
    print(title)
    print("_" * len(title))


# This code displays the menu
def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


# This code displays the separator
def display_separator():
    print("-" * 24)


# This code gets the users input
def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 6:
                if user_input > 0:
                    return user_input
                else:
                    get_user_input(prompt)

            else:
                get_user_input(prompt)

        except:
            print("That's not an option please choose between 1 and 5\n")


# This code gets the users solution
def get_user_solution(problem):
    print("Enter your answer \n")
    print(problem, end="")
    result = get_float(" = ")
    return result


# This code checks the solution
def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("WRONG!")
        return count


# This code makes the questions
def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 3:
        problem = str(number_one) + " x " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " / " + str(number_two) + " to one decimal place "
        solution = number_one / number_two
        solution = round(solution, 1)
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count


# This code displays the end result
def display_result(total, correct):
    global percentage
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.")

    if percentage < 5:
        print("You suck at math. :)")

    elif percentage > 5:
        print("Good Job, you don't suck at math.")


# This code gets angry at user for wasting time
def get_stuffed():
    get_stuffed = yes_no("are you kidding me????? \n")
    if get_stuffed == "quit" or get_stuffed == "bye":
        print("I quit.")
    else:
        print("Don't waste my time.")


# This code double checks whether the user wishes to play the game
def game_sure():
    game = yes_no("are you sure? \n")
    if game == "no" or game == "n":
        main()
    elif game == "yes" or game == "y":
        print({get_stuffed()})


# This code is the main part that runs everything
def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input('Please enter a number between 1 and 5\n')
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input('Please enter a number between 1 and 5\n')

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)


# This code asks for name
name = input("Hey! Whats your name?  \n").capitalize()
if name:
    print("Welcome " + name + "!")
    print()
# This code asks if user wants to read instructions
response = yes_no("Do you want to read the instructions? \n").capitalize()

if response == "Yes" or response == "Y":
    instruction()
print()

# This code asks if user wishes to play
should_start = yes_no("would you like to start the game? \n")
if should_start == "yes" or should_start == "y":
    print({main()})
else:
    game_sure()
