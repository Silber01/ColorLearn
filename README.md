# ColorLearn

## What is ColorLearn?
ColorLearn is a machine learning algorithm that, given a color, attempts to categorize it. The more colors it learns, the more accurate it is at successfully guessing colors.

## How to Use
Users can use the program in one of two ways: Through REST API calls (shown at <a href="https://www.danielsla.de/colorLearn">my website</a>), or by using the GUI in the app.
For either method, first install the required packages with `pip install -r requirements.txt`.
To use the GUI, run `main.py`. To host the REST API, run `model/__init__.py`.

## How it Works
Given a color, the program will analyze its red, green, and blue values and graph their values on a 3D graph along with all other colors that it has seen. Then, it finds the three closest colors of each color type on that graph, and calculates the average of each color type. The color with the lowest average distance is concluded to be the same color, meaning the bot has figured out the color.

## Tools and Frameworks Used
The program was made using Python. The built-in GUI for ColorLearn is made using Tkinter, and the REST API was created using flask.



