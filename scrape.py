import bs4
import requests
import csv

# Function to extract player data from a single page
def extract_player_data(soup):
    players = soup.findAll('tr', 'player_tr_')
    for p in players:
        tds = p.findAll('td')
        name = tds[0].text.strip()
        clubs = p.find('span', 'players_club_nation').findAll('a')
        club = clubs[0]['data-original-title'].replace('Icons', 'unknown').strip()
        nation = clubs[1]['data-original-title'].replace('Icons', 'unknown').strip()
        league = clubs[2]['data-original-title'].replace('Icons', 'unknown').strip()
        return [name, club, nation, league]

# Function to get the total number of pages
def get_total_pages(soup):
    pagination = soup.find('ul', 'pagination')
    pages = pagination.findAll('li')
    last_page = pages[-2].text.strip()
    return int(last_page)

# Main program
response = requests.get('https://www.futbin.com/players?page=1')
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Get the total number of pages
total_pages = get_total_pages(soup)

# Extract player data for all pages
player_data = []
for page in range(1, total_pages + 1):
    response = requests.get(f'https://www.futbin.com/players?page={page}')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    player_data.extend(extract_player_data(soup))

# Write player data to CSV file
with open('player_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(player_data)
