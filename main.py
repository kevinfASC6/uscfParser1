import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# def write_info_to_csv(ids, filename):
#     base_url = "https://www.uschess.org/msa/MbrDtlTnmtHst.php?"
#     with open(filename, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         for id in ids:
#             url = base_url + str(id)
#             html = requests.get(url)
#             soup = BeautifulSoup(html.text, "html.parser") 
#             liverating0 = soup.find_all('td')  
#             lix = liverating0[5]

#             liverating = soup.findChildren('table')
#             li1 = liverating[6]
#             rows = li1.findChildren(['th', 'tr'])[:6]

#             writer.writerow([lix.text])  # Write the liverating0 value to CSV

#             for row in rows:
#                 cells = row.findChildren('td')
#                 row_data = [cell.text for cell in cells]
#                 writer.writerow(row_data)  # Write the row data to CSV

#             writer.writerow([])  # Add an empty row in CSV for separation

# id_list = [17143510, 14973111, 148002058]
# output_filename = 'player_info.csv'

# write_info_to_csv(id_list, output_filename) 


def view_players(ids):
    base_url = "https://www.uschess.org/msa/MbrDtlTnmtHst.php?"
    all_player_data = []  # To store information for all players

    for player_id in ids:
        url = base_url + str(player_id)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        # Extract required data from the HTML
        liverating0 = soup.find_all('td')
        lix = liverating0[5].text.replace("\n", "")
        liverating = soup.findChildren('table')
        li1 = liverating[6]
        rows = li1.findChildren(['th', 'tr'])[:6] 
        print(all_player_data)
        for row in rows:
            cells = row.findChildren('td')
            row_data = [cell.text for cell in cells]
            all_player_data.append(row_data)
    all_player_data = tabulate(all_player_data, tablefmt="html")
    return lix, all_player_data 

def main(): 
    print(view_players([14973111]))
if __name__ == "__main__": 
    main()


