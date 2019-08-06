import argparse
import yfinance as yf
from pprint import pprint



def parse(result):
        pass


if __name__=="__main__":
        argparser = argparse.ArgumentParser()
        argparser.add_argument('ticker',help = 'Prints data from online yfin scraper.')
        args = argparser.parse_args()
        ticker = args.ticker
        try:
                ticker = yf.Ticker(ticker)
                function_mappings = {
                        'info':ticker.info,
                        'options':ticker.options,
                        'option_chain':ticker.option_chain,
                        'dividends':ticker.dividends,
                        'splits':ticker.splits,
                        'actions':ticker.actions,
                        'financials':ticker.financials,
                        'balance_sheet':ticker.balance_sheet,
                        'cashflow':ticker.cashflow,
                        'history':ticker.history
                }
        except ValueError:
                print('Could not create ticker {}.\n'.format(args.ticker.upper()))
        else:
                print('The things you can ask of this ticker are:')
                pprint([f for f in function_mappings])
                result=function_mappings[input('Please input the function you want to use: ')]
                parse(result)
                pprint(result)
                        
