import bs4
import requests
import csv

response = requests.get('https://www.futbin.com/players?page=1))
print(response.text)
soup = bs4.BeautifulSoup(response.text,'html.parser')
numbers = [1,2]
for number in numbers:
    players = soup.findAll('tr','player_tr_'+str(number))
    for p in players:
        tds = p.findAll('td')
        name = tds[0].text.strip()
        clubs = p.find('span', 'players_club_nation').findAll('a')
        club = clubs[0]['data-original-title'].replace('Icons', 'unknown').strip()
        nation = clubs[1]['data-original-title'].replace('Icons', 'unknown').strip()
        league = clubs[2]['data-original-title'].replace('Icons', 'unknown').strip()
        print('Name     : ',name)
        print('Club     : ',club)
        print('Nation   : ',nation)
        print('League   : ',league,'\n')


for page in range(1, 380):
    req =  requests.get('https://www.futbin.com/players?page='+str(page))
    soup = bs4.Beautiful...

datas =[]
for page in range(1, 380):
    req =  requests.get('https://www.futbin.com/players?page=1))

print('League   : ',league,'\n')
datas.append([name, club, nation, league])

