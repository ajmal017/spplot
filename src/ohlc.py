import tkinter as tk
import yfinance as yf
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#oop style broken af
#graph still fills too far in screen, may introduce scroll bar

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
        self.visual = tk.Frame(self.root, width=1000, height=1000)
        self.visual.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.figure1 = plt.Figure(figsize=(5,6), dpi=200)
        self.figure2 = plt.Figure(figsize=(5,2), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.ax2 = self.figure2.add_subplot(111)
                
    def graph_data(self, pd, volume=False):
        try:
            ticker = yf.Ticker(self.get_tick.get())
            data = ticker.history(period=pd)
            if volume:
                self.plot_volume(data)
            else:
                self.plot_ohlc(data)
        except:
            tk.messagebox.showinfo("Whoops!", "You must enter a valid ticker to get data.")

    def plot_ohlc(self, data):
        #plt.style.use('fivethirtyeight')
        self.ax1.clear()
        data.Open.plot(kind='line', legend=True, ax=self.ax1)
        data.High.plot(kind='line', legend=True, ax=self.ax1)
        data.Low.plot(kind='line', legend=True, ax=self.ax1)
        data.Close.plot(kind='line', legend=True, ax=self.ax1)
        self.ax1.set_title("OHLC")
        self.ax1.set_xlabel('Date')
        self.ax1.set_ylabel('USD')
        self.canvas1 = FigureCanvasTkAgg(self.figure1, master=self.visual)
        self.canvas1.get_tk_widget().place(x=0, y=0, relwidth=1, relheight=0.6)
        
    def plot_volume(self, data):
        self.ax2.clear()
        data.Volume.plot(kind='line', legend=True, ax=self.ax2)
        self.ax2.set_title("Volume")
        self.ax2.set_xlabel('Date')
        self.ax2.set_ylabel('Stocks in Millions')
        canvas2 = FigureCanvasTkAgg(self.figure2, master=self.visual)
        canvas2.get_tk_widget().place(x=0, y=600, relwidth=1, relheight=0.4)
        
ohlc = graphic()
ohlc.root.mainloop()
