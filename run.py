import os
from colorama import Fore, Style
from random import randint
from time import sleep


def read_file(file):
    """
    Reading file and return in lines
    """
    with open(file, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def ask_name():
    """
    Asking Username for conecting
    """
    player_name = input('Please enter your Username.\n')
    if not player_name.strip():
        player_name = "Superuser"
    print(f'''
    {Fore.GREEN}Welcome to
    {Fore.YELLOW}The Famous Places and Countries game,
    {Fore.BLUE}{player_name}!
    {Fore.GREEN}You have 10 questions...
    ''')
    return player_name


def handle_quit(user_input, score, questions_answered_count):
    """
    Asking for quit or continue playing game
    """
    if user_input.lower() == 'y':
        return
    elif user_input.lower() == 'n':
        if score == 0:
            print(f'''
{Fore.BLUE}Your score is
{Fore.RED}{score} {Style.RESET_ALL}out of {questions_answered_count}
Thanks for enjoying my little Python terminal game!
Come back for more!
''')
        else:
            print(f'''
{Fore.BLUE}Your score is {Fore.GREEN}{score}
{Style.RESET_ALL}out of {questions_answered_count}
Thanks for enjoying my little Python terminal game!
Come back for more!
 ''')
        quit()
    else:
        play = input(f'{Style.BRIGHT} Please enter Y; or N.\n')
        handle_quit(play, score, questions_answered_count)


def generate_rand_int(data, upper_bound):
    random_index = randint(0, upper_bound - 1)
    if random_index in data:
        return generate_rand_int(data, upper_bound)
    return random_index


def validate_response():
    while True:
        response = input(f'''
{Fore.GREEN}Please enter country name.
For example, France, Great Britain.\n
''')
        answer = response.lower()
        try:
            if answer.isdigit():
                raise TypeError(f'{Fore.RED}You entered a number!{Fore.GREEN}')
            elif any(str.isdigit(i) for i in answer):
                raise TypeError(f'''
{Fore.RED}You entered a name
with a number!{Fore.GREEN}
''')
            elif not answer.strip():
                print(f'''
                {Fore.RED}You entered an empty string or only spaces!
                {Fore.GREEN}Try again!
                ''')
            else:
                return answer
        except TypeError as e:
            print(f'Invalid input. {e}')


def play_game():

    """
    Main program function
    """
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Shows welcoming message
    print(f'''
    {Fore.GREEN}Welcome to {Fore.YELLOW}My small Python Terminal GAME!
    {Fore.GREEN}I ask you about Famous places in the World.
    And you need try answer the question 'Where is this?'
    {Fore.RED}OK?
    {Fore.GREEN}LET'S GO!!!
    ''')
    places_list = read_file('places.txt')
    countries_list = read_file('countries.txt')
    player_score = 0
    qu_ansd_ind = []

    ask_name()
    sleep(1)
    while True:
        random_index = generate_rand_int(qu_ansd_ind, len(places_list))
        place = places_list[random_index]
        country_index = places_list.index(place)
        print(f'''
{Fore.GREEN}In which country is
the famous place  {Fore.RED} {place}
{Fore.GREEN}located?
''')
        player_answer = validate_response()

        qu_ansd_ind.append(country_index)

        if countries_list[country_index] == player_answer:
            country = countries_list[country_index]
            print(f'''
            The famous place {place} is located in: {country}
            {Style.BRIGHT}Well done!{Style.RESET_ALL}{Fore.GREEN}
            ''')
            player_score += 1
        else:
            print(f'''
             {Fore.RED}You missed this time
            Hint: Next time check your spelling{Fore.GREEN}
            ''')

        if len(qu_ansd_ind) == 10:
            question_count = len(qu_ansd_ind)
            print(f'Your score is {player_score} out of {question_count}')
            play = input(f'{Style.BRIGHT}GAME OVER{Style.RESET_ALL}, press Y to start again or N to quit:\n')
            handle_quit(play, player_score, len(qu_ansd_ind))
            player_score = 0
            qu_ansd_ind.clear()


def main():
    play_game()


if __name__ == '__main__':
    main()
