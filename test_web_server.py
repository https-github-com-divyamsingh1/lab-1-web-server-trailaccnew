import requests

# Replace with the appropriate URL of your running web server
server_url = "http://127.0.0.1:8080/"

# Test 1: Request an existing page (HelloWorld.html)
response = requests.get(server_url + "HelloWorld.html")
if response.status_code == 200 and "Hello, World!" in response.text:
    print("Test 1 Passed: Page found and content is correct.")
else:
    print("Test 1 Failed")

# Test 2: Request a non-existing page
response = requests.get(server_url + "NonExistentPage.html")
if response.status_code == 404 and "404 Not Found" in response.text:
    print("Test 2 Passed: Page not found response received.")
else:
    print("Test 2 Failed")

# Test 3: Request the root URL without specifying a file
response = requests.get(server_url)
if response.status_code == 404 and "404 Not Found" in response.text:
    print("Test 3 Passed: Root URL without a file handled correctly.")
else:
    print("Test 3 Failed")

# Add more test cases as need
