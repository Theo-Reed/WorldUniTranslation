import json
import csv
import os
import sys
import pandas as pd

# Add root to path to import gemini_translator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gemini_translator import GeminiTranslator

def main():
    csv_path = os.path.join(os.path.dirname(__file__), "china_universities.csv")
    
    if not os.path.exists(csv_path):
        print(f"CSV not found at {csv_path}")
        return

    print(f"Reading {csv_path}...")
    df = pd.read_csv(csv_path, encoding='utf-8-sig')
    
    # Identify missing names
    missing_mask = df['english_name'].isna() | (df['english_name'].astype(str).str.strip() == "") | (df['english_name'].astype(str).str.lower() == "nan")
    to_translate_df = df[missing_mask]
    
    if to_translate_df.empty:
        print("No missing English names found in China university list.")
        return

    print(f"Found {len(to_translate_df)} universities with missing English names. Translating via Gemini...")
    
    translator = GeminiTranslator()
    batch_size = 50
    
    # Prepare data for translator
    # We pass chinese_name as both to emphasize it's the source
    raw_data = [
        {"chinese_name": row['chinese_name'], "original_name": row['chinese_name']}
        for _, row in to_translate_df.iterrows()
    ]

    for i in range(0, len(raw_data), batch_size):
        batch = raw_data[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1}/{(len(raw_data)-1)//batch_size + 1}...")
        
        # Using country="China" and language="Chinese"
        translated_batch = translator.translate_university_names(batch, country="China", language="Chinese")
        
        # Update the main dataframe
        for item in translated_batch:
            cname = item.get('chinese_name')
            ename = str(item.get('english_name', '')).strip()
            
            # Clean wrapping quotes and internal quotes
            if ename.startswith('"') and ename.endswith('"'):
                ename = ename[1:-1].strip()
            ename = ename.replace('"', "'").replace(',', ' ')
            
            if ename:
                df.loc[df['chinese_name'] == cname, 'english_name'] = ename
        
        # Save after each batch
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"Batch saved. Remaining missing: {len(df[df['english_name'].isna() | (df['english_name'].astype(str).str.strip() == '')])}")

    print(f"Successfully finished updating missing names in {csv_path}")

if __name__ == "__main__":
    main()
