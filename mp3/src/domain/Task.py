"""
Brian T. Bailey
ITM 513 - MP3
Task Class Module
"""

PRIORITY_CODE = {2: 'Low', 1: 'Medium', 0: 'High'}
PRIORITY_COLOR = {2: 'blue', 1: 'green', 0: 'red'}
PRIORITY_VALUE = {'Low': 2, 'Medium': 1, 'High': 0}


class Task:
  """Models Task data.
  
  This class is a model for 2Dooz task data.
  
  Attributes:
    title: A string for the task title
    desc: A string for a slightly longer task description
    priority: An integer representing the task priority value.
        High = 0, Medium = 1, Low = 2
    due: A String representing a due date/time
    completed: A String representing a completed date/time
  """
  
  def __init__(self, title, desc, priority, due, completed):
    """Inits the Task Class."""
    self.title = title
    self.desc = desc
    self.priority = priority
    self.due = due
    self.completed = completed

  def __str__(self):
    """String method for string conversion and output."""
    return "(Task: %s, Priority: %s, Due: %s, Completed: %s)" % (
        self.title, self.getPriority(), self.due, self.completed)

  def getPriority(self):
    """Method to get the string value of the priority code.
    
    Returns:
      A string representing the text value of the priority code.
    """
    return PRIORITY_CODE[self.priority]
    
  def getPriorityColor(self):
    """Method to get the string value of the priority color.
    
    Returns:
      A string representing the text value of the priority color.
    """
    return PRIORITY_COLOR[self.priority]


# Testing
if __name__ == '__main__':
  aTask = Task('Test', 'Test Task', 2, '2012', '2012')
  print aTask