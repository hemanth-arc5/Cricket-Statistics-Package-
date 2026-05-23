# Cricket Statistics Package

A beginner-friendly Python package for cricket statistics analysis.
This project demonstrates how to create and use installable Python packages with modular structure and reusable functions.

It covers:

Python Modules
Python Packages
Installable Packages using setup.py
Importing Packages Outside the Project Directory
Clean Project Structure

---

## Project Structure
cricketstats_project/
│
├── setup.py
├── README.md
│
├── cricketstats/
│   ├── __init__.py
│   ├── batting.py
│   ├── bowling.py
│   └── team.py
│
├── demo_inside_project.py
└── outside_demo.py

---

## Features

### Batting Module (batting.py)

Functions available:

Calculate batting average
Calculate strike rate
Find highest score
Functions
batting_average(runs, innings)
strike_rate(runs, balls)
highest_score(scores)

### Bowling Module (bowling.py)

Functions available:

Calculate economy rate
Calculate bowling average
Find best bowling figures
Functions
economy_rate(runs, overs)
bowling_average(runs, wickets)
best_figures(figures)

### Team Module (team.py)

Functions available:

Display player names
Calculate total team score
Functions
show_players()
team_score(scores)

---

## Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/cricketstats_project.git

2️⃣ Move into the Project Folder

cd cricketstats_project

3️⃣ Install the Package

pip install .

💻 Usage Example

Create a Python file outside the project folder and use the package like this:

from cricketstats import *

print("Batting Average:", batting_average(5000, 120))
print("Strike Rate:", strike_rate(80, 60))
print("Highest Score:", highest_score([45, 90, 120]))

print("Economy Rate:", economy_rate(45, 10))
print("Bowling Average:", bowling_average(200, 15))
print("Best Figures:", best_figures([(3, 25), (5, 20)]))

print("Players:", show_players())
print("Team Score:", team_score([120, 80, 95]))

---

## Sample Output

Batting Average: 41.66

Strike Rate: 133.33

Highest Score: 120

Economy Rate: 4.5

Bowling Average: 13.33

Best Figures: (5, 20)


Players: ['Virat Kohli', 'Rohit Sharma', 'MS Dhoni']

Team Score: 295

### Technologies Used

Python 3

setuptools

pip

---

## Concepts Covered

Python Modules

Python Packages

__init__.py

setup.py

Package Installation

Importing Packages

Function-Based Programming
