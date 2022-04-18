from configparser import ConfigParser
import csv
from datetime import datetime


class WallmineExporter():

    def __init__(self, config):
        self.config = config

    def write_csv(self, transactions):
        print("\nWriting transactions to Wallmine CSV...")
        outputpath = self.config['Wallmine']['OutputPath']

        with open(outputpath, 'w', newline='') as csvfile:
            fieldnames = [
                "Name",
                "Symbol",
                "Shares",
                "Type",
                "Date",
                "Price",
                "Commission",
                "Notes"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for key, transaction in transactions.items():

                action = transaction["Action"]
                type = action
                symbol = transaction["Ticker"]
                name = transaction["Name"]
                commision = transaction["Currency conversion fee (EUR)"]
                price = transaction["Price / share"]
                quantity = transaction["No. of shares"]
                tradeDate = datetime.fromisoformat(transaction["Time"])

                if action in ["Market buy", "Limit buy", "Stop limit buy"]:
                    type = "BUY"
                elif action in ["Market sell", "Limit sell", "Stop limit sell", "Stop sell"]:
                    type = "SELL"
                else:
                    # Probably one of dividend, deposit or withdraw
                    # These aren't supported by Yahoo Finance import format
                    continue

                if symbol in ['VUAA', 'ECAR']:
                    continue
                elif symbol in self.config['WallmineTickerMap']:
                    symbol = self.config['WallmineTickerMap'][symbol]

                writer.writerow({
                    "Name": name,
                    "Symbol": symbol,
                    "Shares": quantity,
                    "Type": type,
                    "Date": tradeDate.strftime("%d.%m.%Y"),
                    "Price": price,
                    "Commission": commision,
                    "Notes": ""
                })
            print("\tWritten to: {}".format(outputpath))
