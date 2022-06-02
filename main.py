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
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from data_loader import adddata_fe, getheaders_fe
import customplot
from tkinter import messagebox

font_1 = ("Times", 20, "bold")
font_2 = ("Times", 15)
font_3 = ("Times", 10)

###############################################
################ Global Variables ##############

datasets_global_var = list()
plots_global_var = dict()
plots_global_var_keys = list()
options_datasets = list()
merged_list = list()

options_plottypes = ['Line Plot','Scatter Plot','Histogram','Bar Plot']
options_color = ['blue','red','green','orange','cyan','black','purple']
options_plotids = list()
options_axis = list()
options_markers = ['red x', 'red .', 'blue x', 'blue .', 'green x', 'green .']

###############################################
#options_datasets = ['NONE','0','yhadhfasfigaushiuyq3e324eui32y489234g1','2','2','3']
#options_plottypes = ['NONE','Line Plot','Scatter Plot','Histogram','Bar Plot']
#options_axis = ['NONE','ColA','ColB','ColC']
#options_color = ['NONE','Blue','Red','Green','Orange','Violet','Black']
#options_plotids = ['NONE','Plot Name 1','Plot Name 2','Plot Name 3','Plot Name 4']
#options_markers = ['NONE','Red Cross','Red Dot','Blue Cross','Blue Dot','Green Cross','Green Dot']
root = Tk()

#####################################################################
#################### Variables in global scope #######################
clicked_option_data = StringVar()

clicked_option_plottype = StringVar()

clicked_option_xaxis = StringVar()

clicked_option_yaxis = StringVar()

clicked_option_color = StringVar()

clicked_option_plotid = StringVar()
clicked_option_plotid_m = StringVar()

clicked_option_marker = StringVar()

label_x_str = StringVar()
label_x_str.set('NONE')

label_y_str = StringVar()
label_y_str.set('NONE')

title_str = StringVar()
title_str.set('NONE')

clicked_option_marker_2 = StringVar()
clicked_option_marker_2.set('.')

marker_value = IntVar()
marker_value.set(0)

annot_value = IntVar()
annot_value.set(0)

scaling_x_m = DoubleVar()
scaling_x_m.set(1.0)

scaling_x_b = DoubleVar()
scaling_x_b.set(0.0)

scaling_y_m = DoubleVar()
scaling_y_m.set(1.0)

scaling_y_b = DoubleVar()
scaling_y_b.set(0.0)

global_listbox_index = 0


# create frame style
style1 = ttk.Style()
style1.configure('new.TFrame', background="#132020")

style2 = ttk.Style()
style2.configure('outer.TFrame', background="#091010")

style3 = ttk.Style()
style3.configure('sidebar.TFrame', background="#263f3f")

#style4 = ttk.Style()
#style4.configure('new.TEntry', insertbackground="black", foreground = "red",fieldbackground="black")


style5 = ttk.Style()
style5.configure("new.TCheckbutton", background="#263f3f",foreground = "#FFFFFF")
style5.configure("new.TMenubutton", background="#132020",foreground = "#FFFFFF")
style5.configure("side.TMenubutton", background="#263f3f",foreground = "#FFFFFF")



#####################################################################
root.title("tk.DataViz")
root.configure(background='#091010')
mainframe = ttk.Frame(root, padding="5",style='outer.TFrame')
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#################### Main frame ########################



lbl_title = Label(mainframe, text = "tk.DataViZ", font = font_1,bg = "#091010",fg = "#FFFFFF")
lbl_title.grid(row = 0, column = 0)

dataloader_frame = ttk.Frame(mainframe, padding="5",borderwidth = '5',relief = 'sunken',style='new.TFrame')
dataloader_frame.grid(row = 0, column = 1, pady = 10, padx = 10)

optionsel_frame = ttk.Frame(mainframe, padding="5",borderwidth = '5',relief = 'sunken',style='new.TFrame')
optionsel_frame.grid(row = 0, column = 2,pady = 10, padx = 10)

