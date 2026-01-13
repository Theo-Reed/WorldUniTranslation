import json
import csv
import os
import subprocess

def fetch_egypt_universities():
    url = "https://yxcx.cscse.edu.cn/api/xlxwrzz/xlxwrz/getUniversityListOrPage"
    payload = {
        "country": "埃及",
        "currentPage": 1,
        "pageSize": 100,
        "universityIndex": ""
    }
    
    curl_command = [
        "curl", "-s", "-X", "POST", url,
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ]
    
    try:
        process = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        result = json.loads(process.stdout)
        
        data = result.get("data", [])
        
        csv_path = os.path.join(os.path.dirname(__file__), "egypt_universities.csv")
        
        with open(csv_path, mode='w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Chinese Name", "English Name"])
            for item in data:
                writer.writerow([item.get("CHINESE_NAME"), item.get("ENGLISH_NAME")])
        
        print(f"Successfully saved {len(data)} universities to {csv_path}")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_egypt_universities()

if __name__ == "__main__":
    fetch_egypt_universities()
