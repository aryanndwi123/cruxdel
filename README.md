# Cricket Match Simulation

This is a Python script that simulates a cricket match between two teams. The script uses randomization to determine the outcome of each ball and provides commentary throughout the match.

## Prerequisites

To run this script, you need to have Python installed on your system. The script is compatible with Python 3.

## How to Run

1. Copy the code from the above section into a Python file (e.g., `main.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python file is located.
4. Run the following command to execute the script:

## Script Overview

The script consists of several classes and functions to simulate a cricket match. Here's a brief overview of each component:

### Classes

1. `Player`: Represents a cricket player with attributes such as name, batting, bowling, fielding, running, and experience. Keeps track of the player's performance statistics during the match.
2. `Team`: Represents a cricket team with a name and a list of players. It also has methods to select a captain, determine the next batsman and bowler, and store batting and bowling lineups.
3. `Field`: Represents the cricket field with attributes like size, fan ratio, pitch conditions, and home advantage.
4. `Umpire`: Simulates the umpire's role in the match by keeping track of the score, wickets, and overs. It also simulates each ball's outcome based on player ratings.
5. `Commentator`: Provides commentary during the match, displaying information about events and outcomes.
6. `Match`: Orchestrates the entire match simulation. It handles the toss, innings, score calculation, and commentary. It also displays the final scoreboard and declares the winner.

### Functions

The script includes the following functions:

- `simulate_ball`: Simulates a ball being played between a batsman and a bowler. It calculates the outcome based on the player's ratings and returns the result.
- `provide_commentary`: Displays the provided commentary message in the console.

### Execution

At the end of the script, a match instance is created with two teams (India and England) and a field configuration. The match is then started by tossing a coin to decide which team bats or bowls first. The innings progress ball by ball, with outcomes and commentary displayed. Once the innings are over, the match proceeds to the next innings if applicable. Finally, the script displays the scoreboard and declares the winner based on the target and chase scores.

Please note that the script uses randomization to determine match outcomes, so the results may vary with each execution.

Feel free to modify the player names, ratings, teams, and field configurations to create your own match simulations.

Enjoy the cricket match simulation!