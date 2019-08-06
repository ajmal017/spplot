# must run with command line: sudo python3 yfie.py 

import yfinance as yf
import argparse

def print_all(ticker):
    #prints all information about Ticker
    #print Ticker itself
    print('This is a ticker object from {}\n'.format(yf.__file__))
    print('This ticker is {}\n'.format(ticker))
    #print properties/methods of Ticker
    yfie_props = ['info','options','option_chain','dividends','splits','actions','financials','balance_sheet','cashflow','history']
    print('The things you can ask of this ticker are:\n')
    for p in yfie_props:
        print(p)
    print('\nThis is the history doc string:\n{}\nParameters\n\tperiod : str\n\t\tValid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max\n\t\tEither Use period parameter or use start and end\n\tinterval : str\n\t\tValid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo\n\t\tIntraday data cannot extend last 60 days\n\tstart: str\n\t\tDownload start date string (YYYY-MM-DD) or _datetime.\n\t\tDefault is 1900-01-01\n\tend: str\n\t\tDownload end date string (YYYY-MM-DD) or _datetime.\n\t\tDefault is now\n\tprepost : bool\n\t\tInclude Pre and Post market data in results?\n\t\tDefault is False\n\tauto_adjust: bool\n\t\tAdjust all OHLC automatically? Default is True\n')

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('abrev',help = 'Prints info about what you can do with a yfinance ticker.')
    args = argparser.parse_args()
    abrev = args.abrev
    try:
        ticker = yf.Ticker(abrev)
    except IOError:
        print('Could not create ticker.\n')
    else:
        print_all(ticker)
        
