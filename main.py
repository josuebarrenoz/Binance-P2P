import requests
import json
import time

url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
headers = {
    "Content-Type": "application/json",
    "clienttype": "web",
    "lang": "en"
}

def fetch_all_sellers(asset, fiat, trade_type, pay_type):
    page = 1
    rows = 20  # Binance max rows per page
    all_sellers = []

    while True:
        print(f"Fetching page {page}...")

        payload = {
            "asset": asset,
            "fiat": fiat,
            "tradeType": trade_type,
            "page": page,
            "rows": rows,
            "payTypes": [pay_type],
            "publisherType": None
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            print(f"Error on page {page}: {response.text}")
            break

        data = response.json()

        if not data['data']:
            print("No more sellers found, stopping.")
            break

        all_sellers.extend(data['data'])
        page += 1
        #time.sleep(1)  # Just to avoid rate limits

    return all_sellers

def process_sellers_to_json(sellers):
    processed = []

    for ad in sellers:
        adv = ad['adv']
        advertiser = ad['advertiser']

        processed.append({
            "seller": advertiser.get("nickName", "Unknown"),
            "price": f"{adv['price']} {adv['fiatUnit']}",
            "available_usdt": adv['surplusAmount'],
            "min_amount": f"{adv['minSingleTransAmount']} {adv['fiatUnit']}",
            "max_amount": f"{adv['maxSingleTransAmount']} {adv['fiatUnit']}",
            "completion_rate": f"{advertiser.get('monthFinishRate', 0) * 100:.2f}%",
            "trade_method": adv['tradeMethods'][0]['tradeMethodName'] if adv['tradeMethods'] else "Unknown"
        })

    return processed

def print_sellers(sellers):
    for seller in sellers:
        print(f"Seller: {seller['seller']}")
        print(f"Price: {seller['price']}")
        print(f"Available: {seller['available_usdt']} USDT")
        print(f"Min Amount: {seller['min_amount']}")
        print(f"Max Amount: {seller['max_amount']}")
        print(f"Completion Rate: {seller['completion_rate']}")
        print(f"Payment Method: {seller['trade_method']}")
        print("-" * 40)

def save_to_json_file(sellers, asset, fiat):
    filename = f"p2p_{asset}_{fiat}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(sellers, f, indent=4)
    print(f"Saved to {filename}")

# Fetch and process
asset = "USDT"
fiat = "VES"
trade_type = "SELL"
pay_type = "Banesco"

all_sellers = fetch_all_sellers(asset, fiat, trade_type, pay_type)
processed_sellers = process_sellers_to_json(all_sellers)

print_sellers(processed_sellers)

save_to_json_file(processed_sellers, asset, fiat)
print(f"Total unique sellers fetched: {len(processed_sellers)}")
