import datetime
import re
import sys

from utils.data_handler import choose_location, get_expectancy, goodbye
from utils.image_drawer import (
    load_image,
    save_image,
    color_weeks,
    circle_expectancy,
    create_legend,
    draw_title,
)
from utils.intro_maker import (
    display_greeting,
    display_results,
    calculate_weeks,
    parse_birthdate,
    show_box,
)


# file paths
LIFE_EXPECTANCY = "../project/data/life-expectancy.csv"
WEEKS_PATH = "../project/images/weeks.png"
SAVE_PATH = "../project/images/"

# constants for regex and date formats
NAME_REGEX = re.compile(r"^[A-Za-z'-]+$")
DATE_FORMATS = [
    (re.compile(r"^\d{2}/\d{2}/\d{4}$"), "%d/%m/%Y"),
    (re.compile(r"^\d{2}-\d{2}-\d{4}$"), "%d-%m-%Y"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
]


def main():
    """
    create your life in weeks chart using helper functions
    """
    # display intro
    display_greeting()
    name = get_valid_name()
    birthdate = get_valid_birthdate(name)
    display_results(name, birthdate)
    ask_to_continue(name)

    # prompt for country/continent and fetch average life expectancy
    choice = choose_location()
    expectancy = get_expectancy(choice, LIFE_EXPECTANCY)

    # calculate the number of weeks lived
    weeks_lived = calculate_weeks(birthdate)
    if weeks_lived > 4680:
        show_box(f"Congratulations, {name}", " you filled all the squares!")
        weeks_lived = 4680

    # load the image and get the drawing context
    image, draw = load_image(WEEKS_PATH)

    # color weeks, highlight average life expectancy, create the legend, and draw the title
    color_weeks(draw, weeks_lived)
    circle_expectancy(draw, expectancy)
    create_legend(draw)
    draw_title(image, draw, name)

    # save the modifed chart
    save_image(image, f"{SAVE_PATH}{name}.png")

    # display a nice farewell message
    goodbye()


def get_valid_name():
    """prompt for and validate the user's first name. Repeat on error"""
    show_box("Let's get started!", "What's your first name?")
    while True:
        name = input("\n> ").strip()
        # check whether name is empty
        if not name:
            show_box("Oops! It looks like your name is",
                     " playing hide & seek. Can you reveal it?")
        # check whether name is formatted properly
        elif not NAME_REGEX.fullmatch(name):
            show_box("Please share only your first name,",
                     "no spaces or extra words allowed!")
        else:
            return name


def get_valid_birthdate(name: str) -> str:
    """
    prompt the user for their birthdate, allow only valid formats and real dates
    repeats until a valid, non-future date is entered
    """
    # define the formatted prompt
    prompt = [
        f"Nice to meet you, {name}!",
        "Please enter your birthdate",
        "in one of these formats:",
        "dd/mm/yyyy dd-mm-yyyy yyyy-mm-dd",
    ]
    print()
    show_box(*prompt)
    today = datetime.date.today()
    while True:
        entry = input("\n> ").strip()
        print()
        date = parse_birthdate(entry)
        # check whether the format is valid
        if not any(regex.fullmatch(entry) for regex, _ in DATE_FORMATS):
            show_box("Error: Invalid format.", "Use: dd/mm/yyyy dd-mm-yyyy yyyy-mm-dd")
        # check whether the date is real
        elif not date:
            show_box("Error: That date does not exist!", "Please enter a valid date.")
        # check whether the date is allowed
        elif date > today:
            show_box("Error: Your birthdate can't be", "in the future. Try again!")
        else:
            return date


def ask_to_continue(name: str) -> bool:
    """display an intermediary menu"""
    show_box(f"{name}, are you ready", "to continue? (Yes/No)")
    while True:
        choice = input("\n> ").strip().lower()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            show_box("  Thank you for choosing our program! ", "Goodbye!")
            print()
            sys.exit(0)
        else:
            show_box("Invalid input!", "Please enter 'Yes' or 'No'.")
        print()


if __name__ == "__main__":
    main()
