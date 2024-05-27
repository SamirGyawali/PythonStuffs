from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_card = soup.find_all('div', class_='card')
    for course in course_card:
        course_name = course.h5.text
        course_price = course.a

        print(course_name)
        print(course_price)