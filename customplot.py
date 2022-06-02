'''
MIT License

Copyright (c) 2021 Pranesh6767

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import ttk
from tkinter import filedialog
import os

class customplot:
    def __init__(self,color,dataX,dataY,x_name,y_name,title,plot_type,masterframe,x_m,y_m,x_b,y_b,marker_opt):
        self.color = color
        self.dataX = dataX
        self.dataY = dataY
        self.x_name = x_name
        self.y_name = y_name
        self.title = title
        self.plot_type = plot_type
        self.masterframe = masterframe
        
        try:
            self.dataX_up = (self.dataX * x_m) + x_b
            
        except:
            self.dataX_up = self.dataX
            
        try:
            self.dataY_up = (self.dataY * y_m) + y_b
        except:
            self.dataY_up = self.dataY
            
        

        self.annotation_flag = False
        self.marker_flag = False
        self.marker_color = 'red'
        self.marker_type = 'x'
        
        self.x_m = x_m
        self.y_m = y_m
        self.y_b = y_b
        self.x_b = x_b

        self.fig = plt.Figure(figsize=(7, 6), dpi=100)
        self.plot1 = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.masterframe)

        self.marker_opt = marker_opt
        
        if self.x_name == "NONE":
            self.x_name = self.dataX.name
        if self.y_name == "NONE":
            self.y_name = self.dataY.name

    def getdata(self):
        return {'color':self.color, 'dataX':self.dataX.name, 'dataY' :self.dataY.name,
                'x_name':self.x_name,'y_name':self.y_name,'title':self.title,'plot_type':self.plot_type,
                'x_m':self.x_m, 'y_m':self.y_m, 'x_b':self.x_b, 'y_b':self.y_b, 'Marker_2': self.marker_opt}

    def updatedata(self,color,dataX,dataY,x_name,y_name,title,plot_type,x_m,y_m,x_b,y_b,marker_opt):
        self.color = color
        self.dataX = dataX
        self.dataY = dataY
        self.x_name = x_name
        self.y_name = y_name
        self.title = title
        self.plot_type = plot_type
        if self.x_name == "NONE":
            self.x_name = self.dataX.name
        if self.y_name == "NONE":
            self.y_name = self.dataY.name
        try:
            self.dataX_up = (self.dataX * x_m) + x_b
        except:
            self.dataX_up = self.dataX
        try:
            self.dataY_up = (self.dataY * y_m) + y_b
        except:
            self.dataY_up = self.dataY
            
        self.x_m = x_m
        self.y_m = y_m
        self.y_b = y_b
        self.x_b = x_b

        self.marker_opt = marker_opt

    def updateFrame(self,frame):
        self.masterframe = frame

    def createpdf(self):
        #print("Log: Function: Createpdf Called Successfully")
        file_selected = filedialog.asksaveasfilename(defaultextension=".pdf",initialdir="/", title="Select a File")
        self.fig.savefig(file_selected)

    def plotdata(self,other_plots,subplots):

        subplotids = {1:[111],2:[121,122],3:[131,132,133],4:[221,222,223,224],
                      6:[231,232,233,234,235,236],8:[241,242,243,244,245,246,247,248],
                      9:[331,332,333,334,335,336,337,338,339]}
        

        self.fig = plt.Figure(figsize=(7, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.masterframe)

        subplotids_sel = subplotids[subplots]
        for j,division in enumerate(other_plots):
            self.plot1 = self.fig.add_subplot(subplotids_sel[j])

            for i in division:
                option_plot = i.plot_type
                if option_plot == 'Line Plot':
                    self.plot1.plot(i.dataX_up,i.dataY_up,c=i.color,marker=i.marker_opt,label = i.y_name)

                if option_plot == 'Scatter Plot':
                    self.plot1.scatter(i.dataX_up, i.dataY_up, c=i.color, label=i.y_name, marker=i.marker_opt)

                if option_plot == 'Histogram':
                    self.plot1.hist(i.dataX)

                if option_plot == 'Bar Plot':
                    self.plot1.bar(self.dataX, self.dataY, color=self.color)

            self.plot1.grid()
            leg = self.plot1.legend();
            self.plot1.set_xlabel(i.x_name)
            self.plot1.set_title(i.title)



        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)
        event_manager = self.canvas.mpl_connect('button_press_event', self.onclick_plot)
        toolbarFrame = ttk.Frame(master=self.masterframe)
        toolbarFrame.grid(row=2, column=0)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbarFrame)
        toolbar.update()

        pdf_addon_button = ttk.Button(self.masterframe, text = 'PDF',command = self.createpdf)
        pdf_addon_button.grid(row = 3, column = 0)
        #t.remove()

        return None

    def onclick_plot(self,event):
        self.canvas.flush_events()
        if self.marker_flag == True:
            self.plot1.scatter(event.xdata, event.ydata, marker=self.marker_type, c=self.marker_color)
            self.canvas.draw()

        if self.annotation_flag == True:
            xmin, xmax, ymin, ymax = self.plot1.axis()
            x_avg = xmin + xmax // 2
            y_avg = ymin + ymax // 2
            if event.xdata < x_avg:
                ha_str = "left"
                x_loc = event.xdata + (x_avg / 10)
            else:
                ha_str = "right"
                x_loc = event.xdata - (x_avg / 10)
            if event.ydata < y_avg:
                va_str = "bottom"
                y_loc = event.ydata + (y_avg / 10)
            else:
                va_str = "top"
                y_loc = event.ydata - (y_avg / 10)

            i = self.plot1.text(x_loc, y_loc, "X:{},\ny:{}".format(round(event.xdata, 2), round(event.ydata, 2)), ha=ha_str,
                           va=va_str, rotation=0, size=10,
                           bbox=dict(boxstyle="round,pad=0.3", fc="cyan", ec="b", lw=2))
            self.canvas.draw()
            i.remove()
        # if you wanna save markings.... you can do one thing
        # create a list or array in constructor and append the x and y coordinates of event
        # that you are getting on each click
        # then in plot function you can write a loop from which it can plot every markings
        return None

    def setmarker(self,marker_flags,mc,mt):
        self.marker_flag = marker_flags
        self.marker_color = mc
        self.marker_type = mt
        return 1

    def reset_frame(self,frame_r,listoplots,tot_subplots):
        self.masterframe = frame_r
        self.plotdata(listoplots,tot_subplots)

    def setannot(self,an_flag):
        self.annotation_flag = an_flag
