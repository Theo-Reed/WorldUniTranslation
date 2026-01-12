import pandas as pd
import json
import os

def extract_universities():
    # Use absolute path or relative to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'China', 'China University List.xls')
    output_path = os.path.join(base_dir, 'China', 'china_universities.json')
    
    try:
        # Read the excel file. Based on inspection, headers are on the second row (index 1)
        df = pd.read_excel(file_path, header=1)
        
        # The school name is in the second column ('学校名称')
        # The school code is in the third column ('学校标识码')
        # Section headers (like provinces) have NaN in the code column
        school_name_col = df.columns[1]
        code_col = df.columns[2]
        
        # Filter rows that have a school code (actual universities)
        universities = df[df[code_col].notna()].copy()
        
        university_list = []
        for name in universities[school_name_col]:
            if isinstance(name, str) and name != '学校名称':
                university_list.append({
                    "chinese_name": name.strip(),
                    "english_name": ""
                })
        
        # Save to JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(university_list, f, ensure_ascii=False, indent=4)
            
        print(f"Successfully extracted {len(university_list)} universities to {output_path}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    extract_universities()
