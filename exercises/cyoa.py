"""Exercise 6 - Create your own Adventure!"""

__author__ = "730466526"


points: int = 0
player: str = ""
one: str = "1"
two: str = "2"
three: str = "3"
points_pt_two = 3


def main() -> None:
    """Buzzfeed quiz to find someones spirit animal."""
    greet()
    turn: int = 0
    global one
    global two
    global three
    global player
    global points
    zero: int = 0
    while turn <= 2:
        random_number: str = input("Please choose a number 1-3, where 1. will exit the game, 2 and 3 will begin the game: ")
        if random_number == one:
            route_one()
        if random_number == two:
            route_two()
            print(f"Thank you {player} for playing, you ended with {points}!")
        if random_number == three:
            route_three(zero)
            print(f"Thank you {player} for playing, you ended with {points}!")
        turn += 1


def greet() -> None:
    """Greeting to the game!"""
    party_emoji: str = "\U0001F973"
    global player
    print(f"Greetings player! Welcome to a Buzzfeed quiz where soul searching will be done and tears may arise. This is a very personal and life altering quiz that will look deep into your heart and tell you what animal is your SPIRIT AMINAL {party_emoji}!")
    player_name: str = input("To begin, please enter your name: ")
    player = player_name


def route_one() -> None:
    """Exiting the player from the experience."""
    llama: str = "\U0001F999"
    route_one_points: int = 1
    global points
    global player
    points += route_one_points
    print("We understand this soul searching quest is not for everyone, and we thank you for your time.")
    print(f"Here are the number of points you accumulated and the animal you are: {points}, {llama}!")


def route_two() -> None:
    """Playing the game!"""
    global one
    global two
    global three
    global player
    global points
    fish: str = "\U0001F420"
    swan: str = "\U0001F9A2"
    dog: str = "\U0001F415"
    import random
    number: int = random.randint(50, 55)
    choice: str = input(f"Welcome {player} to finding your spirit animal! Please enter the number beside the sentence that resonates most with you: 1. Do you love swimming, 2. Do you love flying, 3. Do your love walking/running: ")
    if choice == one:
        points += 1
    if choice == two:
        points += 50
    if choice == three:
        points += 100
    input("Next, which is your favorite color of these three: 1. Blue, 2. White, 3. Brown: ")
    if choice == one:
        points += 1
    if choice == two:
        points += number
    if choice == three:
        points += 100
    input(f"Final question {player}, if you were an element bender from Avater: The Last Airbender (not sponsored), which bender would you be?: 1. Water, 2. Air, 3. Earth: ")
    if choice == one:
        points += 1
    if choice == two:
        points += 50
    if choice == three:
        points += 100
    print("Time to find out your results!")
    if points <= 102:
        print(f"{player}, congratulations, you are a {fish}! Thank you for playing.")
    if points >= 103 and points < 200:
        print(f"{player}, congratulations, you are a {swan}! Thank you for playing.")
    if points >= 200:
        print(f"{player}, congratulations, you are a {dog}! Thank you for playing.")
    

def route_three(points_pt_two: int) -> int:
    """Updating players points."""
    fish: str = "\U0001F420"
    swan: str = "\U0001F9A2"
    dog: str = "\U0001F415"
    global one
    global two
    global three
    global player
    global points
    choices: str = input(f"Welcome {player} to finding your spirit animal! Please enter the number beside the sentence that resonates most with you: 1. Do you love swimming, 2. Do you love flying, 3. Do your love walking/running: ")
    if choices == one:
        points_pt_two += 1
    if choices == two:
        points_pt_two += 50
    if choices == three:
        points_pt_two += 100
    input("Next, which is your favorite color of these three: 1. Blue, 2. White, 3. Brown: ")
    if choices == one:
        points_pt_two += 1
    if choices == two:
        points_pt_two += 50
    if choices == three:
        points_pt_two += 100
    input(f"Final question {player}, if you were an element bender from Avater: The Last Airbender (not sponsored), which bender would you be?: 1. Water, 2. Air, 3. Earth: ")
    if choices == one:
        points_pt_two += 1
    if choices == two:
        points_pt_two += 50
    if choices == three:
        points_pt_two += 100
    points = points_pt_two
    print("Time to find out your results!")
    if points <= 102:
        print(f"{player}, congratulations, you are a {fish}! Thank you for playing.")
    if points >= 103 and points < 200:
        print(f"{player}, congratulations, you are a {swan}! Thank you for playing.")
    if points >= 200:
        print(f"{player}, congratulations, you are a {dog}! Thank you for playing.")
    return points


if __name__ == "__main__":
    main()