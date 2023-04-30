from pages.quotes_page import QuotesPage, InvalidTagForAuthorError, InvalidAuthorNameError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    service = Service("chromedriver.exe")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(service=service, options=chrome_options)
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidAuthorNameError as e:
    chrome.close()
    print(e)
except InvalidTagForAuthorError as e:
    chrome.close()
    print(e)
except Exception as e:
    chrome.close()
    print(e)
