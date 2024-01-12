#FUTBIN Player Data Scraper

This script scrapes player data from the FUTBIN website and saves it to a CSV file. The data includes player name, club, nation, league, rating, version, pace, shooting, passing, dribbling, defense, and physical attributes.

## Usage
Install the required Python libraries:
Copy
pip install bs4 requests csv
Save the script as a file with a .py extension, e.g. futbin_scraper.py.
Open the script in a text editor and replace the https://www.futbin.com/players?page=1 URL with the URL of the FUTBIN page you want to scrape data from.

Run the script using the following command:

Copy
python futbin_scraper.py
The script will generate a CSV file named player_data.csv containing the scraped data.
Example
The following is an example of the data that will be saved to the CSV file:

apache
Copy
Name,Club,Nation,League,Rating,Version,Pace,Shooting,Passing,Dribbling,Defense,Physical
Pelé,Paris Saint-Germain,Brazil,Ligue 1,96,Winter Wildcard,94,95,90,95,59,80
Cristiano Ronaldo,Manchester United,Portugal,Premier League,94,Base,93,94,79,94,43,75
Lionel Messi,FC Barcelona,Argentina,La Liga,93,Base,92,91,86,92,54,82
Neymar Jr.,Paris Saint-Germain,Brazil,Ligue1,93,Versus Ice,91,87,90,97,41,66
Kylian Mbappé,Paris Saint-Germain,France,Ligue1,93,UCL TOTGS,98,92,84,94,40,81

## Troubleshooting
- If you are having problems running the script, make sure that you have installed the required Python libraries.
- If you are getting an error message saying "ModuleNotFoundError: No module named 'bs4'", make sure that you have installed the beautifulsoup4 library.
- If you are getting an error message saying "ModuleNotFoundError: No module named 'requests'", make sure that you have installed the requests library.
- If you are getting an error message saying "ModuleNotFoundError: No module named 'csv'", make sure that you have installed the csv library.

## License
This script is licensed under the MIT License.
