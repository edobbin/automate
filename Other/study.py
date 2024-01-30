import webbrowser
import time
from selenium import *

# def isBrowserOpen(driver)

site=[
    'leetcode.com',
    'youtube.com',
    'google.com',
    'chat.openai.com'
]

chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 1" %s'

WB = webbrowser.get(chrome_path)
for s in site:
    webbrowser.get(chrome_path).open(s)
    

