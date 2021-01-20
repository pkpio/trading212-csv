from configparser import ConfigParser
import csv
from datetime import datetime

class YahooFinanceExporter():
    SymbolMap = {
        "BTCE": "DE000A27Z304.SG",
        "WDI": "WDI.DE",
        "ECAR": "ECAR.L"
    }

    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")

    def write_csv(self, transactions):
        print("Writing transactions to CSV...")
        outputpath = self.config['YahooFinance']['OutputPath']

        with open(outputpath, 'w', newline='') as csvfile:
            fieldnames = [
                "Symbol",
                "Current Price",
                "Date",
                "Time",
                "Change",
                "Open",
                "High",
                "Low",
                "Volume",
                "Trade Date",
                "Purchase Price",
                "Quantity",
                "Commission",
                "High Limit",
                "Low Limit",
                "Comment"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for key, transaction in transactions.items():

                action = transaction["Action"]
                symbol = transaction["Ticker"]
                currency = transaction["Currency (Price / share)"]
                price = transaction["Price / share"]
                quantity = transaction["No. of shares"]
                tradeDate = datetime.fromisoformat(transaction["Time"])

                if action in ["Market buy", "Limit buy", "Stop limit buy"]:
                    quantity = float(quantity)
                elif action in ["Market sell", "Limit sell", "Stop limit sell"]:
                    quantity = -float(quantity)
                else:
                    # Probably one of dividend, deposit or withdraw
                    # These aren't supported by Yahoo Finance import format
                    continue

                if symbol in self.SymbolMap:
                    symbol = self.SymbolMap[symbol]
                elif currency == "GBX":
                    # UK stocks are typically mapped with .L at end
                    symbol = symbol + ".L"
                elif currency == "USD":
                    # Dollar stocks typically don't need any extra work
                    pass
                else:
                    print("Unknown symbol {}".format(symbol))

                writer.writerow({
                    "Symbol": symbol,
                    "Date": tradeDate.strftime("%Y/%m/%d"),
                    "Time": tradeDate.strftime("%H:%M"),
                    "Trade Date": tradeDate.strftime("%Y%m%d"),
                    "Purchase Price": price,
                    "Quantity": quantity
                })
            print("\tWritten to: {}".format(outputpath))
