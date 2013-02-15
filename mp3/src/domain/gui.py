"""
Brian T. Bailey
ITM 513 - MP3
2Dooz GUI Class Module
"""

import tkFont
from Tkinter import *
from tkMessageBox import *
import datautils
from Task import PRIORITY_CODE
from Task import PRIORITY_COLOR
from Task import PRIORITY_VALUE
from Task import Task


class AppGui(object):
  """2Dooz GUI Components Class.
  
  This class contains the entire 2Dooz GUI and all its methods.
  
  Attributes:
    parent: The root parent window to attach the GUI into.
    datalist: A list of Task objects that serves as run time data structure.
    selected: An integer that represents the index of the datalist that is
        currently selected.
  """
  
  def __init__(self, parent):
    """Inits the AppGui Class.
    
    Args:
      parent: The root parent window to attach the GUI into.
    """
    self.parent = parent
    self.datalist = datautils.load_data()
    self.datalist.sort(key=lambda x: x.priority)
    self.selected = None
    
    self.make_menu(parent)
    
    tFrame = Frame(parent, background='#ffffff')
    tFrame.pack(fill=X)
    bFrame = Frame(parent, background='#00ff00')
    bFrame.pack(expand=YES, fill=BOTH)
    
    selectedLabel = Label(tFrame, text='Currently Selected Task')
    selectedLabel.config(anchor='w', pady=4, font=tkFont.Font(size=18, 
                                                              weight='bold'))
    selectedLabel.pack(fill=X)
    
    self.draw_fields(tFrame)
    
    self.make_filterbar(tFrame)
    Frame(tFrame, height=10).pack()
    
    self.canvas = self.init_canvas(bFrame)
    self.draw_canvas_frame(self.canvas, self.datalist)
        
  def make_menu(self, menuparent):
    """Method to build the menu bar.
    
    Args:
      menuparent: The frame to attach the menu bar to.
    """
    menubar = Frame(menuparent, relief=RAISED, bd=2)
    menubar.pack(side=TOP, fill=X)
    
    Button(menubar, text='Add New Task', command=self.add_task).pack(side=LEFT)
    Button(menubar, text='Edit Selected Task', 
           command=self.edit_task).pack(side=LEFT)
    Button(menubar, text='Delete Selected Task', 
           command=self.delete_task).pack(side=LEFT)
    Button(menubar, text='Quit', command=self.quit_app).pack(side=RIGHT)
    
  def make_filterbar(self, filterparent):
    """Method to build the result filter control bar.
    
    Args:
      filterparent: The frame to attach the filter bar to.
    """
    filterbar = Frame(filterparent, relief=RAISED, bd=3)
    filterbar.pack(fill=X)
    
    row1 = Frame(filterbar)
    row1.pack(side=TOP, fill=X)
    s1 = Label(row1, text='Sort Order: ', pady=2, anchor='w')
    s1.config(font=tkFont.Font(weight='bold'))
    s1.pack(side=LEFT)
    self.sort_order = StringVar()
    Radiobutton(row1, text='Descending', command=self.onRadioChange, 
                variable=self.sort_order, value='DSC', padx=6).pack(side=LEFT)
    Radiobutton(row1, text='Ascending', command=self.onRadioChange, 
                variable=self.sort_order, value='ASC', padx=6).pack(side=LEFT)
    self.sort_order.set('DSC')
    
    row2 = Frame(filterbar)
    row2.pack(side=TOP, fill=X)
    s2 = Label(row2, text='Display: ', pady=2, anchor='w')
    s2.config(font=tkFont.Font(weight='bold'))    
    s2.pack(side=LEFT)
    self.display_options = []
    options = ['High Priority', 'Medium Priority', 
               'Low Priority', 'Completed Tasks']
    for opt in options:
      var = IntVar()
      Checkbutton(row2, text=opt, variable=var, command=self.onCheckbox, 
                  padx=6).pack(side=LEFT)
      var.set(1)
      self.display_options.append(var)
        
  def init_canvas(self, canvasparent, scrollheight=400):
    """Method to initialize the canvas element.
    
    Initializes the canvas element and binds the scrollbars to it.
    
    Args:
      canvasparent: The frame that the canvas element will attach to.
      scrollheight: An integer representing the vertically scrollable area.
          Default value is 400.
    
    Returns:
      The canvas element.
    """
    canvas = Canvas(canvasparent, bg='#ffffff')
    canvas.config(width=600, height=250, highlightthickness=0)
    canvas.config(scrollregion=(0, 0, 600, scrollheight))
    vScroll = Scrollbar(canvasparent)
    vScroll.config(command=canvas.yview)
    hScroll = Scrollbar(canvasparent, orient='horizontal')
    hScroll.config(command=canvas.xview)
    canvas.config(yscrollcommand=vScroll.set)
    canvas.config(xscrollcommand=hScroll.set)
    vScroll.pack(side=RIGHT, fill=Y)
    hScroll.pack(side=BOTTOM, fill=X)
    canvas.pack(side=TOP, expand=YES, fill=BOTH)
    return canvas
    
  def draw_canvas_frame(self, frameparent, data):
    """Method to draw the frame and data that is attached to the canvas element.
    
    This method draws the frame and rows of data from the datalist. It attaches
    the frame to the canvas element. Then calls the method to draw each row
    of Tasks from the datalist.
    
    Args:
      frameparent: The frame (canvas) to attach this frame to.
      data: A list of Task objects.
    """
    self.cFrame = Frame(frameparent, background='#ffffff')
    frameparent.create_window(0,0, window=self.cFrame, anchor='nw')
    self.cFrame.bind('<Configure>', self.onFrameConfigure)
    
    c1label = Label(self.cFrame, text='Priority', padx=12, bg='#cccccc')
    c1label.grid(row=0, column=0, sticky=NSEW)
    c2label = Label(self.cFrame, text='Title', padx=12, bg='#cccccc')
    c2label.grid(row=0, column=1, sticky=NSEW)
    c3label = Label(self.cFrame, text='Description', padx=12, bg='#cccccc')
    c3label.grid(row=0, column=2, sticky=NSEW)
    c4label = Label(self.cFrame, text='Due', padx=12, bg='#cccccc')
    c4label.grid(row=0, column=3, sticky=NSEW)
    c5label = Label(self.cFrame, text='Completed', padx=12, bg='#cccccc')
    c5label.grid(row=0, column=4, sticky=NSEW)
    
    totalrows = len(data)
    if totalrows == 0:
      print 'empty data'
    else:
      for row in range(totalrows):
        self.draw_row(self.cFrame, data[row], row)
    
  def draw_row(self, frame, taskobj, row):
    """Method to draw an individual from of data.
    
    This method is used to draw each row in the data table. This table is a
    grid of labels attached to the frame which is attached to the canvas. It 
    also uses the isNotFiltered method to check if it should display the row.
    
    Args:
      frame: The frame to attach the row to.
      taskobj: A Task object from datalist list of Task objects.
      row: An integer representing the index of the Task object in the datalist.
    """
    if self.isNotFiltered(taskobj):
      priority = Label(frame, text=taskobj.getPriority(), padx=12, 
                       relief=SUNKEN, bd=1, cursor='hand1')
      priority.config(bg=taskobj.getPriorityColor())
      priority.grid(row=row+1, column=0, sticky=NSEW)
      priority.bind('<Button-1>', lambda i: self.onSelectRow(i, pos=row))
    
      title = Label(frame, text=taskobj.title, padx=12, relief=SUNKEN, bd=1, 
                    anchor='w', cursor='hand1')
      title.grid(row=row+1, column=1, sticky=NSEW)
      title.bind('<Button-1>', lambda i: self.onSelectRow(i, pos=row))
    
      desc = Label(frame, text=taskobj.desc, padx=12, relief=SUNKEN, bd=1, 
                   anchor='w', justify=LEFT, cursor='hand1')
      desc.grid(row=row+1, column=2, sticky=NSEW)
      desc.bind('<Button-1>', lambda i: self.onSelectRow(i, pos=row))
    
      due = Label(frame, text=taskobj.due, padx=12, relief=SUNKEN, bd=1, 
                  cursor='hand1')
      due.grid(row=row+1, column=3, sticky=NSEW)
      due.bind('<Button-1>', lambda i: self.onSelectRow(i, pos=row))
    
      completed = Label(frame, text=taskobj.completed, padx=12, relief=SUNKEN, 
                        bd=1, cursor='hand1')
      completed.grid(row=row+1, column=4, sticky=NSEW)
      completed.bind('<Button-1>', lambda i: self.onSelectRow(i, pos=row))
      
  def onFrameConfigure(self, event):
    """Reset the scroll region of the canvas to the inner frame size.
    
    This method makes sure the canvas scroll region is set to the size of the
    frame of data attached to it. It is called whenever the frame is modified.
    
    Args:
      event: An event passed to the method
    """
    self.canvas.configure(scrollregion=self.canvas.bbox('all'))
    
  def onSelectRow(self, event, pos):
    """Callback method when a row is selected.
    
    This method is called when a row is selected in the data table. It loads 
    the selected row's data into the labels in the top portion of the GUI.
    
    Args:
      event: An event passed to the method
      pos: An integer representing the index of the Task in the datalist.
    """
    self.selected = pos
    self.selPriority.set(self.datalist[pos].getPriority())
    self.priorityLabel.config(fg=self.datalist[pos].getPriorityColor())
    self.selTitle.set(self.datalist[pos].title)
    self.selDesc.set(self.datalist[pos].desc)
    self.selDue.set(self.datalist[pos].due)
    self.selComplete.set(self.datalist[pos].completed)
    
  def draw_fields(self, parent):
    """Draws the labels in the top of the GUI to display the selected info.
    
    Args:
      parent: A frame to attached the widgets to.
    """
    selFrame = Frame(parent, background='#ffffff')
    selFrame.pack(fill=X)
    
    Label(selFrame, text='Task Priority: ', 
          anchor='e').grid(row=0, column=1, sticky=NSEW)
    Label(selFrame, text='Task Title: ', 
          anchor='e').grid(row=1, column=1, sticky=NSEW)
    Label(selFrame, text='Task Description: ', 
          anchor='e').grid(row=2, column=1, sticky=NSEW)
    Label(selFrame, text='Task Due Date: ', 
          anchor='e').grid(row=3, column=1, sticky=NSEW)
    Label(selFrame, text='Task Completed Date: ', 
          anchor='e').grid(row=4, column=1, sticky=NSEW)
    Label(selFrame, text='', anchor='e').grid(row=5, column=1, sticky=NSEW)
    
    self.selPriority = StringVar()
    self.selTitle = StringVar()
    self.selDesc = StringVar()
    self.selDue = StringVar()
    self.selComplete = StringVar()
    
    self.priorityLabel = Label(selFrame, textvariable=self.selPriority, 
                               anchor='w', fg='black')
    self.priorityLabel.grid(row=0, column=2, sticky=NSEW)
    Label(selFrame, textvariable=self.selTitle, 
          anchor='w').grid(row=1, column=2, sticky=NSEW)
    Label(selFrame, textvariable=self.selDesc, 
          anchor='w').grid(row=2, column=2, sticky=NSEW)
    Label(selFrame, textvariable=self.selDue, 
          anchor='w').grid(row=3, column=2, sticky=NSEW)
    Label(selFrame, textvariable=self.selComplete, 
          anchor='w').grid(row=4, column=2, sticky=NSEW)
    
    self.selTitle.set('Click A Task To Select')
    
  def add_task(self):
    """Callback for the add task button.
    
    This callback method for the add task button creates and populates a 
    new modal window with widgets for Task entry.  
    """
    self.addwindow = Toplevel()
    self.addwindow.title('Add a New Task')
    row1 = Frame(self.addwindow)
    row1.pack(side=TOP, fill=X)
    Label(row1, text='Task Title: ', width=15).pack(side=LEFT)
    self.addTitle = StringVar()
    Entry(row1, textvariable=self.addTitle, width=30).pack(side=RIGHT, 
                                                           expand=YES, fill=X)
    
    row2 = Frame(self.addwindow)
    row2.pack(side=TOP, fill=X)
    Label(row2, text='Task Priority: ', width=15).pack(side=LEFT)
    self.addPriority = StringVar()
    self.addPriority.set('High')
    OptionMenu(row2, self.addPriority, 'High', 'Medium', 'Low').pack(side=LEFT)
    
    row3 = Frame(self.addwindow)
    row3.pack(side=TOP, fill=X)
    Label(row3, text='Task Desc: ', width=15).pack(side=LEFT)
    self.addDesc = StringVar()
    Entry(row3, textvariable=self.addDesc, width=30).pack(side=RIGHT, 
                                                          expand=YES, fill=X)
    
    row4 = Frame(self.addwindow)
    row4.pack(side=TOP, fill=X)
    Label(row4, text='Task Due: ', width=15).pack(side=LEFT)
    self.addDue = StringVar()
    Entry(row4, textvariable=self.addDue, width=30).pack(side=RIGHT, 
                                                         expand=YES, fill=X)
    
    row5 = Frame(self.addwindow)
    row5.pack(side=TOP, fill=X)
    Label(row5, text='Completed: ', width=15).pack(side=LEFT)
    self.addCompleted = StringVar()
    Entry(row5, textvariable=self.addCompleted, 
          width=30).pack(side=RIGHT, expand=YES, fill=X)
    
    Button(self.addwindow, text='Add Task', 
           command=self.insert_task).pack(side=RIGHT)
    Button(self.addwindow, text='Cancel', 
           command=self.addwindow.destroy).pack(side=RIGHT)
    
    self.addwindow.focus_set()
    self.addwindow.grab_set()
    self.addwindow.wait_window()

  def edit_task(self):
    """Callback for the edit task button.
    
    This callback method for the edit task button creates and populates a 
    new modal window with widgets for Task editing.
    """
    if self.selected:
      self.editwindow = Toplevel()
      self.editwindow.title('Edit Selected Task')
      row1 = Frame(self.editwindow)
      row1.pack(side=TOP, fill=X)
      Label(row1, text='Task Title: ', width=15).pack(side=LEFT)
      self.editTitle = StringVar()
      self.editTitle.set(self.datalist[self.selected].title)
      Entry(row1, textvariable=self.editTitle, 
            width=30).pack(side=RIGHT, expand=YES, fill=X)
    
      row2 = Frame(self.editwindow)
      row2.pack(side=TOP, fill=X)
      Label(row2, text='Task Priority: ', width=15).pack(side=LEFT)
      self.editPriority = StringVar()
      self.editPriority.set(
          PRIORITY_CODE[self.datalist[self.selected].priority])
      OptionMenu(row2, self.editPriority, 
                 'High', 'Medium', 'Low').pack(side=LEFT)
    
      row3 = Frame(self.editwindow)
      row3.pack(side=TOP, fill=X)
      Label(row3, text='Task Desc: ', width=15).pack(side=LEFT)
      self.editDesc = StringVar()
      self.editDesc.set(self.datalist[self.selected].desc)
      Entry(row3, textvariable=self.editDesc, 
            width=30).pack(side=RIGHT, expand=YES, fill=X)
    
      row4 = Frame(self.editwindow)
      row4.pack(side=TOP, fill=X)
      Label(row4, text='Task Due: ', width=15).pack(side=LEFT)
      self.editDue = StringVar()
      self.editDue.set(self.datalist[self.selected].due)
      Entry(row4, textvariable=self.editDue, 
            width=30).pack(side=RIGHT, expand=YES, fill=X)
    
      row5 = Frame(self.editwindow)
      row5.pack(side=TOP, fill=X)
      Label(row5, text='Completed: ', width=15).pack(side=LEFT)
      self.editCompleted = StringVar()
      self.editCompleted.set(self.datalist[self.selected].completed)
      Entry(row5, textvariable=self.editCompleted, 
            width=30).pack(side=RIGHT, expand=YES, fill=X)
    
      Button(self.editwindow, text='Save Changes', 
             command=self.update_task).pack(side=RIGHT)
      Button(self.editwindow, text='Cancel', 
             command=self.editwindow.destroy).pack(side=RIGHT)
    
      self.editwindow.focus_set()
      self.editwindow.grab_set()
      self.editwindow.wait_window()
    else:
      showerror('No Selection Error', 'Nothing is Selected!')

  def insert_task(self):
    """Method to insert the new Task data into the datalist.
    
    This method inserts the new Task data from the add window to the 
    datalist Task list. It also saves the updated datalist to the filesystem 
    using the save_data method of the datautils module.
    """
    newtask = Task(self.addTitle.get(), self.addDesc.get(), 
                   PRIORITY_VALUE[self.addPriority.get()], 
                   self.addDue.get(), self.addCompleted.get())
    self.datalist.append(newtask)
    self.onRadioChange()
    self.addwindow.destroy()
    self.selPriority.set('')
    self.priorityLabel.config(fg='black')
    self.selTitle.set('Click A Task To Select')
    self.selDesc.set('')
    self.selDue.set('')
    self.selComplete.set('')
    self.selected = None
    datautils.save_data(self.datalist)  
    
  def update_task(self):
    """Method to insert the updated Task data into the datalist.
    
    This method inserts the updated Task data from the edit window to the 
    datalist Task list. It also saves the updated datalist to the filesystem 
    using the save_data method of the datautils module.
    """
    updatedtask = Task(self.editTitle.get(), self.editDesc.get(), 
                       PRIORITY_VALUE[self.editPriority.get()], 
                       self.editDue.get(), self.editCompleted.get())
    self.datalist[self.selected] = updatedtask
    self.onRadioChange()
    self.editwindow.destroy()
    self.selPriority.set('')
    self.priorityLabel.config(fg='black')
    self.selTitle.set('Click A Task To Select')
    self.selDesc.set('')
    self.selDue.set('')
    self.selComplete.set('')
    self.selected = None
    datautils.save_data(self.datalist)

  def delete_task(self):
    """Callback method for the Delete selected task button.
    
    This method deletes the selected Task object from the datalist. It also 
    saves the updated datalist to the filesystem using the save_data method of 
    the datautils module.
    """
    if self.selected:
      ans = askokcancel('Delete Task', 
                        'Are you sure you want to delete the selected task?')
      if ans:
        self.datalist.pop(self.selected)
        self.selPriority.set('')
        self.priorityLabel.config(fg='black')
        self.selTitle.set('Click A Task To Select')
        self.selDesc.set('')
        self.selDue.set('')
        self.selComplete.set('')
        self.selected = None
        self.cFrame.destroy()
        self.draw_canvas_frame(self.canvas, self.datalist)
        datautils.save_data(self.datalist)
    else:
      showerror('No Selection Error', 'Nothing is Selected!')
    
  def onRadioChange(self):
    """Callback method for sorting radio button change handler.
    
    This method causes the datalist to be sorted according to the current 
    setting of the radio button. It is called when the radio button changes. 
    It can also be called whenever you need to sort the datalist according to 
    the setting of the radiobutton.
    """
    if self.sort_order.get() == 'DSC':
      self.datalist.sort(key=lambda x: x.priority)
    elif self.sort_order.get() == 'ASC':
      self.datalist.sort(key=lambda x: x.priority, reverse=True)
    
    self.cFrame.destroy()
    self.draw_canvas_frame(self.canvas, self.datalist)
    
  def onCheckbox(self):
    """Callback method for checkbox change handler.
    
    This method simply forces the data table to redraw.
    """
    self.cFrame.destroy()
    self.draw_canvas_frame(self.canvas, self.datalist)
    
  def isNotFiltered(self, task):
    """Determines if the task should be displayed according to the filters.
    
    This method is used to determine if the given Task item should be shown 
    in the data table based on the settings of the filter checkboxes.
    
    Args:
      task: A Task object
      
    Returns:
      True: If the task is not filtered out and should be displayed.
      False: If the task is filtered out and should not be displayed.
    """
    if task.completed != '':
      #print 'task is complete'
      if self.display_options[3].get() == 0:
        #print 'dont show completed task'
        return False
      else:
        #print 'continue to check filters'
        if task.priority == 0 and self.display_options[0].get() == 1:
          #print 'High'
          return True
        elif task.priority == 1 and self.display_options[1].get() == 1:
          #print 'Med'
          return True
        elif task.priority == 2 and self.display_options[2].get() == 1:
          #print 'Low'
          return True
        else:
          #print 'false'
          return False
    else:
      #print 'task is not complete'
      if task.priority == 0 and self.display_options[0].get() == 1:
        #print 'High'
        return True
      elif task.priority == 1 and self.display_options[1].get() == 1:
        #print 'Med'
        return True
      elif task.priority == 2 and self.display_options[2].get() == 1:
        #print 'Low'
        return True
      else:
        #print 'false'
        return False
        
  def quit_app(self):
    """Callback for quit button.
    
    This method callback for the quit button verifies the user wants to quit 
    the application and if they click yes, saves the data to the filesystem
    using the save_data method of the datautils module.
    """
    ans = askokcancel('Verify exit', 'Really quit?')
    if ans:
      datautils.save_data(self.datalist)
      self.parent.quit()