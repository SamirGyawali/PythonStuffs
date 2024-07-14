from bs4 import BeautifulSoup
import requests

subject_urls = {
    'SE': ['https://hamrocsit.com/semester/sixth/se/question-bank/2080', 'https://hamrocsit.com/semester/sixth/se/question-bank/model-set-i/', 'https://hamrocsit.com/semester/sixth/se/question-bank/2076', 'https://hamrocsit.com/semester/sixth/se/question-bank/2079', 'https://hamrocsit.com/semester/sixth/se/question-bank/2077'],
    'EG': ['https://hamrocsit.com/semester/sixth/e-governance/question-bank/', 'https://hamrocsit.com/semester/sixth/e-governance/question-bank/2079', 'https://hamrocsit.com/semester/sixth/e-governance/question-bank/2078', 'https://hamrocsit.com/semester/sixth/e-governance/question-bank/2076'],
    'NCC': ['https://hamrocsit.com/semester/sixth/ncc/question-bank/', 'https://hamrocsit.com/semester/sixth/ncc/question-bank/2076', 'https://hamrocsit.com/semester/sixth/ncc/question-bank/2079', 'https://hamrocsit.com/semester/sixth/ncc/question-bank/2078'],
    'TW': ['https://hamrocsit.com/semester/sixth/tw/question-bank/', 'https://hamrocsit.com/semester/sixth/tw/question-bank/2074', 'https://hamrocsit.com/semester/sixth/tw/question-bank/2075', 'https://hamrocsit.com/semester/sixth/tw/question-bank/2079', 'https://hamrocsit.com/semester/sixth/tw/question-bank/2078'],
    'CDC': ['https://hamrocsit.com/semester/sixth/cdc/question-bank/', 'https://hamrocsit.com/semester/sixth/cdc/question-bank/2075', 'https://hamrocsit.com/semester/sixth/cdc/question-bank/2076', 'https://hamrocsit.com/semester/sixth/cdc/question-bank/2078'],
    'EC': ['https://hamrocsit.com/semester/sixth/e-commerce/question-bank/', 'https://hamrocsit.com/semester/sixth/e-commerce/question-bank/2078', 'https://hamrocsit.com/semester/sixth/e-commerce/question-bank/2076', 'https://hamrocsit.com/semester/sixth/e-commerce/question-bank/2079']
}


## FUTURE_NOTE: i know i know this function doesnot returns but i've assigned to the variable in line 74, i'm to lazy to fix this thanks to hemanta for helping me with this
## scrap the single page
def scrap_this(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml') ## why .content? to convert the source which is of raw bytes into text, BeautifulSoup() needs text format not raw format. i can also do .text at the end of request method to change it immediately into text

    date_div = soup.find('div', class_='syllabus_header')
    date = date_div.find_all('p')[-1].text

    subject_div = soup.find('div', class_='marks_header')
    subject = subject_div.find_all('p')[-1].text

    qsn_no = 0
    print()
    print(f"{date}")
    print()

    qsn_divs = soup.find_all('div', class_='qnbank_content')
    for div in qsn_divs:
        p_tag = div.find('p')
        if(p_tag):
            qsn = p_tag.text
            qsn_no+=1
            if(qsn_no <= 3):
                print(f"{qsn_no}. (10-marks) {qsn}")
            else:
                print(f"{qsn_no}. (5-marks) {qsn}")


def get_user_input():
    while True:
        try:
            user_input = int(input("Enter index of the subject: "))
            if(user_input>6):
                print("Enter valid index")
            else:
                return user_input
        except ValueError:
            print("Invalid input. please enter a valid integer")



print(f"list of subjects: 1.SE, 2.EG, 3.NCC, 4.TW, 5.CDC 6.EC\n"
      f" type 1, 2, 3 based on index of subject to scrap that subject")
user = get_user_input()

if(user == 1):
    urls_to_scrape = subject_urls['SE']
if(user == 2):
    urls_to_scrape = subject_urls['EG']
if(user == 3):
    urls_to_scrape = subject_urls['NCC']
if(user == 4):
    urls_to_scrape = subject_urls['TW']
if(user == 5):
    urls_to_scrape = subject_urls['CDC']
if(user == 6):
    urls_to_scrape = subject_urls['EC']

# print(urls_to_scrape)

## todo implement writing into file

for url in urls_to_scrape:
    scrap_this(url)
