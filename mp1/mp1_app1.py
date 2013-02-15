# MP1 Application 1
# Brian T. Bailey

# Define get and put functions
def get(list):
  t = list.pop(0)
  print "Removed a task from the queue: %s with priority %s" % (t.keys()[0], t[t.keys()[0]])
  return t

def put(list, task):
  list.append(task)
  list.sort(key=lambda pv: pv.values()[0], reverse=True)
  print "Added a task to the queue: %s with priority %s" % (task.keys()[0], task[task.keys()[0]])

# Create priority queue as a List
queue = []

# Start application display output
print "\nMP1 Application 1"
print "Brian T. Bailey\n"

# Load queue with test data
print "Adding Tasks to Priority Queue:"
print "----------------------------------------------------------"
for line in open('test_data.txt'):
  data = eval(line.rstrip())
  put(queue, data)
print "\n"

# Display queue contents
print "Current State of the Priority Queue:"
print "----------------------------------------------------------"
print "Number of items in queue: %s" % len(queue)
for i in queue:
  print i
print "\n"

# Remove tasks from queue in priority order
print "Removing Tasks from Priority Queue in Highest Priority FIFO Order:"
print "----------------------------------------------------------"
for i in range(len(queue)):
  get(queue)
print "\n"

# Display queue contents
print "Final State of the Priority Queue:"
print "----------------------------------------------------------"
print "Number of items in queue: %s" % len(queue)
print queue
print "\n"