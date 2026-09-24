# Raspberry Pi Supply Dashboard

A daily automated dashboard to track the prices and availability of various Raspberry Pi products across major suppliers (Adafruit, SparkFun, PiShop, DigiKey, Micro Center, Newark).

## Features
- Scrapes product prices and stock statuses
- Automatically generates a static `index.html` dashboard
- GitHub Actions workflow to update the dashboard daily
- Sortable table columns

## Usage
The dashboard is built automatically using GitHub Actions and can be served via GitHub Pages.

To run it locally:
```bash
pip install -r requirements.txt
python build_dashboard.py
```
