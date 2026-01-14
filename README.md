# Global Universities List

A comprehensive database of universities worldwide, providing standardized **English** and **Chinese** names for each institution.

[中文版](./README_CN.md)

## Project Overview

This project maintains a curated list of higher education institutions globally. It serves as a centralized database where every university entry includes:
- **_id**: A unique identifier.
- **Chinese Name**: The official name in Simplified Chinese.
- **English Name**: The standardized international English name (translated/verified via AI).
- **Country**: The country name in both Chinese and English.

**Total Records:** ~10,300+ entries across 100+ countries.

## 🚀 Quick Start

The entire project is managed by a single unified script: `main.py`.

### Prerequisites
1.  Python 3.8+
2.  Install dependencies:
    ```bash
    pip install pandas google-genai python-dotenv
    ```
3.  Set up your `.env` file in the `scripts/` directory with your Gemini API key:
    ```env
    # scripts/.env
    GEMINI_API_KEY=your_api_key_here
    ```

### Usage
Run the project manager script to normalize data, translate missing names, and generate the final summary:

```bash
python3 main.py
```

This script performs three main tasks:
1.  **Normalize**: Standardizes CSV headers and cleans up formatting in every country folder.
2.  **Translate**: Scans for non-English names (e.g., French, Spanish, Russian) and uses **Gemini 2.0 Flash** to translating them into standard English.
3.  **Summarize**: Aggregates all country data into the master file `world_universities.csv`.

## 📂 Project Structure

Data is organized by country within the `data/` directory. Configuration and utility scripts are located in `scripts/`.

```
.
├── main.py                     # The core management script
├── world_universities.csv      # The final output (Master Database)
├── README.md                   # English documentation
├── README_CN.md                # Chinese documentation
├── data/                       # Raw and cleaned data
│   ├── China/                  # Special handling for China data
│   ├── USA/                    # USA data
│   └── ...                     # Other countries
└── scripts/                    # Configuration and utilities
    ├── .env                    # Environment variables (API Key)
    ├── ssl_adapter.py          # Network utility
    └── openssl_legacy.cnf      # SSL configuration
```

## ✨ Key Features

- **Automated AI Translation**: Uses the Gemini API to detect non-English names (e.g., "Université de Paris" or "東京大学") and translates them to their official English equivalents.
- **Strict English Validation**: Enforces "English-only" names in the final output. Terms like *Universidad*, *Ecole*, *Hochschule* are automatically flagged and translated.
- **Data Standardization**: Automatically cleans headers, removes duplicate columns, and fixes common formatting issues (e.g., smart quotes, extra spaces).
- **Regions**: Special handling for **Hong Kong**, **Macau**, and **Taiwan** to ensure correct formatting in the global list.

## Data Sources
- **China**: Collected via specific scrapers (retained in `data/China/` folder).
- **Global**: A compilation from various official lists, standardized into a uniform format.

## License
MIT
