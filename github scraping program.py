import requests
from bs4 import BeautifulSoup as bs

github_user = raw_input("Input Github user (nick): ")

try:
    url = 'https://github.com/{}'.format(github_user)
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')

    comp_name = soup.find('span', {'class': 'p-name'}).get_text().strip()
    profile_bio = soup.find('div', {'class': 'user-profile-bio'}).get_text()
    fwers_fwing_stars = []
    profile_img = soup.find('img', {'alt': 'Avatar'})['src']
    tot_repo = soup.find('span', {'class': 'Counter'})['title']
    location = soup.find('span', {'class': 'p-label'}).get_text()

    print("\nComplete mame: {}".format(comp_name))
    print("Profile Bio: {}".format(profile_bio))
    print("Profile Photo: {}".format(profile_img))
    print("Total Repositories: {}".format(tot_repo))
    print("Location: {}".format(location))
except AttributeError:
    print("Profile not encountered!")