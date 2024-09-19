from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate 
import re

app = Flask(__name__)

custom_headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
} 

def extract_expiration_date(input_string):
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    matches = re.findall(date_pattern, input_string)
    
    if matches:
        return matches[-2] 
    else:
        return None   

def extract_regular_rating(input_text):
    regular_rating_pattern = r"Regular Rating\s*?\n\s*\n\s*(\d+)\s*?\n(\d{4}-\d{2})(?:\(Current floor is (\d+)\))?"
    match = re.search(regular_rating_pattern, input_text)
    
    if match:
        regular_rating = match.group(1)
        rating_date = match.group(2)
        floor_rating = match.group(3) if match.group(3) else "N/A"
        return regular_rating, rating_date, floor_rating
    else:
        return None, None, None  # Regular rating not found in the input text



def view_players(ids):
    base_url = "https://www.uschess.org/msa/MbrDtlTnmtHst.php?" 
    pub_url = "https://www.uschess.org/msa/MbrDtlMain.php?" 
    all_player_data = []  # To store information for all players

    for player_id in ids:
        url = base_url + str(player_id)
        html = requests.get(url, headers=custom_headers)
        soup = BeautifulSoup(html.text, "html.parser")

        url2 = pub_url + str(player_id) 
        html2 = requests.get(url2)
        soup2 = BeautifulSoup(html2.text, "html.parser")    

        pub_date = soup2.find_all('td')[8]  # Has the expiration date and the monthly supplement inside of it, which can be the second best solution
        date = extract_expiration_date(pub_date.text)  
        monthly_rating = extract_regular_rating(pub_date.text)

        # Extract required data from the HTML
        liverating0 = soup.find_all('td')
        lix = liverating0[5].text.replace("\n", "") 
        print(lix)
        liverating = soup.findChildren('table')
        li1 = liverating[6]
        rows = li1.findChildren(['th', 'tr'])[:6] 
        all_player_data.append([lix, f"Expiration Date: {date}", monthly_rating]) 
        for row in rows:
            cells = row.findChildren('td')
            row_data = [cell.text for cell in cells]
            all_player_data.append(row_data)
    all_player_data = tabulate(all_player_data, tablefmt="html") 
    return all_player_data 
 
view_players([14973111])