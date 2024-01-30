import webbrowser
import sys

valid_sites =[
    'reddit.com',
    'medium.com',
    'stackoverflow.com',
    'w3schools.com',
    'geeksforgeeks.org',
    'youtube.com'
]

url= "https://www.google.com/search?q="
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 3" %s'
def add_Filter():
    filt = '('
    for index, site in enumerate(valid_sites):
        filt += 'site: '+site
        if index == len(valid_sites):
            filt+=')'
        else:
            filt+= ' OR '
    return filt

def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:]) ==0:
        print('Error: Enter a google search\n')
    else:
        finURL= url+create_query()+add_Filter()
        webbrowser.get(chrome_path).open_new(finURL)

create_url()
# webbrowser.get(chrome_path).open(url)

