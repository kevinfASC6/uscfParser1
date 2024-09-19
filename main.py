import csv 
import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate 

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

def write_info_to_csv(ids, filename):
    base_url = "https://www.uschess.org/msa/MbrDtlTnmtHst.php?" 
    pub_url = "https://www.uschess.org/msa/MbrDtlMain.php?" 
    all_player_data = []
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for id in ids:
            url = base_url + str(id)
            html = requests.get(url)
            soup = BeautifulSoup(html.text, "html.parser") 

            url2 = pub_url + str(id) 
            html2 = requests.get(url2)
            soup2 = BeautifulSoup(html2.text, "html.parser")  
            pub_date = soup2.find_all('td')[8] 
            date = extract_expiration_date(pub_date.text) 
            monthly_rating = extract_regular_rating(pub_date.text)  
            liverating0 = soup.find_all('td')  
            lix = liverating0[5].text.replace("\n", "") 
            writer.writerow([lix, f"Expiration Date: {date}", monthly_rating])  # Write the liverating0 value to CSV 
            writer.writerow([])  # Add an empty row in CSV for separation 
            

id_list = [16915550,
30886275,
30886136,
30893859,
30730210,
31325596,
31516687,
31537134,
30891615,
30233678,

]
output_filename = 'player_info.csv'

print(write_info_to_csv(id_list, output_filename))


# def view_players(ids):
#     base_url = "https://www.uschess.org/msa/MbrDtlTnmtHst.php?"
#     all_player_data = []  # To store information for all players

#     for player_id in ids:
#         url = base_url + str(player_id)
#         html = requests.get(url)
#         soup = BeautifulSoup(html.text, "html.parser")

#         # Extract required data from the HTML
#         liverating0 = soup.find_all('td')
#         lix = liverating0[5].text.replace("\n", "")
#         liverating = soup.findChildren('table')
#         li1 = liverating[6]
#         rows = li1.findChildren(['th', 'tr'])[:6] 
#         print(all_player_data)
#         for row in rows:
#             cells = row.findChildren('td')
#             row_data = [cell.text for cell in cells]
#             all_player_data.append(row_data)
#     all_player_data = tabulate(all_player_data, tablefmt="html")
#     return lix, all_player_data 

# def main(): 
#     print(view_players([14973111]))
# if __name__ == "__main__": 
#     main()


