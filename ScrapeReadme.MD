# Futbin Player Data Scraper

## Overview

This Python script scrapes player data from the Futbin website, specifically focusing on FIFA player details. It utilizes BeautifulSoup for web scraping and writes the collected data to a CSV file for further analysis or usage.

## Features

- **Data Extraction:** Extracts player information including name, club, nation, league, rating, version, and attribute details.
  
- **Pagination Handling:** Dynamically identifies and navigates through multiple pages to ensure all player data is captured.

- **CSV Export:** Outputs the collected player data to a CSV file (`player_data.csv`) for easy integration with data analysis tools.

## Usage

1. **Installation:**
    - Clone the repository to your local machine.
    - Install the required Python packages using `pip install -r requirements.txt`.

2. **Run the Script:**
    - Open a terminal in the project directory.
    - Run the script using `python filename.py` (replace `filename.py` with the actual filename of your Python script).

3. **CSV Output:**
    - The script will generate a CSV file named `player_data.csv` in the same directory.

## Requirements

- Python 3.x
- BeautifulSoup (installed via `pip install beautifulsoup4`)
- Requests (installed via `pip install requests`)

## Customization

- **URL Modification:**
    - Adjust the URL in the script to target different pages or sections of the website if needed.

- **CSV Header:**
    - Modify the `csv_writer.writerow` line to customize the header of the CSV file.

## Acknowledgments

This script is designed to automate the collection of player data from the Futbin website for analysis and research purposes.

## License

This project is licensed under the [MIT License](LICENSE).
