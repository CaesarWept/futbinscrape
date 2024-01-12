import bs4
import requests
import csv

# Function to extract player data from a single page
def extract_player_data(soup):
    # Get player name
    name = soup.find('h1', {'class': 'player_name'}).text.strip()

    # Get player club and nation
    clubs = soup.find('span', {'class': 'players_club_nation'}).findAll('a')
    club = clubs[0]['data-original-title'].replace('Icons', 'unknown').strip()
    nation = clubs[1]['data-original-title'].replace('Icons', 'unknown').strip()

    # Get player league
    league = soup.find('span', {'class': 'player_club_nation'}).find('a')['title'].replace('Icons', 'unknown').strip()

    # Get player rating
    rating = soup.find('div', {'class': 'player_rating'}).text.strip()

    # Get player version
    version = soup.find('div', {'class': 'player_version'}).text.strip()

    # Get player attributes
    attributes = soup.findAll('div', {'class': 'player_attribute'})
    pace = attributes[0].text.strip()
    shooting = attributes[1].text.strip()
    passing = attributes[2].text.strip()
    dribbling = attributes[3].text.strip()
    defense = attributes[4].text.strip()
    physical = attributes[5].text.strip()

    # Return player data as a list
    return [name, club, nation, league, rating, version, pace, shooting, passing, dribbling, defense, physical]

# Function to get the total number of pages
def get_total_pages(soup):
    pagination = soup.find('ul', {'class': 'pagination'})
    pages = pagination.findAll('li')
    last_page = pages[-2].text.strip()
    return int(last_page)

# Main program
response = requests.get('https://www.futbin.com/players?page=1')
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Get the total number of pages
total_pages = get_total_pages(soup)

# Create a list to store all player data
player_data = []

# Iterate through all pages and extract player data for each page
for page in range(1, total_pages + 1):
    response = requests.get(f'https://www.futbin.com/players?page={page}')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    players = soup.findAll('tr', {'class': 'player_tr'})
    for player in players:
        player_data.append(extract_player_data(player))

# Write player data to CSV file
with open('player_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Club', 'Nation', 'League', 'Rating', 'Version', 'Pace', 'Shooting', 'Passing', 'Dribbling', 'Defense', 'Physical'])
    csv_writer.writerows(player_data)
