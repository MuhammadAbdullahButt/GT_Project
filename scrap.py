import requests
from bs4 import BeautifulSoup
import re

def scrape_web_pages(urls):
    all_text_data = []
    for url in urls:
        # Send a GET request to the URL
        headers = {"User-Agent": "Windows NT 10.0; Win64; x64"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text data from HTML
            text_data = soup.get_text()
            # Clean the text 
            text_data = re.sub(r'\s+', ' ', text_data)
            # Append the cleaned text data to the list
            all_text_data.append(text_data)
        else:
            print(f"Failed to fetch data from {url}")

    return all_text_data

#URLs to scrape data
urls = [    
            #science&education TRAIN DATA
            #"https://pgc.edu/importance-of-education-in-life/",
            #"https://www.vedantu.com/chemistry/importance-of-science",
            #"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4198034/",
            #"https://www.uopeople.edu/blog/10-reasons-why-is-education-important/",
            #"https://habitatbroward.org/blog/benefits-of-education/",
            #"https://medium.com/@tayyabtaimoor23/article-on-science-and-technology-3efd5b2b88b4",
            #"https://byjus.com/english/article-on-the-importance-of-education/",
            #"https://www.lilianefonds.org/project/inclusive-play-based-early-childhood-education-ipece?gad_source=1&gclid=CjwKCAjwxLKxBhA7EiwAXO0R0L0zlNRmgrO8E5yLFJld87wf-04RmAJhP2lgDHzQf2S-FlWsBKyURxoCt2oQAvD_BwE",
            #"https://www.windle.org.uk/views/beyond-enrolment?gad_source=1&gclid=CjwKCAjwxLKxBhA7EiwAXO0R0HEjsp1ID6btfn9tSsNVCbPYfM76vlG1asI0DTj65JpjtCAsNSyXFhoCllEQAvD_BwE",
            #"https://www.researchgate.net/publication/260075970_The_Importance_of_Education",
            #"https://leverageedu.com/blog/article-on-importance-of-education/",
            #"https://www.toppr.com/guides/essays/essay-on-education/",
          
           
            #science&education TEST DATA
           # "https://www.britannica.com/topic/education/Education-in-the-earliest-civilizations",
            # "https://en.wikipedia.org/wiki/Science",
            #"https://undsci.berkeley.edu/understanding-science-101/what-is-science/",

            #sports TRAIN DATA
            #"https://www.britannica.com/sports/sports",
            #"https://kids.britannica.com/students/article/sports/601225",
            #"https://www.britannica.com/sports/football-soccer",
            #"https://www.khaleejtimes.com/sports/waseem-hails-dp-world-ilt20-experience-for-helping-uae-to-qualify-for-asia-cup-2025",
            #"https://www.khaleejtimes.com/sports/ipl-2024-master-blasters-sunrisers-set-ipl-record-for-most-sixes-in-single-season",
            #"https://www.khaleejtimes.com/sports/cricket/india-not-everyone-happy-with-ipls-impact-player-rule",
            #"https://aerower.com/en/452",
            #"https://www.vedantu.com/english/importance-of-sports-essay",
            #"https://www.toppr.com/guides/essays/importance-of-sports/",
            #"https://daffodil.edu.np/sport-importance/",
            #"https://ihtusa.com/what-are-the-benefits-and-importance-of-sports-in-education/",
            #"https://www.linkedin.com/pulse/sports-its-importance-kanimozhi-thangaraj-rvipc",
            
            #sports TEST DATA
            #"https://digitalizetraining.com/importance-of-sports-essay-and-article/",
            #"https://www.vedantu.com/blog/importance-of-sports-in-a-students-life",
            #"https://www.muhealth.org/conditions-treatments/pediatrics/adolescent-medicine/benefits-of-sports",

            #disease&symptoms TRAIN DATA
            #"https://www.mayoclinic.org/diseases-conditions/heart-attack/symptoms-causes/syc-20373106",
            #"https://www.cdc.gov/heartdisease/heart_attack.htm",
            #"https://www.nhs.uk/conditions/heart-attack/",
            #"https://www.who.int/news/item/26-04-2024-statement-on-the-antigen-composition-of-covid-19-vaccines",
            #"https://en.wikipedia.org/wiki/COVID-19",
            #"https://lgh.punjab.gov.pk/Covid19Info",
            #"https://my.clevelandclinic.org/health/symptoms/10880-fever",
            #"https://www.webmd.com/first-aid/fevers-causes-symptoms-treatments",
            #"https://www.hopkinsmedicine.org/health/conditions-and-diseases/fever",
            #"https://en.wikipedia.org/wiki/Fever",
            #"https://www.cdc.gov/diabetes/basics/diabetes.html",
            #"https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes",
            
            #disease%symptoms TEST DATA
            # "https://www.britannica.com/science/disease",
            # "https://en.wikipedia.org/wiki/Disease",
            # "https://my.clevelandclinic.org/health/diseases/17724-infectious-diseases"
            
        ]

# Scrape text data from web pages
scraped_data = scrape_web_pages(urls)

# Save scraped data to a file
with open("sports_train_12.txt", "w", encoding="utf-8") as file:
    for data in scraped_data:
        file.write(data + "\n")
