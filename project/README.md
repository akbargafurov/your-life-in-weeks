# life in weeks – the final project
for CS50's Introduction to Programming with Python <br>
by Akbar Gafurov & Arevik Osipyan

video overview: <[life in weeks](https://youtu.be/FDV3obZF4H4)>

## motivation
We were inspired to create this application after reading a thought-provoking article by Tim Urban, [Your Life in Weeks](https://waitbutwhy.com/2014/05/life-weeks.html), which depicts our lives as a grid of squares, each representing one week. We believe that it's essential to reflect on the past and present to intentionally build a more fulfilling and purposeful future. This app can help to achieve this noble goal!

## project overview
Our project is a visualizer that helps users understand their lives in weeks by calculating how many weeks they have already lived and how many remain (based on their continent's or country's average life expectancy). It features time-based calculations, data interpretation, and graphical representation to create a meaningful visual reflection of a user's lifespan up to date.

## project structure
The project consists of the following key components:
```
project/
│
├── project.py
├── test_project.py
├── data/
│   └── life_expectancy.csv
├── images/
│   └── example.png
│   └── weeks.png
├── utils/
│   └── data_handler.py
│   └── image_drawer.py
│   └── intro_maker.py
├── LICENSE
├── requirements.txt
└── README.md
```
This modular structure separates responsibilities for cleaner code management and easier future scalability.

## features
Our project includes the following features:
* user input interface: displays command-line prompts to collect user's birthdate and country/region
* age & week calculation: determines current age in weeks and compares it to the average life expectancy for the selected continent/country
* visual chart generator: creates a personal life-in-weeks chart using rows and columns of squares, with the squares associated with lived weeks filled in a different color
* data-driven life expectancy: incorporates actual average life expectancy data by country for more personalized results
* chart export: allows users to download their life chart as a PNG image
* perspective tool: offers a unique, minimalistic view on time usage and remaining life expectancy to encourage reflection

## prerequisites
Ensure Python 3.8+ is installed along with required libraries:
* Pillow

To install required libraries, run `pip install -r requirements.txt`

Note: This project also uses built-in Python modules:
* csv
* datetime
* math
* re
* sys

## usage
To use the project, run `python project.py`:
* enter your first name
* enter your birthdate
* select your continent or country
* view a visual representation of your life in weeks
* download the chart

This app can be used to raise self-awareness, help with goal-setting, and gain perspective on how much time we have spent, where we are now, and what we want to do in the future.

## example
A user born on December 2, 2000, from Uzbekistan sees that he/she has lived approximately 1274 weeks out of an average 3744 (72 years). The chart starkly demonstrates that he/she has passed a third of his/her lifespan – encouraging reflection and renewed motivation for the next stage of his/her life.

![example chart](../project/images/example.png)

## limitations
Current constraints reflect the project's demo-stage and include:
* a fixed maximum life expectancy of 90 years
* a basic chart design with minimal customization options
* a download option limited to PNG format only
* a lack of interactive features or real-time user input

These limitations define the current scope while presenting an opportunity for future improvements.

## optimization
Future improvements could include some additional features:
* interactive graphs to create a more dynamic experience
* different charts to provide a varied perspective on life
* color-coding system to highlight significant life stages
* sharing capabilities to easily exchange life visualizations

These enhancements would potentially improve the app's functionality and versatility.

## conclusion
This project reminds us all that our time is finite and valuable. By visually representing our life in weeks, we hope to spark introspection and motivate intentional living. As more users try out this tool, we envision it becoming a companion for life planning and reflection.

## license
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
