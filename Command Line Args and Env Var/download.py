import sys
import requests
import os

url = sys.argv[1]
filename = sys.argv[2]


response = requests.get(url, stream=True)
with open(filename, 'wb') as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
print("Download completed.")