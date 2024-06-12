
import threading   # Imports the threading module, which allows the creation of multiple threads.
import time       #Imports the time module, used here to simulate delays and measure performance.


def eat_breakfast():
    # Simulate the time taken to eat breakfast by sleeping for 3 seconds
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    #Simulate the time taken to drink coffee by sleeping for 4 seconds
    time.sleep(4)
    print("You drank coffee")


def study():
     # Simulate the time taken to study by sleeping for 5 seconds
    time.sleep(5)
    print("You finish studying")
    
    
# eat_breakfast()
# drink_coffee()
# study()

# Creating a new thread to run the eat_breakfast function
x = threading.Thread(target=eat_breakfast, args=())
x.start()# Start the thread, which runs the eat_breakfast function concurrently

# Creating a new thread to run the drink_coffee function
y = threading.Thread(target=drink_coffee, args=())
y.start()# Start the thread, which runs the drink_coffee function concurrently

# Creating a new thread to run the study function
z = threading.Thread(target=study, args=())
z.start()# Start the thread, which runs the study function concurrently

# Wait for the eat_breakfast thread to finish
x.join()

# Wait for the drink_coffee thread to finish
y.join()

# Wait for the study thread to finish
z.join()

# Print the number of active threads
print(threading.active_count())

# Print a list of all active Thread objects
print(threading.enumerate())

# Print the value of the performance counter, which is the time in seconds since an unspecified point
print(time.perf_counter())