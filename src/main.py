import tkinter as tk
import yfinance as yf
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#class menu_bar:
        #buttons and methods for each option
        #window forms and buttons should move around data in a DF that gets sent as argument to the appropriate function call after execution button like "plot"


#def open/close/high/low(params):
        #time periods need to be set


#graphical display
    

if __name__=="__main__":
        #show window with buttons/run mainloop()
        ticker = yf.Ticker(input("Please input the ticker for which you would like to view candlestick data: "))
        data = ticker.history()
        make_display(data)
