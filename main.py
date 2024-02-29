"""
I will take the first 49 pages of AirPods reviews on Walmart, 
including both 1-star and 5-star ratings, and save them in a text file. Then, 
I will use the reviews from page 50 of both 1-star and 5-star ratings for testing
the machine learning model. Alternatively, I may use reviews of other technology products.


The script needs to be run twice, each time collecting both the positive and negative reviews.
"""

import requests
from requests_html import HTMLSession #you need to do pip install requests-html


repeatedReview1 = "I washed my previous AirPods and needed a new pair ASAP! Upon searching I found this bundle which included the AirPods and an Airtag which I've been wanting for one low price. Easy ordering process and I received my items the very next day as scheduled. My items were new, packaged and exactly what I wanted."
repeatedReview2 = "The package was open and the headphones are not second generation, they are from the first. This is not my first time buying them and the last time i bought they were perfectly fine their for i trusted that this time it would be the same yet the airpods inside are first gen and the case saids its 2."


counterOfReviews = 0
myList = []
for i in range(1, 50):
    
    url = "https://www.walmart.com/reviews/product/604342441?filter=5&page=" + str(i)
    session = HTMLSession()
    reponse = session.get(url)
    
    myList.clear()
    myList = reponse.html.find("span.tl-m.mb3.db-m")

    with open("positive.txt", "a", encoding="utf-8") as file: #change the name of the txt.file to negative or positive
        for i in myList:
             
             if i.text == repeatedReview1 or i.text == repeatedReview2:
                 continue
             else:
                 file.write(i.text + "\n")
                 counterOfReviews = counterOfReviews + 1
                 file.write("\n")


print("done with the script")
print("counter of reviews", counterOfReviews)
    




   
    