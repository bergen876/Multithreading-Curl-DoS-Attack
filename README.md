# Multithreading-Curl-DoS-Attack


# Overview
This Python script is designed to execute a cURL command concurrently across a large number of threads. It can be used for stress testing or simulating heavy load on a server by continuously sending HTTP requests. The script leverages Python's threading module to create multiple threads, each of which repeatedly executes the specified cURL command in an infinite loop.

# Features
High Concurrency: The script spawns a large number of threads (30,000 by default) to perform concurrent cURL requests.
Customizable Command: You can specify any cURL command to be executed by the threads.
Infinite Execution: Each thread runs in an infinite loop, continuously sending requests with a short delay between each request.

# Requirements
Python 3.x
cURL installed on the system

# Usage
Adjust the number of threads value per your system requirements 

execute the script using python3
