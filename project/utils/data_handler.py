import csv
import math
import sys


def load_data(file: str) -> dict:
    """
    load data from a CSV file and return a dictionary mapping entities to average life expectancy

    parameters:
        file (str): a filename or file path to the CSV file
    returns:
        exp (dict): a key-value pair for entity and average life expectancy
    raises:
        FileNotFoundError: if the file doesn't exist
    notes:
        average life expectancy is rounded up to the nearest integer for simplicity
    """
    # create an empty dictionary
    exp = {}

    # set up try-except block to ensure the existence of file
    try:
        with open(file) as f:
            reader = csv.DictReader(f)
            # map entities to average life expectancy dynamically
            exp = {
                row["Entity"].title(): math.ceil(float(row["Life Expectancy"]))
                for row in reader
            }
    except FileNotFoundError:
        raise FileNotFoundError(f"file not found {file}")

    # return a dictionary with entities and average life expectancy
    return exp


def choose_location() -> int:
    """
    display a menu for the user to choose a continent or country

    returns:
        choice (int): the user's selection
    """
    # define the formatted menu and error message
    menu = """
    ╔════════════════════════════════════════╗
    ║          LIFE EXPECTANCY MENU          ║
    ╠════════════════════════════════════════╣
    ║  1   based on your CONTINENT (general) ║
    ║  2   based on your COUNTRY (specific)  ║
    ╠════════════════════════════════════════╣
    ║     Enter 1 or 2 to make a selection   ║
    ╚════════════════════════════════════════╝
    """
    error_msg = """
    ╔════════════════════════════════════════╗
    ║         Error: Invalid choice.         ║
    ║          Please enter 1 or 2.          ║
    ╚════════════════════════════════════════╝
    """

    print(menu)

    # set up a while-loop to ensure the validity of input
    while True:
        # ask a user to choose whether to use continent or country to determine user's average life expectancy
        choice = input("> ").strip()
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print(error_msg)


def get_continent_expectancy(expectancy: dict[str, int]) -> int:
    """
    prompt the user to select a continent and return the associated life expectancy

    parameters:
        expectancy (dict): a dictionary with continents and life expectancy
    returns:
        expectancy[country] (int): average life expectancy given for a selected continent
    """
    # map continents to options
    continents = {
        "1": "Africa",
        "2": "Asia",
        "3": "Europe",
        "4": "North America",
        "5": "Oceania",
        "6": "South America",
        "7": "World",
    }

    # define the formatted menu and error message
    menu = """
    ╔════════════════════════════════════════╗
    ║           SELECT A CONTINENT           ║
    ╠════════════════════════════════════════╣
    ║  1   Africa                            ║
    ║  2   Asia                              ║
    ║  3   Europe                            ║
    ║  4   North America                     ║
    ║  5   Oceania                           ║
    ║  6   South America                     ║
    ║  7   World                             ║
    ╠════════════════════════════════════════╣
    ║     Enter 1 to 7 to make a selection   ║
    ╚════════════════════════════════════════╝
    """
    error_msg = """
    ╔════════════════════════════════════════╗
    ║         Error: Invalid choice.         ║
    ║      Please enter a number 1 to 7.     ║
    ╚════════════════════════════════════════╝
    """

    print(menu)

    # set up a while-loop to ensure the validity of input
    while True:
        # ask a user to select their continent to determine user's average life expectancy
        choice = input("> ").strip()
        if choice in continents:
            continent = continents[choice]
            return expectancy[continent]
        else:
            print(error_msg)


def get_country_expectancy(expectancy: dict[str, int]) -> int:
    """
    prompt the user to select a country and return the associated life expectancy

    parameters:
        expectancy (dict): a dictionary with countries and life expectancy
    returns:
        expectancy[country] (int): average life expectancy given for a selected country
    """
    # define the formatted menu and error message
    menu = """
    ╔════════════════════════════════════════╗
    ║            SELECT A COUNTRY            ║
    ╠════════════════════════════════════════╣
    ║          Type in your country          ║
    ╚════════════════════════════════════════╝
    """
    error_msg = """
    ╔════════════════════════════════════════╗
    ║       Error: Invalid country name.     ║
    ║        Please check the spelling.      ║
    ╚════════════════════════════════════════╝
    """

    print(menu)
    # set up a while-loop to ensure the validity of input
    while True:
        # ask a user to select their country to determine user's average life expectancy
        country = input("> ").strip().title()
        if country in expectancy:
            return expectancy[country]
        else:
            print(error_msg)


def get_expectancy(choice: int, data_file: str) -> int:
    """
    determine the average life expectancy based on user's choice (continent or country)

    parameters:
        entity (int): the user's choice (continent or country)
    returns:
        expectancy[country] (int): average life expectancy given for a continent/country
    """
    # load data from the csv file and store it in a dictionary
    expectancy = load_data(data_file)

    # find the average life expectancy based on the continent or country
    if choice == 1:
        return get_continent_expectancy(expectancy)
    else:
        return get_country_expectancy(expectancy)


def goodbye() -> None:
    """
    display a farewell message to the user
    """
    # define the formatted menu
    menu = """
    ╔════════════════════════════════════════╗
    ║               THANK YOU!               ║
    ╠════════════════════════════════════════╣
    ║           Your chart is ready          ║
    ║               Good luck!               ║
    ╚════════════════════════════════════════╝
    """

    sys.exit(menu)
