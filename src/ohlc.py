import tkinter as tk
import yfinance as yf
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#need graph to replace instead of add more - probably with .clear()
#graph still fills too far in screen, may introduce scroll bar
#put volume below

class graphic:
    def __init__(self):
        #basic setup
        self.root = tk.Tk()
        self.root.title("OHLC Project")
        #buttons
        self.options = tk.Frame(self.root)
        self.options.pack(side=tk.LEFT, fill=tk.BOTH)
        #form for ticker entry
        tk.Label(self.options, text="Ticker").grid(row=0, sticky=tk.W)
        self.get_tick = tk.Entry(self.options)
        self.get_tick.grid(row=0, column=1)
        self.get_tick.focus_set()
        #buttons
        self.week = tk.Button(self.options, text="1 week", command=lambda pd='1wk': self.graph_data(pd))
        self.week.grid(row=1,column=0)
        self.month = tk.Button(self.options, text="1 month", command=lambda pd= '1mo' : self.graph_data(pd))
        self.month.grid(row=1,column=1)
        self.volume = tk.Button(self.options, text="Volume", command=lambda pd='1mo': self.graph_data(pd, volume=True))
        self.volume.grid(row=2,column=1)
        #section for the graph
        self.visual = tk.Frame(self.root)
        self.visual.pack(side=tk.LEFT, fill=tk.BOTH)
        
    def graph_data(self, pd, volume=False):
        try:
            ticker = yf.Ticker(self.get_tick.get())
            data = ticker.history(period=pd)
            if volume:
                self.plot_volume(data)
            else:
                self.plot_it(data)
        except:
            tk.messagebox.showinfo("Whoops!", "You must enter a valid ticker to get data.")

    def plot_it(self, data):
        #plt.style.use('fivethirtyeight')
        figure = plt.Figure(figsize=(5,6), dpi=200)
        ax1 = figure.add_subplot(111)
        data.Open.plot(kind='line', legend=True, ax=ax1)
        data.High.plot(kind='line', legend=True, ax=ax1)
        data.Low.plot(kind='line', legend=True, ax=ax1)
        data.Close.plot(kind='line', legend=True, ax=ax1)
        ax1.set_title("OHLC")
        ax1.set_xlabel('Date')
        ax1.set_ylabel('USD')
        line = FigureCanvasTkAgg(figure, self.visual)
        line.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_volume(self, data):
        figure = plt.Figure(figsize=(5,6), dpi=200)
        ax1 = figure.add_subplot(111)
        data.Volume.plot(kind='line', legend=True, ax=ax1)
        ax1.set_title("Volume")
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Stocks in Millions')
        line = FigureCanvasTkAgg(figure, self.visual)
        line.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        
ohlc = graphic()
ohlc.root.mainloop()
