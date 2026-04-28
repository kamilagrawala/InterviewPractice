from collections import deque
import pprint

def print_formatted(data):
    """Pretty prints the given data."""
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

def main():
    """Main entry point for ActivityMonitor."""
    print("Welcome to ActivityMonitor!")
    userInterfaceHandler()

def setupDeque():
    return deque()

dq_items = setupDeque()
dq_time = setupDeque()

def addItemsDeque(items):
    dq_items.append(items)

def addTimeStampsDeque(time_stamps):
    dq_time.append(time_stamps)

def cleanDeques(w, t):
    while len(dq_items) > 0 and int(dq_time[0]) <= int(t) - w:
        dq_time.popleft()
        dq_items.popleft()

def userInterfaceHandler():
    while True:
        events = input("Enter events:\n").split("\n")
        print_formatted(f"events: {events}")

        for e in events:
            array = e.split(" ")
            addTimeStampsDeque(array[0])
            addItemsDeque(array[1])

            print_formatted(f"last time in timestamps {dq_time[-1]}")
            cleanDeques(500, dq_time[-1])
            print_formatted(f"{dq_time[-1]} {array[1]} {len(dq_items)}")

        print_formatted(f"dq_items: {dq_items}")
        print_formatted(f"dq_time: {dq_time}")

if __name__ == "__main__":
    main()
