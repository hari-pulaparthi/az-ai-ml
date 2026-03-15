# Python Program to Simulate Parallel File Downloads using Threading 

import threading 
import time 

# Function to simulate file download 
def download_file(file_name, download_time):
    print(f"Starting download of {file_name}...")
    time.sleep(download_time)  # Simulate download time
    print(f"Completed download of {file_name}.")

# Main program 
if __name__ == "__main__":
    files = ["file1.zip", "file2.zip", "file3.zip"]
    threads = []

    print("Initiating parallel file downloads...\n")

    # Create and start threads
    for file in files:
        thread = threading.Thread(target=download_file, args=(file, 2))  # Simulate 2 seconds download time
        threads.append(thread)
        thread.start()
    
    # wait for all threads to complete
    for thread in threads:
        thread.join()

    print("\nAll file downloads completed.")