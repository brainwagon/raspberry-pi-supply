import requests
from bs4 import BeautifulSoup
import datetime

PRODUCTS = [
    {
        "name": "Raspberry Pi 5 8GB",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/5813",
    },
    {
        "name": "Raspberry Pi 5 4GB",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/5812",
    },
    {
        "name": "Raspberry Pi 4 4GB",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/4296",
    },
    {
        "name": "Raspberry Pi Zero 2 W",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/5291",
    },
    {
        "name": "Raspberry Pi 5 8GB",
        "supplier": "SparkFun",
        "url": "https://www.sparkfun.com/products/23551",
    },
    {
        "name": "Raspberry Pi 5 4GB",
        "supplier": "SparkFun",
        "url": "https://www.sparkfun.com/products/23550",
    },
    {
        "name": "Raspberry Pi 5 8GB",
        "supplier": "PiShop",
        "url": "https://www.pishop.us/product/raspberry-pi-5-8gb/",
    },
    {
        "name": "Raspberry Pi 5 4GB",
        "supplier": "PiShop",
        "url": "https://www.pishop.us/product/raspberry-pi-5-4gb/",
    },
    {
        "name": "Raspberry Pi 5 8GB",
        "supplier": "DigiKey",
        "url": "https://www.digikey.com/en/products/detail/raspberry-pi/SC1112/21267073",
    },
    {
        "name": "Raspberry Pi 5 8GB",
        "supplier": "Micro Center",
        "url": "https://www.microcenter.com/search/search_results.aspx?Ntt=raspberry+pi+5+8gb",
    },
    {
        "name": "Raspberry Pi 5 8GB",
        "supplier": "Newark",
        "url": "https://www.newark.com/c/embedded-computers-education-maker-boards/raspberry-pi/raspberry-pi-5-model-b",
    },
    {
        "name": "Raspberry Pi Zero 2 W",
        "supplier": "SparkFun",
        "url": "https://www.sparkfun.com/products/18713",
    },
    {
        "name": "Raspberry Pi Zero 2 W",
        "supplier": "PiShop",
        "url": "https://www.pishop.us/product/raspberry-pi-zero-2-w/",
    },
    {
        "name": "Raspberry Pi Zero 2 W",
        "supplier": "DigiKey",
        "url": "https://www.digikey.com/en/products/filter/raspberry-pi-zero-2-w",
    },
    {
        "name": "Raspberry Pi Zero 2 W",
        "supplier": "Micro Center",
        "url": "https://www.microcenter.com/search/search_results.aspx?Ntt=raspberry+pi+zero+2+w",
    },
    {
        "name": "Raspberry Pi Zero 2 W",
        "supplier": "Newark",
        "url": "https://www.newark.com/c/embedded-computers-education-maker-boards/raspberry-pi/raspberry-pi-zero-2-w",
    },
    {
        "name": "Raspberry Pi Pico",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/4864",
    },
    {
        "name": "Raspberry Pi Pico W",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/5526",
    },
    {
        "name": "Raspberry Pi Pico",
        "supplier": "SparkFun",
        "url": "https://www.sparkfun.com/products/17829",
    },
    {
        "name": "Raspberry Pi Pico W",
        "supplier": "SparkFun",
        "url": "https://www.sparkfun.com/products/20173",
    },
    {
        "name": "Raspberry Pi Pico",
        "supplier": "PiShop",
        "url": "https://www.pishop.us/product/raspberry-pi-pico/",
    },
    {
        "name": "Raspberry Pi Pico W",
        "supplier": "PiShop",
        "url": "https://www.pishop.us/product/raspberry-pi-pico-w/",
    },
    {
        "name": "Raspberry Pi Pico",
        "supplier": "DigiKey",
        "url": "https://www.digikey.com/en/products/filter/raspberry-pi-pico",
    },
    {
        "name": "Raspberry Pi Pico W",
        "supplier": "DigiKey",
        "url": "https://www.digikey.com/en/products/filter/raspberry-pi-pico-w",
    },
    {
        "name": "Raspberry Pi Pico",
        "supplier": "Micro Center",
        "url": "https://www.microcenter.com/search/search_results.aspx?Ntt=raspberry+pi+pico",
    },
    {
        "name": "Raspberry Pi Pico W",
        "supplier": "Micro Center",
        "url": "https://www.microcenter.com/search/search_results.aspx?Ntt=raspberry+pi+pico+w",
    },
    {
        "name": "Raspberry Pi Pico",
        "supplier": "Newark",
        "url": "https://www.newark.com/c/embedded-computers-education-maker-boards/raspberry-pi/raspberry-pi-pico",
    },
    {
        "name": "Raspberry Pi Pico W",
        "supplier": "Newark",
        "url": "https://www.newark.com/c/embedded-computers-education-maker-boards/raspberry-pi/raspberry-pi-pico-w",
    },
    {
        "name": "Raspberry Pi Pico 2 W",
        "supplier": "Adafruit",
        "url": "https://www.adafruit.com/product/6000",
    },
    {
        "name": "Raspberry Pi Pico 2 W",
        "supplier": "SparkFun",
        "url": "https://www.sparkfun.com/products/26356",
    },
    {
        "name": "Raspberry Pi Pico 2 W",
        "supplier": "PiShop",
        "url": "https://www.pishop.us/product/raspberry-pi-pico-2-w/",
    },
    {
        "name": "Raspberry Pi Pico 2 W",
        "supplier": "DigiKey",
        "url": "https://www.digikey.com/en/products/filter/raspberry-pi-pico-2-w",
    },
    {
        "name": "Raspberry Pi Pico 2 W",
        "supplier": "Micro Center",
        "url": "https://www.microcenter.com/search/search_results.aspx?Ntt=raspberry+pi+pico+2+w",
    },
    {
        "name": "Raspberry Pi Pico 2 W",
        "supplier": "Newark",
        "url": "https://www.newark.com/c/embedded-computers-education-maker-boards/raspberry-pi/raspberry-pi-pico-2-w",
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_adafruit(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        price_elem = soup.find('span', itemprop='price')
        price = price_elem.text.strip() if price_elem else "Unknown"
        
        stock = "Unknown"
        if "Out of stock" in response.text or "OUT OF STOCK" in response.text:
            stock = "Out of Stock"
        elif "In stock" in response.text or "IN STOCK" in response.text:
            stock = "In Stock"
            
        return {"price": price, "stock": stock}
    except Exception as e:
        return {"price": "Error", "stock": "Error"}

def scrape_sparkfun(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        price_elem = soup.find('meta', property='product:price:amount')
        price = f"${price_elem['content']}" if price_elem else "Unknown"
        
        stock = "Unknown"
        if "Out of stock" in response.text or "Out of Stock" in response.text:
            stock = "Out of Stock"
        elif "In stock" in response.text or "In Stock" in response.text:
            stock = "In Stock"
            
        return {"price": price, "stock": stock}
    except Exception as e:
        return {"price": "Error", "stock": "Error"}

def scrape_pishop(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        price_elem = soup.find('span', class_='price--withoutTax')
        price = price_elem.text.strip() if price_elem else "Unknown"
        
        stock = "Unknown"
        if "Out of stock" in response.text or "Out of Stock" in response.text:
            stock = "Out of Stock"
        elif "Add to Cart" in response.text:
            stock = "In Stock"
            
        return {"price": price, "stock": stock}
    except Exception as e:
        return {"price": "Error", "stock": "Error"}

def scrape_digikey(url):
    # DigiKey usually blocks requests with 403.
    # We return a placeholder to remind the user to check website directly.
    return {"price": "Check Website", "stock": "Check Website"}

def scrape_microcenter(url):
    # Micro Center blocks requests with 403 bot protection.
    # We return a placeholder to remind the user to check website directly.
    return {"price": "Check Website", "stock": "Check Website"}

def scrape_newark(url):
    # Newark blocks requests with 403 bot protection.
    # We return a placeholder to remind the user to check website directly.
    return {"price": "Check Website", "stock": "Check Website"}

def main():
    results = []
    for p in PRODUCTS:
        print(f"Scraping {p['name']} from {p['supplier']}...")
        if p['supplier'] == 'Adafruit':
            info = scrape_adafruit(p['url'])
        elif p['supplier'] == 'SparkFun':
            info = scrape_sparkfun(p['url'])
        elif p['supplier'] == 'PiShop':
            info = scrape_pishop(p['url'])
        elif p['supplier'] == 'DigiKey':
            info = scrape_digikey(p['url'])
        elif p['supplier'] == 'Micro Center':
            info = scrape_microcenter(p['url'])
        elif p['supplier'] == 'Newark':
            info = scrape_newark(p['url'])
        else:
            info = {"price": "Unknown", "stock": "Unknown"}
            
        results.append({
            "name": p['name'],
            "supplier": p['supplier'],
            "url": p['url'],
            "price": info['price'],
            "stock": info['stock']
        })
        
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Raspberry Pi Supply Dashboard</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f7f6; color: #333; }}
            h1 {{ text-align: center; color: #c51a4a; }}
            .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            .timestamp {{ text-align: center; color: #777; margin-bottom: 20px; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th, td {{ border-bottom: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #f8f9fa; font-weight: bold; text-transform: uppercase; font-size: 0.9em; color: #555; }}
            tr:hover {{ background-color: #f1f1f1; }}
            .in-stock {{ color: #28a745; font-weight: bold; }}
            .out-of-stock {{ color: #dc3545; font-weight: bold; }}
            .check-website {{ color: #ffc107; font-weight: bold; }}
            a {{ color: #007bff; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            th {{ cursor: pointer; position: relative; padding-right: 20px; user-select: none; }}
            th::after {{ content: '↕'; position: absolute; right: 5px; color: #ccc; font-size: 0.8em; }}
            th.sort-asc::after {{ content: '▲'; color: #555; }}
            th.sort-desc::after {{ content: '▼'; color: #555; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Raspberry Pi Supply Dashboard</h1>
            <div class="timestamp">Last updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}</div>
            <table>
                <tr>
                    <th>Product</th>
                    <th>Supplier</th>
                    <th>Price</th>
                    <th>Status</th>
                    <th>Link</th>
                </tr>
    """
    
    for r in results:
        stock_class = "check-website"
        if "In Stock" in r['stock']:
            stock_class = "in-stock"
        elif "Out of Stock" in r['stock'] or "Out of stock" in r['stock']:
            stock_class = "out-of-stock"
            
        html_content += f"""
                <tr>
                    <td>{r['name']}</td>
                    <td>{r['supplier']}</td>
                    <td>{r['price']}</td>
                    <td class="{stock_class}">{r['stock']}</td>
                    <td><a href="{r['url']}" target="_blank">View on {r['supplier']}</a></td>
                </tr>
        """
        
    html_content += f"""
            </table>
        </div>
        <footer style="text-align: center; margin-top: 40px; color: #888; font-size: 0.9em; padding-bottom: 20px;">
            List compiled on: {datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p UTC")}
        </footer>
"""
    html_content += """
        <script>
            document.querySelectorAll('th').forEach((th, i) => {
                th.addEventListener('click', () => {
                    const table = th.closest('table');
                    const tbody = table.querySelector('tbody') || table;
                    const rows = Array.from(tbody.querySelectorAll('tr:nth-child(n+2)'));
                    const isAscending = th.classList.contains('sort-asc');
                    
                    table.querySelectorAll('th').forEach(t => t.classList.remove('sort-asc', 'sort-desc'));
                    th.classList.toggle('sort-asc', !isAscending);
                    th.classList.toggle('sort-desc', isAscending);
                    
                    rows.sort((a, b) => {
                        const cellA = a.children[i].textContent.trim();
                        const cellB = b.children[i].textContent.trim();
                        
                        const numA = parseFloat(cellA.replace(/[^0-9.-]+/g, ""));
                        const numB = parseFloat(cellB.replace(/[^0-9.-]+/g, ""));
                        
                        if (!isNaN(numA) && !isNaN(numB) && cellA.includes('$') && cellB.includes('$')) {
                            return isAscending ? numA - numB : numB - numA;
                        }
                        return isAscending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
                    });
                    
                    rows.forEach(row => tbody.appendChild(row));
                });
            });
        </script>
    </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(html_content)
    print("Generated index.html")

if __name__ == "__main__":
    main()
