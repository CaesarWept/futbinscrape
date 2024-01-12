# Football Player Comparison App

## Overview

- This Python script was designed to compare retired football players using an Elo-based rating system, inspired by the player comparison feature on Transfermarkt.
- The aim was to create a python script that could compare players who are no longer active in professional football, eg: Iniesta, Robben, Maradona.
- V0.1. Simple early draft created on a PC without access to VS Code or alternative editor. 


## Features

- **Player Elo Ratings:** Each player is assigned an Elo rating, which adjusts based on the outcomes of comparisons.
  
- **Player Images:** The application displays player images for side-by-side visual comparisons.

- **Dynamic Resizing:** Player images are dynamically resized to fit the user's screen, maintaining the original aspect ratios.

- **User Interaction:** Users can vote for their preferred player in each comparison, influencing the players' Elo ratings.

- **Persistent Data:** Player data, including Elo ratings, is saved locally to provide continuity across sessions.

## Usage

1. **Installation:**
    - Clone the repository to your local machine.
    - Ensure you have Python installed.

2. **Run the Application:**
    - Open a terminal in the project directory.
    - Run `python filename.py` (replace `filename.py` with the actual filename of your Python script).

3. **Player Comparisons:**
    - Players are presented side-by-side with their names and Elo ratings.
    - Vote for your preferred player by clicking the corresponding button.
    - Elo ratings are updated based on the outcomes of each comparison.

4. **Local Data Storage:**
    - Player data, including Elo ratings, is saved in a local file (`players_data.pkl`).
    - Ensure the file has read and write permissions.

## Customization

- **Adjust Elo Parameters:**
    - Modify the `STARTING_ELO` and `k_factor` variables to adjust the starting Elo rating and the impact of each match on ratings.

- **Resize Images:**
    - Change the `target_screen_fraction` variable to adjust the size of player images on the screen.

- **Button Size:**
    - Customize the size of the vote buttons by modifying the `button_size` variable.

## Inspirations

This application is inspired by the player comparison features found on popular football-related platforms, offering a nostalgic experience for football fans to reminisce about retired players.

## Acknowledgments

- Inspired by Transfermarkt Player Comparison Tool
- Built using Python, Tkinter, and PIL.

## License

This project is licensed under the [MIT License](LICENSE).
