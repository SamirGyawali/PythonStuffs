from bs4 import BeautifulSoup
import requests

source = requests.get('https://hamrocsit.com/semester/sixth/se/question-bank/').text
soup = BeautifulSoup(source, 'lxml')

date_div = soup.find('div', class_='syllabus_header')
date = date_div.find_all('p')[-1].text

subject_div = soup.find('div', class_='marks_header')
subject = subject_div.find_all('p')[-1].text


qsn_no = 0;
print(f"{date} {subject}")
print()


qsn_divs = soup.find_all('div', class_='qnbank_content')


for div in qsn_divs:
    p_tag = div.find('p')
    if(p_tag):
        qsn = p_tag.text
        qsn_no+=1
        if(qsn_no <= 3):
            print(f"{qsn_no}. (10-Marks) {qsn}")
        else:
            print(f"{qsn_no}. (5-Marks) {qsn}")