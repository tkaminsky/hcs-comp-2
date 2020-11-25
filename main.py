import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.harvard.com/shelves/featured_holiday/"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
bookshelf = soup.find(class_="books")
books = list(bookshelf.find_all('li'))
books.pop(0)

titles = []

for x in books:
    y = x.find('h2')
    if y != None:
        titles.append(y.find('a').get_text())

for i in range(len(titles)):
    print(str(i + 1) + ". " + titles[i])
