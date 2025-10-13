import threading
import time

def brewChai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 = threading.Thread(target=brewChai, name="Barista-1")
thread2 = threading.Thread(target=brewChai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")