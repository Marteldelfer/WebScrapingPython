from bs4 import BeautifulSoup;

with open("./localScraping/home.html", "r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        
        course_name = course.h5.text
        course_price = course.a.text

        print(f'{course_name} course costs: {course_price.split()[-1]}')