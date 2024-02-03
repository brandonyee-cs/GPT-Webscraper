import requests
from bs4 import *
from openai import OpenAI
import config #This is your own config file that contains your API key.

ai = OpenAI(api_key = config.openai_apikey) #config.openai_apikey is a variable imported from my config file.

url = input('Enter Website URL: ')
prompt = input('[==] ')

def scrapSite(url, prompt): #Pull information from the website
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator='\n', strip = True)
        print(text)
    else:
        print(f"Failed to access website. Status code: {response.status_code}") #For error recovery

def searchSite(website, prompt):
    print('generating...')
    completion = ai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {'role': 'system', 'content': f"You are going to analyze a website's content and search for {prompt}"},
            {'role': 'user', 'contet': f"This is the text content of the website: {website}. Follow these instructions {prompt} and print what you find."}
        ]
    )
    searchResult = completion.choices[0].message.content
    print(f"Search Results: {searchResult}")

searchSite(url,prompt)