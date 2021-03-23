import os
import glob
import csv

class Trading212Importer():

    def __init__(self, config):
        self.config = config

    def read_csv(self):
        print("Reading transactions from CSV...")

        inputPath = self.config['Trading212']['InputPath']
        inputFiles = []
        transactions = dict()

        if not os.path.exists(inputPath):
            raise Exception("{} input path doesn't exist".format(inputPath))
        elif os.path.isdir(inputPath):
            for file in glob.glob(inputPath + "*.csv"):
                inputFiles.append(file)
        else:
            inputFiles.append(inputPath)

        for file in inputFiles:
            subdict = self.parse_transactions(file)
            transactions = self.merge_two_dicts(transactions, subdict)

        return transactions

    def parse_transactions(self, file):
        print("\tProcessing: {}".format(file))
        transactions = dict()
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions[row["ID"]] = row
        return transactions

    def merge_two_dicts(self, x, y):
        """Given two dictionaries, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z
