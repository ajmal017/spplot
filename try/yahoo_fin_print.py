import json
import argparse
from pprint import pprint

def show_data(ticker):
        with open('{}-summary.json'.format(ticker)) as data_file:
                data = json.load(data_file)
                #print(data)
                #pprint(data)
                #print('\n')
                for x in data:
                        print(x, ':', data[x])

if __name__=="__main__":
        argparser = argparse.ArgumentParser()
        argparser.add_argument('ticker',help = 'Prints data from online yfin scraper.')
        args = argparser.parse_args()
        ticker = args.ticker
        try:
                f = open("{}-summary.json".format(ticker))
                f.close()
        except IOError:
                print('File is not accessible')
        else:
                print ("Reading data from {}-summary.json\n".format(ticker))
                show_data(ticker)