plot_frame = ttk.Frame(mainframe, padding="5",borderwidth = '5',relief = 'sunken',style='new.TFrame')
plot_frame.grid(row = 1, column = 0,pady = 10, padx = 10,columnspan = 2)

sidebar_frame = ttk.Frame(mainframe, padding="5",borderwidth = '5',relief = 'sunken',style='new.TFrame')
sidebar_frame.grid(row = 1, column = 2,pady = 10, padx = 10)

mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=3)

mainframe.rowconfigure(0, weight = 1)
mainframe.rowconfigure(1, weight = 3)
########################################################################

#################### data loader frame ########################
lb2 = Label(dataloader_frame, text = "Add The Dataset (CSV)", font = font_2,bg = "#132020",fg = "#FFFFFF")
lb2.grid(row = 0, column = 0)

def adddata_fi():
    global datasets_global_var, options_datasets,drop_down_data
    datasets_global_var, options_datasets = adddata_fe(datasets_global_var, options_datasets)
    drop_down_data = ttk.OptionMenu(dataloader_frame, clicked_option_data, 'NONE', style = "new.TMenubutton",*options_datasets)
    drop_down_data.config(width=20)
    drop_down_data.grid(row=0, column=2, pady=10)
    drop_down_data['menu'].configure(background="#132020",foreground = "#FFFFFF")

btn_adddata = Button(dataloader_frame, text = 'ADD',command = adddata_fi,background = 'green',foreground = '#FFFFFF',width = 10)
btn_adddata.grid(row = 1, column = 0)

lb2 = Label(dataloader_frame, text = "Dataset:-", font = font_2,bg = "#132020",fg = "#FFFFFF")
lb2.grid(row = 0, column = 1, pady = 10, padx = 20)

drop_down_data = ttk.OptionMenu(dataloader_frame, clicked_option_data, 'NONE',style = "new.TMenubutton",*options_datasets)
drop_down_data.config(width = 20)
drop_down_data.grid(row = 0, column = 2, pady = 10)
drop_down_data['menu'].configure(background="#132020",foreground = "#FFFFFF")

def proceed_fi():
    global options_axis,datasets_global_var
    ind_dataset = options_datasets.index(clicked_option_data.get())
    options_axis = getheaders_fe(ind_dataset,datasets_global_var)

    drop_down_xaxis = ttk.OptionMenu(optionsel_frame, clicked_option_xaxis, 'NONE', style = "new.TMenubutton",*options_axis)
    drop_down_xaxis.config(width=12)
    drop_down_xaxis.grid(row=0, column=3, padx=(3, 20))
    drop_down_xaxis['menu'].configure(background="#132020",foreground = "#FFFFFF")

    drop_down_yaxis = ttk.OptionMenu(optionsel_frame, clicked_option_yaxis, 'NONE', style = "new.TMenubutton",*options_axis)
    drop_down_yaxis.config(width=12)
    drop_down_yaxis.grid(row=0, column=5, padx=(3, 20))
    drop_down_yaxis['menu'].configure(background="#132020",foreground = "#FFFFFF")



btn_proceed = Button(dataloader_frame, text = 'Proceed',command = proceed_fi,background = 'green',foreground = '#FFFFFF',width = 10)
btn_proceed.grid(row = 1, column = 1, columnspan = 2)
###############################################################

#################### Option Selector frame ########################

