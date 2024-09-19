import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# def extract_expiration_date(input_string):
#     date_pattern = r"\d{4}-\d{2}-\d{2}"
#     matches = re.findall(date_pattern, input_string)
    
#     if matches:
#         return matches[-2] 
#     else:
#         return None  

# input_string = "Tournament directors should use the appropriate published rating unless otherwise announced... Expiration Dt.\n\n\n2023-12-31\n\n\n\nFIDE ID39921018 Latest FIDE RatingFIDE CountryUSA\n\n\nLast Change Dt.\n\n\n2023-07-04\n\n\nFor more information on norms-based titles, see The US Chess Title System For more information on the US Chess Rating System, see The US Chess Rating System To see who the most active chess players are, see the Leader Boards Frequently Asked Questions Latest US Chess JGP Standings634 points from 1 eventFor the latest unofficial top player JGP standings, see JGP Standings"
# expiration_date = extract_expiration_date(input_string)
# if expiration_date:
#     print(f"Expiration Date: {expiration_date}")
# else:
#     print("N/A or Non member")


pub_url = "https://www.uschess.org/msa/MbrDtlMain.php?"  
player_list = [14973111, 17143510]
for x in player_list:
    url2 = pub_url + str(x) 
    html2 = requests.get(url2)
    soup2 = BeautifulSoup(html2.text, "html.parser")  
    pub_date = soup2.find_all('td')[6]   
    #pub_date = soup2.find_all('td')[8]  # Has the expiration date and the monthly supplement inside of it, which can be the second best solution
    for _ in pub_date:
        print(_.text)
