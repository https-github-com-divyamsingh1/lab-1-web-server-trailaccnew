import unittest
import subprocess
import requests
import time

# Define the server URL
server_url = "http://127.0.0.1:8080/"

class TestWebServer(unittest.TestCase):
    def test_hello_world(self):
        # Run the server.py in a subprocess
        server_process = subprocess.Popen(['python3', 'server.py'])
        
        # Wait for the server to start (you can adjust the wait time)
        time.sleep(1)

        try:
            # Perform Test 1: Request an existing page (HelloWorld.html)
            response = requests.get(server_url + "HelloWorld.html")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Hello, World!", response.text)

        finally:
            # Stop the server subprocess
            server_process.terminate()

    def test_non_existent_page(self):
        # Run the server.py in a subprocess
        server_process = subprocess.Popen(['python3', 'server.py'])
        
        # Wait for the server to start (you can adjust the wait time)
        time.sleep(1)

        try:
            # Perform Test 2: Request a non-existing page
            response = requests.get(server_url + "NonExistentPage.html")
            self.assertEqual(response.status_code, 404)
            self.assertIn("404 Not Found", response.text)

        finally:
            # Stop the server subprocess
            server_process.terminate()

    def test_root_url(self):
        # Run the server.py in a subprocess
        server_process = subprocess.Popen(['python3', 'server.py'])
        
        # Wait for the server to start (you can adjust the wait time)
        time.sleep(1)

        try:
            # Perform Test 3: Request the root URL without specifying a file
            response = requests.get(server_url)
            self.assertEqual(response.status_code, 404)
            self.assertIn("404 Not Found", response.text)

        finally:
            # Stop the server subprocess
            server_process.terminate()

if __name__ == '__main__':
    unittest.main()
