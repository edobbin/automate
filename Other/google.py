import sys
import webbrowser

url= "https://www.google.com/search?q="
chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 3" %s'


def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:]) ==0:
        print('Error: Enter a google search\n')
    else:
        finURL= url+create_query()
        webbrowser.get(chrome_path).open_new(finURL)

create_url()