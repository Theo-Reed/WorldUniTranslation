import requests
from bs4 import BeautifulSoup
import json
import os
import re
from opencc import OpenCC

cc = OpenCC('t2s')

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'\[[a-z]{2}\]', '', text)
    return text.strip()

def normalize(name):
    return re.sub(r'[\s\(\)（）]', '', name)

def update_macau():
    url = "https://en.wikipedia.org/wiki/List_of_universities_and_colleges_in_Macau"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'china_universities.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        universities = json.load(f)
    uni_map = {normalize(u['chinese_name']): i for i, u in enumerate(universities)}
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print(f"Fetching {url}...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    
    added = 0
    matched = 0
    
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all(['td', 'th'])
            if len(cols) >= 3:
                # English, Portuguese, Chinese
                eng_name = clean_text(cols[0].get_text())
                chi_name = cc.convert(clean_text(cols[2].get_text()))
                
                if not eng_name or not chi_name: continue
                
                norm_chi = normalize(chi_name)
                if norm_chi in uni_map:
                    idx = uni_map[norm_chi]
                    if not universities[idx]['english_name']:
                        universities[idx]['english_name'] = eng_name
                        matched += 1
                else:
                    universities.append({
                        "chinese_name": chi_name,
                        "english_name": eng_name
                    })
                    uni_map[norm_chi] = len(universities) - 1
                    added += 1
                    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(universities, f, ensure_ascii=False, indent=4)
        
    print(f"Macau: Matched {matched}, Added {added}")

if __name__ == "__main__":
    update_macau()
