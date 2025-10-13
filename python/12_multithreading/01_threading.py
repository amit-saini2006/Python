import threading
import time

def takeOrders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brewChai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

# create threads
order_thread = threading.Thread(target=takeOrders)
brewChai_thread = threading.Thread(target=brewChai)

order_thread.start()
brewChai_thread.start()

# wait for both to finsih
order_thread.join()
brewChai_thread.join()
print(f"All orders taken and chai brewed")