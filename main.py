import threading

n = 10  # Adjust 'n' to match the number of buffer slots

buffer = [None] * n
next_in = 0
next_out = 0

mutex = threading.Semaphore(1)  # Initialize mutex to 1 (unlocked)
empty_slots = threading.Semaphore(n)  # Initialize empty_slots to n (all slots are empty)
full_slots = threading.Semaphore(0)  # Initialize full_slots to 0 (no slots are full)
data_available = threading.Semaphore(0)  # Initialize data_available to 0 (no data is available)

def deposit(data):
    empty_slots.acquire()  # Wait for an empty slot
    mutex.acquire()  # Protect critical section

    # Add data to the buffer
    buffer[next_in] = data
    next_in = (next_in + 1) % n

    mutex.release()  # Release mutex
    full_slots.release()  # Signal that a slot is now full
    data_available.release()  # Signal that data is available

def remove():
    full_slots.acquire()  # Wait for a full slot
    mutex.acquire()  # Protect critical section

    # Remove data from the buffer
    data = buffer[next_out]
    next_out = (next_out + 1) % n

    mutex.release()  # Release mutex
    empty_slots.release()  # Signal that a slot is now empty
    return data

if __name__ == "__main__":
    # Your main program logic here
    # Be sure to properly manage and terminate your threads as needed.
