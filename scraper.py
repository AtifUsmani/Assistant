from selenium import webdriver


def youtube():
    browser = webdriver.Chrome()
    browser.get('https://www.youtube.com/')


def YT_music():
    browser = webdriver.Chrome()
    browser.get('https://music.youtube.com/')


def Github():
    browser = webdriver.Chrome()
    browser.get('https://github.com/AtifUsmani/Assistant')
