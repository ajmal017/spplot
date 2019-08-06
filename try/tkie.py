import tkinter as tk
import yfinance as yf
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def scrape(ticker, command):
    #get the requested data
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
    #will not work yet for history bc has req param
    return function_mappings[command]

#put the data from the DF into TK
#rows = data.index
#cols = data.columns

#display
#window = tkinter.Tk()
#window.mainloop()

def show(data, title):
    window = tk.Tk()
    figure = plt.Figure(figsize=(5,4), dpi=350)
    ax1 = figure.add_subplot(111)
    line = FigureCanvasTkAgg(figure, window)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    data.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
    ax1.set_title(title)
    window.mainloop()


#maybe also a command to write to file

if __name__=="__main__":
        #interface to get ticker, command, and maybe window specifications
        ticker = input("Please input the ticker for which you would like to view data: ")
        print("""
The options are: info, options, option_chain, dividends, splits, actions, financials, balance_sheet, cashflow, history
""")
        command = input("Which data you would like to view? ")
        data = scrape(ticker, command)
        show(data, ticker.upper()+' '+command.capitalize())
