import threading
import time
from queue import Queue
from typing import List
import random


def basic_thread_example():
    """Demonstrate basic thread creation and execution."""
    def worker(name: str):
        print(f"Thread {name} starting")
        time.sleep(2)
        print(f"Thread {name} finished")

    # Create and start threads
    thread1 = threading.Thread(target=worker, args=("A",))
    thread2 = threading.Thread(target=worker, args=("B",))

    thread1.start()
    thread2.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()

    print("All threads completed")


def thread_with_args():
    """Show how to pass arguments to threads."""
    def worker(name: str, delay: float):
        print(f"Thread {name} starting with delay {delay}")
        time.sleep(delay)
        print(f"Thread {name} finished")

    # Create threads with different arguments
    threads = [
        threading.Thread(target=worker, args=(
            f"Thread-{i}", random.uniform(1, 3)))
        for i in range(3)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def thread_synchronization():
    """Demonstrate thread synchronization using locks."""
    class Counter:
        def __init__(self):
            self.count = 0
            self.lock = threading.Lock()

        def increment(self):
            with self.lock:
                current = self.count
                time.sleep(0.1)  # Simulate some work
                self.count = current + 1
                print(f"Count: {self.count}")

    counter = Counter()
    threads = [threading.Thread(target=counter.increment) for _ in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def producer_consumer():
    """Show producer-consumer pattern using Queue."""
    def producer(queue: Queue):
        for i in range(5):
            item = f"Item {i}"
            queue.put(item)
            print(f"Produced: {item}")
            time.sleep(0.5)

    def consumer(queue: Queue):
        while True:
            try:
                item = queue.get(timeout=3)
                print(f"Consumed: {item}")
                time.sleep(1)
            except Queue.Empty:
                break

    queue = Queue()
    producer_thread = threading.Thread(target=producer, args=(queue,))
    consumer_thread = threading.Thread(target=consumer, args=(queue,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


def thread_pool_example():
    """Demonstrate using a thread pool for parallel tasks."""
    def worker(task_id: int):
        print(f"Processing task {task_id}")
        time.sleep(random.uniform(0.5, 2))
        print(f"Completed task {task_id}")

    # Create a pool of worker threads
    threads: List[threading.Thread] = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def main():
    """Run all threading examples."""
    print("\n=== Basic Thread Example ===")
    basic_thread_example()

    print("\n=== Thread with Arguments ===")
    thread_with_args()

    print("\n=== Thread Synchronization ===")
    thread_synchronization()

    print("\n=== Producer-Consumer Pattern ===")
    producer_consumer()

    print("\n=== Thread Pool Example ===")
    thread_pool_example()


if __name__ == "__main__":
    main()
