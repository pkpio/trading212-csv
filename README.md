# trading212-csv
Converts Trading 212 CSV files to different formats such Yahoo Finance CSV

# Setup
- Copy `config.ini.sample` to `config.ini`
- Export CSV files from Trading212 app 
  - Download them to `input` folder
  - You can export and download multiple files
  - Overlapping dates are okay

# Usage
Just run `python3 main.py`

# Manual symbol mapping
Trading 212 and Yahoo Finance use different tickers / symbols for some equities. This will affect if you have any European equities in your trades. If there's an issue, the script will tell you to manually map the required tickers.
- For example, `VEUR needs manual mapping!`
- You need to manually find the ticker for this on Yahoo Finance (`VEUR.AS`)
- Add a line mapping them at the end of the `config.ini` file (`VEUR=VEUR.AS`)

**Star the repo to show support**
