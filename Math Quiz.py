import random


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes/no")

    # Main_Quiz


def instruction():
    print("_-_-_-_-_-_-_-_-_-_-_-_-INSTRUCTIONS-_-_-_-_-_-_-_-_-_-_-_")
    print("In this quiz you will be have to answer a series of       ")
    print("questions, depending on how many you get right will be    ")
    print("      your total at the end of the game.                  ")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ ")


def display_intro():
    title = " Quiz "
    print("_" * len(title))
    print(title)
    print("_" * len(title))


def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


def display_separator():
    print("-" * 24)


def get_user_input():
    error = "That's not an option, 1-5 Only."
    try:
        response = int(input("Enter your choice, 1-5: "))

        if response < 13:
            print(error)
        else:
            print(response)

    except ValueError:
        print(error)



def get_user_solution(problem):
    print("Enter your answer \n")
    print(problem, end="")
    result = float(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("WRONG!.")
        return count


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
        problem = str(number_one) + " * " + str(number_two)
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


def display_result(total, correct):
    global percentage
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.")


def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)


name = input("Hey! Whats your name?  \n").capitalize()
if name:
    print("Welcome " + name + "!")
    print()

response = yes_no("Do you want to read the instructions? \n").capitalize()

if response == "Yes" or response == "Y":
    instruction()
print()

should_start = yes_no("would you like to start the game? \n")
if should_start == "yes" or should_start == "y":
    print({main()})
else:
    print()

game = yes_no("are you sure? \n")
if game == "no" or game == "n":
    print({main()})
elif game == "yes" or game == "y":
    print()

get_stuffed = yes_no("are you kidding me????? \n")
if get_stuffed == "quit" or get_stuffed == "bye":
    print("I quit.")
else:
    print("Don't waste my time.")