import json
import os
from opencc import OpenCC

cc = OpenCC('t2s')

def fix_json():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'china_universities.json')
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        universities = json.load(f)

    print(f"Processing {len(universities)} universities...")
    
    changed_count = 0
    for i, uni in enumerate(universities):
        original_name = uni['chinese_name']
        simplified_name = cc.convert(original_name)
        if original_name != simplified_name:
            uni['chinese_name'] = simplified_name
            changed_count += 1
            if changed_count < 10:
                print(f"Converted: {original_name} -> {simplified_name}")

    if changed_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(universities, f, ensure_ascii=False, indent=4)
        print(f"Total changes made: {changed_count}")
    else:
        print("No changes needed. All names are already Simplified.")

if __name__ == "__main__":
    fix_json()
