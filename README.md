# 🚀 Binance P2P Seller Fetcher

## 📌 Overview
This Python script fetches P2P sellers from Binance's API for a given asset, fiat currency, trade type, and payment method. It processes and displays the fetched data in a readable format and saves it to a JSON file.

## ✅ Requirements
- 🐍 Python 3.x
- 📦 `requests` library (install using `pip install requests`)

## ⚙️ How It Works
1. 📡 Sends requests to Binance's P2P API to fetch seller advertisements.
2. 📊 Collects and processes seller details.
3. 🖥️ Prints the sellers' information in a readable format.
4. 💾 Saves the seller details to a JSON file.

## ▶️ Usage
1. Install dependencies if not already installed:
   ```sh
   pip install requests
   ```
2. Run the script:
   ```sh
   python script.py
   ```

## 🔧 Parameters
The script uses the following parameters:
- **💰 asset**: Cryptocurrency to trade (e.g., `USDT`)
- **💵 fiat**: Local currency (e.g., `BDT` for Bangladeshi Taka)
- **🔄 trade_type**: Type of trade (`BUY` or `SELL`)
- **🏦 pay_type**: Payment method (e.g., `bKash`)

These parameters can be modified in the script as needed.

## 📂 Output
- 🖥️ The script prints seller details to the console.
- 📜 The data is saved as a JSON file in the format: `p2p_{asset}_{fiat}.json`.

## 📊 Example Output
```
Fetching page 1...
Seller: JohnDoe
Price: 110.50 BDT
Available: 500.00 USDT
Min Amount: 10.00 BDT
Max Amount: 5000.00 BDT
Completion Rate: 98.75%
Payment Method: bKash
----------------------------------------
Saved to p2p_USDT_BDT.json
Total unique sellers fetched: 10
```

## 🔔 Notes
- ⏳ The script includes a delay (`time.sleep(1)`) to avoid hitting Binance's rate limits.
- ❌ If no more sellers are found, the script stops fetching further pages.

## 📜 License
This script is open-source and free to use.

---

👨‍💻 **Author**: [Abir Arafat Chawdhury](https://t.me/abirxdhackz)

