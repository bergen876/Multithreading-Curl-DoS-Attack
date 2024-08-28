import subprocess
import threading
import time

# Number of threads to run concurrently
num_threads = 30000

# The command to execute
curl_command = 'insert curi command '

def run_curl():
    while True:
        subprocess.call(curl_command, shell=True)
        time.sleep(0.001)  # Sleep for 1 millisecond

# Create and start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=run_curl)
    thread.start()
    threads.append(thread)

# Join threads (this will actually never happen in this infinite loop)
for thread in threads:
    thread.join()
