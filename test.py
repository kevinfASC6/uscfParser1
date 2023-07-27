# import math
 
# def egyptianFraction(nr, dr):
#     print("The Egyptian Fraction " + "Representation of {}/{} is".format(nr, dr)) 
#     ef = []

#     while nr != 0:
#         x = math.ceil(dr / nr)
#         ef.append(x)
#         nr = x * nr - dr
#         dr = dr * x
 
#     for i in range(len(ef)):
#         if i != len(ef) - 1:
#             print(" 1/{} +" .format(ef[i]), end = " ")
#         else:
#             print(" 1/{}" .format(ef[i]), end = " ")

# def main(): 
#     egyptianFraction(4,13)
# if __name__ == "__main__": 
#     main() 

import requests
from bs4 import BeautifulSoup

# Define your custom_headers here if not provided in the code

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
        all_player_data.append(lix) 
        for row in rows:
            cells = row.findChildren('td')
            row_data = [cell.text for cell in cells]
            all_player_data.append(row_data)

    return lix, all_player_data 


def main(): 
    id_list = [17143510, 14973111]
    print(view_players(id_list)) 
if __name__ == "__main__": 
    main()

# import pandas as pd

# # Sample data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 22, 28],
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
# }

# # Creating the DataFrame
# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)





