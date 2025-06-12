import datetime
import re


# constants for boxes, regex, and date formats
MENU_WIDTH = 40
INDENT = " " * 4
NAME_REGEX = re.compile(r"^[A-Za-z'-]+$")
DATE_FORMATS = [
    (re.compile(r"^\d{2}/\d{2}/\d{4}$"), "%d/%m/%Y"),
    (re.compile(r"^\d{2}-\d{2}-\d{4}$"), "%d-%m-%Y"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
]


def make_box(lines: list) -> str:
    """draw a styled box with centered text for a list of lines"""
    border = "═" * MENU_WIDTH
    box = INDENT + "╔" + border + "╗\n"
    for line in lines:
        box += INDENT + "║" + line.center(MENU_WIDTH) + "║\n"
    box += INDENT + "╚" + border + "╝"
    return box


def show_box(*lines: str):
    """prints provided lines of text inside a styled box"""
    print(make_box(list(lines)))


def display_greeting():
    """show a time-based greeting in a box"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good Morning!"
    elif hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Night!"
    print()
    show_box(greeting, "Welcome to Life In Weeks Program!")
    print()


def parse_birthdate(entry: str) -> str:
    """
    try to parse entry as a birthdate using supported formats
    return a date object if successful, else None
    """
    for regex, fmt in DATE_FORMATS:
        # check whether the date is formatted
        if regex.fullmatch(entry):
            try:
                return datetime.datetime.strptime(entry, fmt).date()
            except ValueError:
                return None
    return None


def calculate_weeks(birthdate: str) -> int:
    """calculate the number of weeks in a year, assuming 1 year equals 52 weeks"""
    today = datetime.date.today()

    # calculate the number of weeks
    years_lived = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    last_birthday = birthdate.replace(year=birthdate.year + years_lived)
    extra_days = (today - last_birthday).days

    return years_lived * 52 + extra_days // 7


def display_results(name: str, birthdate: str) -> None:
    """
    show the user's registered birthdate and how many full weeks they've lived,
    using the formatted box output.
    """
    weeks = calculate_weeks(birthdate)
    date_str = birthdate.strftime("%d %B %Y")
    show_box(f"Thank you, {name}!", "Your birthdate is recorded as:", date_str)
    print()
    show_box("You have lived approximately", f"{weeks} full weeks.")
    print()
