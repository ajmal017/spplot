
def addScrollingFigure(figure, frame):
    global canvas, mplCanvas, interior, interior_id, cwid
    # set up a canvas with scrollbars
    canvas = Canvas(frame)
    canvas.grid(row=1, column=1, sticky=Tkconstants.NSEW)
    
    xScrollbar = Scrollbar(frame, orient=Tkconstants.HORIZONTAL)
    yScrollbar = Scrollbar(frame)
    
    xScrollbar.grid(row=2, column=1, sticky=Tkconstants.EW)
    yScrollbar.grid(row=1, column=2, sticky=Tkconstants.NS)
    
    canvas.config(xscrollcommand=xScrollbar.set)
    xScrollbar.config(command=canvas.xview)
    canvas.config(yscrollcommand=yScrollbar.set)
    yScrollbar.config(command=canvas.yview)
    
    # plug in the figure
    figAgg = FigureCanvasTkAgg(figure, canvas)
    mplCanvas = figAgg.get_tk_widget()
    
    # and connect figure with scrolling region
    cwid = canvas.create_window(0, 0, window=mplCanvas, anchor=Tkconstants.NW)
    printBboxes("Init")
    changeSize(figure, 1)
    
