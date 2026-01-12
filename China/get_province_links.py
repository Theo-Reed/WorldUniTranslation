import requests
from bs4 import BeautifulSoup
import json
import os

def get_province_links():
    url = "https://en.wikipedia.org/wiki/List_of_universities_and_colleges_in_China"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    province_links = []
    
    # The links are under sections like "Municipalities", "Provinces", "Autonomous regions", and "Outside mainland China"
    # Looking at the HTML structure from fetch_webpage, they are bullet points
    
    # We want to find the section "List by regions"
    list_by_regions = soup.find('span', {'id': 'List_by_regions'})
    if not list_by_regions:
        # Try header
        list_by_regions = soup.find(lambda tag: tag.name == "h2" and "List by regions" in tag.text)
        
    if list_by_regions:
        # Find all following siblings until the next h2
        current = list_by_regions.parent
        found_links = False
        while current:
            current = current.find_next_sibling()
            if not current or current.name == 'h2':
                break
            
            # Look for <ul> and <li>
            for li in current.find_all('li'):
                a = li.find('a')
                if a and a.get('href') and a['href'].startswith('/wiki/List_of_universities_and_colleges_in_'):
                    full_url = "https://en.wikipedia.org" + a['href']
                    province_links.append(full_url)
    
    # Deduplicate and maintain order
    unique_links = []
    for link in province_links:
        if link not in unique_links:
            unique_links.append(link)
    
    # Range check as requested: Beijing to Macau
    # Let's see if we have them
    start_index = -1
    end_index = -1
    for i, link in enumerate(unique_links):
        if "Beijing" in link:
            start_index = i
        if "Macau" in link:
            end_index = i
            
    if start_index != -1 and end_index != -1:
        # Ensure we include everything from Beijing to Macau
        final_list = unique_links[start_index:end_index+1]
    else:
        final_list = unique_links
        
    # Save to a file for reference
    output_path = os.path.join('China', 'province_links.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_list, f, ensure_ascii=False, indent=4)
        
    print(f"Found {len(final_list)} province links.")
    for link in final_list:
        print(link)

if __name__ == "__main__":
    get_province_links()
