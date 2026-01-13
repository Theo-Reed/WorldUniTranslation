# Global Universities List

A comprehensive database of universities worldwide, providing standardized **English** and **Chinese** names for each institution.

## Project Goal
The objective of this project is to consolidate a complete list of higher education institutions globally. For every university, we provide:
- **_id**: A unique identifier for the combined list.
- **Chinese Name**: Official simplified Chinese name.
- **English Name**: Standard international name, cleaned for CSV compatibility.
- **Country**: The country where the institution is located.

## Data Structure
The project is organized by region/country folders:

- `world_universities.csv`: The master consolidated list of all universities.
- `China/`: Mainland China, Hong Kong, Macau, and Taiwan records. Missing English names are filled using AI translation.
- `Japan/`: Data for Japanese institutions, translated from Japanese originals.
- `Poland/`: Data for Polish institutions, translated from Polish originals.
- `Egypt/`: Data for Egyptian institutions.

## Features & Automation
- **AI-Powered Translation**: Uses **Gemini 2.0 Flash** to provide official international English names based on original language names (Polish, Japanese, etc.) or Chinese context.
- **Incremental Updates**: Scripts track existing records to avoid redundant API calls and save costs.
- **Data Cleaning**: 
    - Automatically removes wrapping double quotes around names.
    - Replaces internal double quotes with single quotes.
    - Replaces commas with spaces in English names to ensure clean CSV formatting without escaping issues.
- **Master Summary**: A central script aggregates all regional CSVs into the root database with unique IDs.

## Summary Generation
To update the global summary file:
```bash
python generate_summary.py
```

## Current Progress
- [x] **China**: 3000 records (including HK/Macau/Taiwan).
- [x] **Japan**: 959 records, Gemini-translated from Japanese.
- [x] **Poland**: 88 records, Gemini-translated from Polish.
- [x] **Egypt**: 28 records.
- [ ] **USA**: Planned.
- [ ] **Europe**: Planned.

## Technical Stack
- **Python 3**: Core processing.
- **Pandas**: Data manipulation and CSV management.
- **Gemini 2.0 Flash**: Academic-grade translation and entity mapping.
- **Requests / Curl**: Official API interactions.
- **python-dotenv**: Secure environment variable management.

## Setup & Usage
1. **API Key**: Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_key_here
   ```
2. **Install Dependencies**:
   ```bash
   pip install pandas google-generativeai python-dotenv requests
   ```
3. **Run Update Scripts**:
   ```bash
   python Poland/update_poland_universities.py
   python Japan/update_japan_universities.py
   ```

## Storage Format
- Encoding: `UTF-8 with BOM` for Excel compatibility.
- Normalized column names (`_id`, `chinese_name`, `english_name`, `country`).
