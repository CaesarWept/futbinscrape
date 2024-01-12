# Football Player Comparison App and Futbin Player Data Scraper
Inspired by the transfermarkt player comparison feature. Data scraping exercise. Inspired by the player comparison feature on transfermarkt, the goal was to compare retired players, eg Robben, Iniesta, Maradona, etc.  Built as a data scraping exercise on a PC without access to VS studio or an alternative code editor :(. 

## Futbin Player Data Scraper

### Overview

The Futbin Player Data Scraper is a Python script designed to extract player data from the Futbin website. It focuses on  player details, including name, club, nation, league, rating, version, and attribute details.

### Features

- **Data Extraction:** Extracts player information from multiple pages on the Futbin website.

- **Pagination Handling:** Dynamically identifies and navigates through multiple pages to ensure all player data is captured.

- **CSV Export:** Outputs the collected player data to a CSV file (`player_data.csv`) for easy integration with data analysis tools.

### Usage

1. **Installation:**
    - Clone the repository to your local machine.
    - Install the required Python packages using `pip install -r requirements.txt`.

2. **Run the Script:**
    - Open a terminal in the project directory.
    - Run the script using `python filename.py` (replace `filename.py` with the actual filename of your Python script).

3. **CSV Output:**
    - The script will generate a CSV file named `player_data.csv` in the same directory.

### Example
The following is an example of the data that will be saved to the CSV file:

```Name,Club,Nation,League,Rating,Version,Pace,Shooting,Passing,Dribbling,Defense,Physical
Pelé,Paris Saint-Germain,Brazil,Ligue 1,96,Winter Wildcard,94,95,90,95,59,80
Cristiano Ronaldo,Manchester United,Portugal,Premier League,94,Base,93,94,79,94,43,75
Lionel Messi,FC Barcelona,Argentina,La Liga,93,Base,92,91,86,92,54,82
Neymar Jr.,Paris Saint-Germain,Brazil,Ligue1,93,Versus Ice,91,87,90,97,41,66
Kylian Mbappé,Paris Saint-Germain,France,Ligue1,93,UCL TOTGS,98,92,84,94,40,81```

## Troubleshooting

- If you are having problems running the script, make sure that you have installed the required Python libraries.
- If you are getting an error message saying "ModuleNotFoundError: No module named 'bs4'", make sure that you have installed the beautifulsoup4 library.
- If you are getting an error message saying "ModuleNotFoundError: No module named 'requests'", make sure that you have installed the requests library.
- If you are getting an error message saying "ModuleNotFoundError: No module named 'csv'", make sure that you have installed the csv library.
  
## Football Player Comparison App

### Overview

The Football Player Comparison App allows users to compare retired football players who are no longer playing. 

### Features

- **Player Comparison:** View two players side by side and vote for the preferred player.
  
- **Elo Rating System:** Utilizes an Elo rating system to dynamically adjust player ratings based on user votes.

- **Image Resizing:** Automatically resizes player images for a consistent and appealing user interface.

### Usage

1. **Installation:**
    - Clone the repository to your local machine.
    - Ensure you have Python and the required dependencies (Tkinter, Pillow) installed.

2. **Run the App:**
    - Open a terminal in the project directory.
    - Run the app using `program.py`
      
3. **Player Data Storage:**
    - Player data, including Elo ratings, is saved locally in a file named `players_data.pkl`.

### Customization

- **Player Images:**
    - Add or replace player images in the designated folder (`E:\Sept 2022 Lenovo\Football` in the provided script).

- **Elo Starting Value:**
    - Adjust the `STARTING_ELO` constant in the script to change the initial Elo rating.


### Requirements

- Python 3.x
- BeautifulSoup (installed via `pip install beautifulsoup4`)
- Requests (installed via `pip install requests`)

### Acknowledgments

- These projects are developed for research and analysis purposes, providing tools for comparing retired football players.
- Inspired by the transfermarkt player comparison feature. 


### License

This project is licensed under the [MIT License](LICENSE).
