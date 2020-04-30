"""
Created on Sun Apr 12 20:19:26 2020

@author: DUDO3
"""

import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.worldometers.info',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.worldometers.info/world-population/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'fsbotchecked=true; __cfduid=dbda2437de98a5a1cbf1f259c388779a21586119756; _ga=GA1.2.1735871553.1586119758; _fsuid=c6bcf27c-e820-42d7-be57-9132a4d24d9e; _fsloc=?i=IE^&c=Wicklow; __beaconTrackerID=7yqrdca9t; __qca=P0-1154466923-1586119758896; __gads=ID=38e140c039bb8656:T=1586119759:S=ALNI_MZkV-isjqMEjtQzShchMHACec8tHA; _gid=GA1.2.1228020505.1587333002; _fssid=ddaaf46a-db9d-478f-9301-5b2f783242dc; fssts=false; __atuvc=5^%^7C15^%^2C0^%^7C16^%^2C4^%^7C17; __atuvs=5e9cc78a508d512d003',
}

def get_page_contents():
    response = requests.get('https://www.worldometers.info/world-population/population-by-country/', headers=headers)
    return response.content

# parsing the HTML content with BeautifulSoup
def convert_to_soup(content):
    return BeautifulSoup(content, 'html.parser')

# getting the full table from webpage I'll be parsing
def get_table(soup):
    return soup.find("table")

# getting the table with all the headers/table titles
def get_headers(table):
    headers = []
    # only interested in 'tr' from table head to get headers
    for table_head in table.thead.find_all("tr"):
        cells = table_head.find_all("th")
        for cell in cells:
            # removing all n/a and spaces from numbers with % sign
            headers.append('"' + cell.text.replace("N.A.", "0").replace(" %", "%") + '"')
        return headers

# find all table rows
def get_rows(table):
    rows = []
    # only interested in 'tr' from table body
    for table_row in table.tbody.find_all("tr"):
        columns = table_row.find_all("td")
        row = []
        for column in columns:
            row.append('"' + column.text.replace("N.A.", "0").replace(" %", "%") + '"')
        rows.append(row)
    return rows

def main():
    contents = get_page_contents()
    soup = convert_to_soup(contents)
    table = get_table(soup)
    print((','.join(get_headers(table))).replace('," ",', ',"0",'))
    for rows in get_rows(table):
        print(','.join(rows).replace('," ",', ',"0",'))

if __name__ == '__main__':
    main()

