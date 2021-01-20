from trading212 import Trading212Importer
from yahoo_finance import YahooFinanceExporter

importer = Trading212Importer()
transactions = importer.read_csv()

exporter = YahooFinanceExporter()
exporter.write_csv(transactions)

print("")
print("----------------------------------------------------------")
print("              Star the repo to show support               ")
print(" https://github.com/praveendath92/trading212-csv")
print("----------------------------------------------------------")
print("")