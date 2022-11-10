from configparser import ConfigParser
from trading212 import Trading212Importer
from yahoo_finance import YahooFinanceExporter
from wallmine import WallmineExporter


config = ConfigParser()
config.read("config.ini")

importer = Trading212Importer(config)
transactions = importer.read_csv()

exporter = YahooFinanceExporter(config)
exporter.write_csv(transactions)

wallmineExporter = WallmineExporter(config)
wallmineExporter.write_csv(transactions)

print("")
print("----------------------------------------------------------")
print("              Star the repo to show support               ")
print(" https://github.com/praveendath92/trading212-csv")
print("----------------------------------------------------------")
print("")