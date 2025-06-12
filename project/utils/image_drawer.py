import sys
from PIL import Image, ImageDraw, ImageFont


# constants for image positioning and colors
GAP = 20
HEIGHT = 18
SQ_COLOR = "#DA70D6"
CIR_COLOR = "#00FF00"
TITLE_COLOR = "#1C1480"


def load_image(path: str) -> dict[str, int]:
    """
    load an image and return both the image and its drawing context

    parameters:
        path (str): the specified path to load the image
    returns:
        image, draw: the loaded image and its drawing context
    """
    try:
        image = Image.open(path).convert("RGB")
        draw = ImageDraw.Draw(image)
        return image, draw
    except Exception as e:
        print(f"error loading image: {e}")
        sys.exit(1)


def save_image(image: Image.Image, path: str) -> None:
    """
    save the image to the specified path

    parameters:
        image (Image.Image): the loaded image
        path (str): the specified path to save the image
    returns:
        None: the function saves the image
    """
    image.save(path)


def color_weeks(draw: ImageDraw.Draw, weeks: int) -> None:
    """
    color a specified number of weeks to represent weeks lived

    parameters:
        weeks (int): number of weeks lived
        draw (ImageDraw.Draw): the drawing context
    returns:
        None: the function modifies an image but does not return a value
    """
    # define constants for image positioning
    X0, Y, BOX_SIZE = 118, 229, 9
    y = Y

    # color the squares row by row
    while weeks > 0:
        # calculate how many squares to color
        boxes_to_color = min(weeks, 52)
        endpoint = X0 + (boxes_to_color * GAP)

        # color a row
        for x in range(X0, endpoint, GAP):
            draw.rectangle([(x, y), (x + BOX_SIZE, y + BOX_SIZE)], fill=SQ_COLOR)

        # move to the next row
        weeks -= boxes_to_color
        y += HEIGHT


def circle_expectancy(draw: ImageDraw.Draw, xp: float) -> None:
    """
    circle a week that represents an average life expectancy

    parameters:
        xp (float): average life expectancy
        draw (ImageDraw.Draw): the drawing context
    returns:
        None: the function modifies an image but does not return a value
    """
    # define constants for image positioning
    X, Y = 123, 233
    y = Y

    # find average life expectancy in weeks
    xp_weeks = round(xp * 52)

    # find y position efficiently
    rows_to_move = xp_weeks // 52
    y += rows_to_move * HEIGHT
    last_row = xp_weeks % 52

    # find x position
    endcircle = X + (last_row * GAP)

    # draw a circle on top of the specified square
    draw.circle((endcircle, y), 9, fill=CIR_COLOR, outline="black")


def create_legend(draw: ImageDraw.Draw) -> None:
    """
    generate a legend with indicators to improve UX

    parameters:
        draw (ImageDraw.Draw): the drawing context
    returns:
        None: the function modifies an image but does not return a value
    """
    # define legend items
    legend_items = [
        ("avg life xp", CIR_COLOR),
        ("weeks lived", SQ_COLOR),
    ]

    # define constants for image positioning
    X, Y, SPACING, BOX_SIZE = 500, 1870, 160, 11

    # create legend dynamically
    for i, (name, color) in enumerate(legend_items):
        # define an offset position
        x_offset = i * SPACING

        # draw labels and write text for legend
        draw.rectangle(
            [X + x_offset, Y, X + BOX_SIZE + x_offset, Y + BOX_SIZE],
            fill=color,
            outline="black",
        )
        draw.text((X + 20 + x_offset, Y - 11), name, fill="black", font_size=24)


def draw_title(image: Image.Image, draw: ImageDraw.Draw, name: str):
    """
    draw "<name>'s Life in Weeks" centered between the top of the image
    and the top of the chart.
    """
    # define the title
    text = f"{name.title()}'s Life in Weeks"
    font_size = 35

    font = ImageFont.truetype("DejaVuSans.ttf", size=font_size)

    # measure text
    left, top, right, bottom = font.getbbox(text)
    text_width = right - left
    text_height = bottom - top

    # center horizontally
    x = (image.width - text_width) / 2
    chart_top_y = 150
    y_center = chart_top_y / 2

    # adjust y to account for text height
    y = y_center - (text_height / 2)

    # draw the title
    draw.text((x, y), text, font=font, fill=TITLE_COLOR)