# Row 0
lb3 = Label(optionsel_frame, text = "Plot Type:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb3.grid(row = 0, column = 0)

drop_down_plottype = ttk.OptionMenu(optionsel_frame, clicked_option_plottype, 'NONE', style = "new.TMenubutton",*options_plottypes)
drop_down_plottype.config(width = 12)
drop_down_plottype.grid(row = 0, column = 1, padx = (3,20))
drop_down_plottype['menu'].configure(background="#132020",foreground = "#FFFFFF")

lb4 = Label(optionsel_frame, text = "X-Axis:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb4.grid(row = 0, column = 2)

drop_down_xaxis = ttk.OptionMenu(optionsel_frame, clicked_option_xaxis, 'NONE', style = "new.TMenubutton",*options_axis)
drop_down_xaxis.config(width = 12)
drop_down_xaxis.grid(row = 0, column = 3, padx = (3,20))
drop_down_xaxis['menu'].configure(background="#132020",foreground = "#FFFFFF")

lb5 = Label(optionsel_frame, text = "Y-Axis:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb5.grid(row = 0, column = 4,sticky = 'W')

drop_down_yaxis = ttk.OptionMenu(optionsel_frame, clicked_option_yaxis, 'NONE',style = "new.TMenubutton",*options_axis)
drop_down_yaxis.config(width = 12)
drop_down_yaxis.grid(row = 0, column = 5, padx = (3,20))
drop_down_yaxis['menu'].configure(background="#132020",foreground = "#FFFFFF")

lb6 = Label(optionsel_frame, text = "Color:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb6.grid(row = 0, column = 6)

drop_down_color = ttk.OptionMenu(optionsel_frame, clicked_option_color, 'NONE',style = "new.TMenubutton",*options_color)
drop_down_color.config(width = 12)
drop_down_color.grid(row = 0, column = 7, padx = (3,20))
drop_down_color['menu'].configure(background="#132020",foreground = "#FFFFFF")

# Row 1

lb7 = Label(optionsel_frame, text = "Label X:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb7.grid(row = 1, column = 0,sticky = 'W')


label_x_w = Entry(optionsel_frame,textvariable = label_x_str, font=font_3,background = "#091010",foreground = '#FFFFFF')
label_x_w.grid(row = 1, column = 1,sticky = 'W', padx = (3,20))

lb8 = Label(optionsel_frame, text = "Label y:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb8.grid(row = 1, column = 2,sticky = 'W')

label_y_w = Entry(optionsel_frame,textvariable = label_y_str, font=font_3,background = "#091010",foreground = '#FFFFFF')
label_y_w.grid(row = 1, column = 3,sticky = 'W', padx = (3,20))

lb9 = Label(optionsel_frame, text = "Title of Plot:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb9.grid(row = 1, column = 4,sticky = 'W')

title_w = Entry(optionsel_frame,textvariable = title_str, font=font_3,background = "#091010",foreground = '#FFFFFF')
title_w.grid(row = 1, column = 5,sticky = 'W', padx = (3,20))

lb9_11 = Label(optionsel_frame, text = "Marker:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb9_11.grid(row = 1, column = 6,sticky = 'W')

options_markers_2 = ['.','x','+','o','^','v','s','*']

drop_down_markers_2 = ttk.OptionMenu(optionsel_frame, clicked_option_marker_2, '.', style = "new.TMenubutton",*options_markers_2)
drop_down_markers_2.config(width = 12)
drop_down_markers_2.grid(row = 1, column = 7,sticky = 'W', pady = (3,20))
drop_down_markers_2['menu'].configure(background="#132020",foreground = "#FFFFFF")
# Row 2

def addplot_fi():
    global plots_global_var,options_plotids,global_listbox_index,plots_global_var_keys
    
    plot_t_new = title_str.get()
    if plot_t_new == 'NONE':
        messagebox.showwarning("showwarning", "You can't set the plot title as NONE. Please try any valid title")
        return 0
    
    if plot_t_new in plots_global_var_keys:
        messagebox.showwarning("showwarning", "Title already exists. Please try any other title.")
        return 0 
    
    
    new_plot = customplot.customplot(
        clicked_option_color.get(),
        datasets_global_var[options_datasets.index(clicked_option_data.get())][clicked_option_xaxis.get()],
        datasets_global_var[options_datasets.index(clicked_option_data.get())][clicked_option_yaxis.get()],
        label_x_str.get(),
        label_y_str.get(),
        title_str.get(),
        clicked_option_plottype.get(),
        plot_frame,
        scaling_x_m.get(),
        scaling_y_m.get(),
        scaling_x_b.get(),
        scaling_y_b.get(),
        clicked_option_marker_2.get()
    )
    plots_global_var[title_str.get()] = new_plot
    options_plotids.append(title_str.get())
    plots_global_var_keys.append(title_str.get())

    drop_down_plotids = ttk.OptionMenu(sidebar_frame_1, clicked_option_plotid, 'NONE', style = "side.TMenubutton",*options_plotids)
    drop_down_plotids.config(width=20)
    drop_down_plotids.grid(row=0, column=1, pady=(3, 20), padx=(5, 5))
    drop_down_plotids['menu'].configure(background="#263f3f",foreground = "#FFFFFF")
    
    drop_down_plotids_m = ttk.OptionMenu(sidebar_frame_1, clicked_option_plotid_m, 'NONE', style = "side.TMenubutton",*options_plotids)
    drop_down_plotids_m.config(width = 20)
    drop_down_plotids_m.grid(row = 0, column = 2, pady = (3,20),padx = (5,5),columnspan = 2)
    drop_down_plotids_m['menu'].configure(background="#263f3f",foreground = "#FFFFFF")
    
    string_listbox = str(global_listbox_index) + ".    " +title_str.get() + "      " + clicked_option_xaxis.get() + "     " + clicked_option_yaxis.get() + "    " + clicked_option_color.get()
    
    listbox_1.insert(global_listbox_index,string_listbox)
    global_listbox_index = global_listbox_index + 1


def updateplot_fi():
    curr_plot = plots_global_var[clicked_option_plotid.get()]
    curr_plot.updatedata(
        clicked_option_color.get(),
        datasets_global_var[options_datasets.index(clicked_option_data.get())][clicked_option_xaxis.get()],
        datasets_global_var[options_datasets.index(clicked_option_data.get())][clicked_option_yaxis.get()],
        label_x_str.get(),
        label_y_str.get(),
        title_str.get(),
        clicked_option_plottype.get(),
        scaling_x_m.get(),
        scaling_y_m.get(),
        scaling_x_b.get(),
        scaling_y_b.get(),
        clicked_option_marker_2.get()
    )
    index_of_plot_in_listbox = plots_global_var_keys.index(title_str.get())
    listbox_1.delete(index_of_plot_in_listbox)
    string_listbox = str(index_of_plot_in_listbox) + ".    " +title_str.get() + "      " + clicked_option_xaxis.get() + "     " + clicked_option_yaxis.get() + "    " + clicked_option_color.get()
    listbox_1.insert(index_of_plot_in_listbox,string_listbox)
    
    
    

lb_x_m = Label(optionsel_frame, text = "X scaling factor:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb_x_m.grid(row = 2, column = 0,sticky = 'W')

en_x_m = Entry(optionsel_frame,textvariable = scaling_x_m, font=font_3,background = "#091010",foreground = '#FFFFFF')
en_x_m.grid(row = 2, column = 1,sticky = 'W', padx = (3,20))

lb_x_b = Label(optionsel_frame, text = "X Bias:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb_x_b.grid(row = 2, column = 2,sticky = 'W')

en_x_b = Entry(optionsel_frame,textvariable = scaling_x_b, font=font_3,background = "#091010",foreground = '#FFFFFF')
en_x_b.grid(row = 2, column = 3,sticky = 'W', padx = (3,20))


lb_y_m = Label(optionsel_frame, text = "Y scaling factor:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb_y_m.grid(row = 2, column = 4,sticky = 'W')

en_y_m = Entry(optionsel_frame,textvariable = scaling_y_m, font=font_3,background = "#091010",foreground = '#FFFFFF')
en_y_m.grid(row = 2, column = 5,sticky = 'W', padx = (3,20))

lb_y_b = Label(optionsel_frame, text = "Y Bias:", font = font_3,bg = "#132020",fg = "#FFFFFF")
lb_y_b.grid(row = 2, column = 6,sticky = 'W')

en_y_b = Entry(optionsel_frame,textvariable = scaling_y_b, font=font_3,background = "#091010",foreground = '#FFFFFF')
en_y_b.grid(row = 2, column = 7,sticky = 'W', padx = (3,20))





btn_add_plot = Button(optionsel_frame, text = 'Add New Plot',command = addplot_fi,background = 'blue',foreground = '#FFFFFF',width = 15)
btn_add_plot.grid(row = 3, column = 0, columnspan = 4,pady=(15,3))

btn_update_plot = Button(optionsel_frame, text = 'Update Existing Plot',command = updateplot_fi,background = 'red',foreground = '#FFFFFF',width = 15)
btn_update_plot.grid(row = 3, column = 4, columnspan = 4,pady=(15,3))


###############################################################

#################### Plot frame ########################

fig = Figure(figsize=(7, 6), dpi=100)
plot1 = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig,master = plot_frame)
canvas.draw()
canvas.get_tk_widget().grid(row = 0, column = 0)

#toolbarFrame = ttk.Frame(master=plot_frame)
#toolbarFrame.grid(row=2,column=0)
#toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
#toolbar.update()

###############################################################

#################### Sidebar frame ########################

sidebar_frame_1 = ttk.Frame(sidebar_frame, padding="5",borderwidth = '5',relief = 'sunken',style='sidebar.TFrame')
sidebar_frame_1.grid(row = 0, column = 0,pady = 10, padx = 10)

sidebar_frame_2 = ttk.Frame(sidebar_frame, padding="5",borderwidth = '5',relief = 'sunken',style='sidebar.TFrame')
sidebar_frame_2.grid(row = 1, column = 0,pady = 10, padx = 10)

sidebar_frame_3 = ttk.Frame(sidebar_frame, padding="5",borderwidth = '5',relief = 'sunken',style='sidebar.TFrame')
sidebar_frame_3.grid(row = 2, column = 0,pady = 10, padx = 10)

lb10 = Label(sidebar_frame_1, text = "Select Plot to show:", font = font_3,bg = "#263f3f",fg = "#FFFFFF")
lb10.grid(row = 0, column = 0,sticky = 'W', pady = (3,20))

drop_down_plotids = ttk.OptionMenu(sidebar_frame_1, clicked_option_plotid, 'NONE', style = "side.TMenubutton",*options_plotids)
drop_down_plotids.config(width = 20)
drop_down_plotids.grid(row = 0, column = 1, pady = (3,20),padx = (5,5))
drop_down_plotids['menu'].configure(background="#263f3f",foreground = "#FFFFFF")

drop_down_plotids_m = ttk.OptionMenu(sidebar_frame_1, clicked_option_plotid_m, 'NONE', style = "side.TMenubutton",*options_plotids)
drop_down_plotids_m.config(width = 20)
drop_down_plotids_m.grid(row = 0, column = 2, pady = (3,20),padx = (5,5), columnspan = 2)
drop_down_plotids_m['menu'].configure(background="#263f3f",foreground = "#FFFFFF")

def change_subplotopts(aa):
    options_cursubplots = [i for i in range(clicked_option_totsubplots.get())]
    drop_down_cursubplot = ttk.OptionMenu(sidebar_frame_1, clicked_option_cursubplots, 0, style = "side.TMenubutton",*options_cursubplots)
    drop_down_cursubplot.config(width=20)
    drop_down_cursubplot.grid(row=1, column=3, pady=(3, 20), padx=(5, 5))
    drop_down_cursubplot['menu'].configure(background="#263f3f",foreground = "#FFFFFF")

lb20 = Label(sidebar_frame_1, text = "Total Subplots:", font = font_3,bg = "#263f3f",fg = "#FFFFFF")
lb20.grid(row = 1, column = 0,sticky = 'W', pady = (3,20))

lb21 = Label(sidebar_frame_1, text = "Current Subplot:", font = font_3,bg = "#263f3f",fg = "#FFFFFF")
lb21.grid(row = 1, column = 2,sticky = 'W', pady = (3,20))

options_totsubplots = [1,2,3,4,6,8,9]
clicked_option_totsubplots = IntVar()
clicked_option_totsubplots.set(1)

drop_down_totsuplots = ttk.OptionMenu(sidebar_frame_1, clicked_option_totsubplots, 1,command=change_subplotopts, style = "side.TMenubutton",*options_totsubplots)
drop_down_totsuplots.config(width = 20)
drop_down_totsuplots.grid(row = 1, column = 1, pady = (3,20),padx = (5,5))
drop_down_totsuplots['menu'].configure(background="#263f3f",foreground = "#FFFFFF")

options_cursubplots = [i for i in range(clicked_option_totsubplots.get())]
clicked_option_cursubplots = IntVar()
clicked_option_cursubplots.set(0)

drop_down_cursubplot = ttk.OptionMenu(sidebar_frame_1, clicked_option_cursubplots, 0, style = "side.TMenubutton",*options_cursubplots)
drop_down_cursubplot.config(width = 20)
drop_down_cursubplot.grid(row = 1, column = 3, pady = (3,20),padx = (5,5))
drop_down_cursubplot['menu'].configure(background="#263f3f",foreground = "#FFFFFF")

def showplot_fi():
    curr_plot = plots_global_var[clicked_option_plotid.get()]
    global merged_list
    merged_list.insert(clicked_option_cursubplots.get(),[curr_plot])
    #print(curr_plot.getdata())
    ################################## Universal Marker #####################
    try:
        marker_fi()
        annote_fi()
    except:
        log_showplot_fi = 1
    #print(merged_list)
    try:
        curr_plot.plotdata(merged_list,clicked_option_totsubplots.get())
    except:
        messagebox.showerror("showerror", "Please clear the plot before displaying another plot")
    response = curr_plot.getdata()
    clicked_option_color.set(response['color'])
    clicked_option_xaxis.set(response['dataX'])
    clicked_option_yaxis.set(response['dataY'])
    label_x_str.set(response['x_name'])
    label_y_str.set(response['y_name'])
    title_str.set(response['title'])
    clicked_option_plottype.set(response['plot_type'])
    scaling_x_m.set(response['x_m'])
    scaling_y_m.set(response['y_m'])
    scaling_x_b.set(response['x_b'])
    scaling_y_b.set(response['y_b'])
    clicked_option_marker_2.set(response['Marker_2'])
    
def mergeplot_fi():
    global merged_list
    curr_plot = plots_global_var[clicked_option_plotid.get()]
    merged_list[clicked_option_cursubplots.get()].append(plots_global_var[clicked_option_plotid_m.get()])
    try:
        curr_plot.plotdata(merged_list,clicked_option_totsubplots.get())
    except:
        messagebox.showerror("showerror", "Please clear the plot before displaying another plot")
        
    
def popout_fi():
    
    
    
    #fig = Figure(figsize=(7, 6), dpi=100)
    #plot1 = fig.add_subplot(111)
    #canvas = FigureCanvasTkAgg(fig, master=plot_frame_p)
    #canvas.draw()
    #canvas.get_tk_widget().grid(row=0, column=0)
    
    
    try:
        curr_plot2 = plots_global_var[clicked_option_plotid.get()]
        
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        plot_frame_p = ttk.Frame(newWindow, padding="5", borderwidth='5', relief='sunken',style='new.TFrame')
        plot_frame_p.grid(row=1, column=0, pady=10, padx=10, columnspan=2)
        
        curr_plot2.updateFrame(plot_frame_p)
        curr_plot2.plotdata(merged_list,clicked_option_totsubplots.get())
        curr_plot2.reset_frame(plot_frame,merged_list,clicked_option_totsubplots.get())
    except:
        messagebox.showwarning("showwarning", "Please plot some data before popping up")
    
    #clear_plotsection()

def clear_plotsection():
    global  merged_list
    merged_list = list()
    fig = Figure(figsize=(7, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

btn_show_plot = Button(sidebar_frame_1, text = 'Show Plot',command = showplot_fi,background = 'green',foreground = '#FFFFFF',width = 10)
btn_show_plot.grid(row = 2, column = 0, pady=(15,3))

btn_merge_plot = Button(sidebar_frame_1, text = 'Merge Plot',command = mergeplot_fi,background = 'blue',foreground = '#FFFFFF',width = 10)
btn_merge_plot.grid(row = 2, column = 1, pady=(15,3))

btn_pop_out = Button(sidebar_frame_1, text = 'Pop Out',command = popout_fi,background = 'purple',foreground = '#FFFFFF',width = 10)
btn_pop_out.grid(row = 2, column = 2, pady=(15,3))

btn_clear_plot = Button(sidebar_frame_1, text = 'Clear Plot',command = clear_plotsection,background = 'red',foreground = '#FFFFFF',width = 10)
btn_clear_plot.grid(row = 2, column = 3, pady=(15,3))

lb11 = Label(sidebar_frame_2, text = "Marker:", font = font_3,bg = "#263f3f",fg = "#FFFFFF")
lb11.grid(row = 0, column = 0,sticky = 'W', pady = (3,20))

def change_marker_fi(choice):
    curr_plot = plots_global_var[clicked_option_plotid.get()]
    if marker_value.get()==1:
        (mc, mt) = choice.split(" ")
        status = curr_plot.setmarker(True,mc,mt)
        print(status)
        print(mc,mt)
    if marker_value.get()==0:
        (mc, mt) = clicked_option_marker.get().split(" ")
        curr_plot.setmarker(False, mc, mt)

drop_down_markers = ttk.OptionMenu(sidebar_frame_2, clicked_option_marker, 'NONE', style = "side.TMenubutton",*options_markers, command = change_marker_fi)
drop_down_markers.config(width = 15)
drop_down_markers.grid(row = 0, column = 1, pady = (3,20),padx = (5,5))
drop_down_markers['menu'].configure(background="#263f3f",foreground = "#FFFFFF")

def marker_fi():

    curr_plot = plots_global_var[clicked_option_plotid.get()]
    if marker_value.get()==1:
        (mc, mt) = clicked_option_marker.get().split(" ")
        status = curr_plot.setmarker(True,mc,mt)
        print(status)
        print(mc,mt)
    if marker_value.get()==0:
        (mc, mt) = clicked_option_marker.get().split(" ")
        curr_plot.setmarker(False, mc, mt)


C1 = ttk.Checkbutton(sidebar_frame_2, text = "ON", variable = marker_value,
                 onvalue = 1, offvalue = 0,command = marker_fi,style = 'new.TCheckbutton')
C1.grid(row = 0, column = 2, pady = (3,20),padx = (2,5))


def annote_fi():
    curr_plot = plots_global_var[clicked_option_plotid.get()]
    if annot_value.get() == 1:
        curr_plot.setannot(True)
    if annot_value.get() == 0:
        curr_plot.setannot(False)

lb12 = Label(sidebar_frame_2, text = "Annotations :", font = font_3,bg = "#263f3f",fg = "#FFFFFF")
lb12.grid(row = 1, column = 0,sticky = 'W', pady = (3,20))

C2 = ttk.Checkbutton(sidebar_frame_2, text = "ON", variable = annot_value,
                 onvalue = 1, offvalue = 0, command = annote_fi,style = 'new.TCheckbutton')
C2.grid(row = 1, column = 1, pady = (3,20),padx = (2,5))

def savepdf_fi():
    curr_plot = plots_global_var[clicked_option_plotid.get()]
    curr_plot.createpdf()

btn_save_pdf_1 = Button(sidebar_frame_2, text = 'Save PDF',command = savepdf_fi,background = 'green',foreground = '#FFFFFF',width = 15)
btn_save_pdf_1.grid(row = 1, column = 2, pady = (3,20),padx = (2,5))

listbox_1 = Listbox(sidebar_frame_3,width = 70,background = "#091010",foreground = '#FFFFFF')
listbox_1.grid(row = 0, column = 0, pady = (3,3), padx = (3,3))




###############################################################

root.mainloop()
