import yfinance as yf

from pandas import DataFrame

#this literally just translates the data retrieved in panda DF form from yfinance into another panda DF, it's for practice, not for practical use

if __name__ == "__main__":
    aapl = yf.Ticker('aapl')
    wk_hist = aapl.history("1wk")
    ops = wk_hist.Open
    opens = []
    for o in ops:
        opens.append(o)
    #print(opens)
    #print(wk_hist.columns)
    #print(isinstance(wk_hist,tuple))

    rows = wk_hist.index
    cols = wk_hist.columns
    dix = {}
    for c in cols:
        liss = []
        for r in rows:
            liss.append(wk_hist[c][r])
        dix[c] = liss
    dix['Date'] = rows
    df = DataFrame(dix)
    df.set_index('Date',inplace=True)
    print('Apple History Report for 1 Week')
    print(df)
