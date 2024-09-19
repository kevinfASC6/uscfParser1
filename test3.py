import re

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

# Example usage:
input_text = """
Tournament directors should use the appropriate published rating unless otherwise announced in all pre-tournament publicity.
For events that begin prior to August 1st, the July supplement should be used.
The ratings shown on this page are official published ratings, which US Chess issues 12 times a year.  As of September 1, 2013, Official ratings lists are generated on the 3rd Wednesday of each month and become official on the 1st day of the next month.  For unofficial rating information from recently rated events, see the 'Tnmt Hst' tab.
Current PublishedRating ( Supplement)
Published Ratingas of 2023-08-01


Regular Rating



1618  
2023-07(Current floor is 1400)



1548



Quick Rating



1544  
2023-07


1456



Blitz Rating



1511 (Based on 18 games)  
2023-07


1511 (Based on 18 games)


Online-Regular Rating



(Unrated)  



(Unrated)



Online-Quick Rating



(Unrated)  



(Unrated)



Online-Blitz Rating



(Unrated)  



(Unrated)

Last Rated Event: 202307285472 IMPACTCOACHINGNETWORK.ORG MARSHALL SUMMER CAMP #4 Rated on 2023-07-29
National and State RankingsCurrent RankingRank as of  2023-08-01
PercentileOverall Ranking10461(Tied) out of 7192985.5Junior Ranking3250(Tied) out of 5189693.8State Ranking (NY)1059(Tied) out of 726585.5Note:  Only current or recent members who have played within the past year are ranked. See Frequent Questions.
Show Ratings History Graphs
Show Game Statistics



Correspondence Rating



(Unrated)




State



NY 




Gender



M 





Expiration Dt.


2024-03-31





FIDE ID39921000   Latest FIDE RatingFIDE CountryUSA


Last Change Dt.


2023-07-28


For more information on norms-based titles, see The US Chess Title System
For more information on the US Chess Rating System, see The US Chess Rating System
To see who the most active chess players are, see the
Leader Boards
Frequently Asked Questions

"""

regular_rating, rating_date, floor_rating = extract_regular_rating(input_text)

if regular_rating:
    print(f"Regular Rating: {regular_rating}")
    print(f"Rating Date: {rating_date}")
    print(f"Floor Rating: {floor_rating}")
else:
    print("Regular rating not found in the input text.")
