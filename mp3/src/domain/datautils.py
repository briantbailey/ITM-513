"""
Brian T. Bailey
ITM 513 - MP3
Data Utility Module
"""

import pickle


def load_data():
  """Loads data into list.
  
  Loads the application data from the pickled file on disk in the data 
  directory if it exists. If the file is not there it returns an empty list.
  
  Returns:
    A list of Task objects from the disk file or empty list if no file exists.
  """
  data = []
  try:
    f = open('data/mp3data.pkl', 'rb')
    data = pickle.load(f)
    f.close()
  except IOError:
    # File doesn't exist - load empty list
    data = []
  return data


def save_data(data):
  """Saves data list to pickled file on disk.
  
  Saves the applications data list to the pickled file on disk in the data 
  directory as long as that directory exists.
  
  Args:
    data: A list of Task objects
  """
  try:
    f = open('data/mp3data.pkl', 'wb')
    pickle.dump(data, f)
    f.close()
  except IOError:
    # File IO Error File can not save
    print 'Error Saving Data To File'