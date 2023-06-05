import requests
import json

# Set up API endpoint and parameters
url = "https://groceryprices.com/api/v1/prices"
params = {"item": "milk", "location": "New York"}

# Send GET request to API endpoint
response = requests.get(url, params=params)

# Parse JSON response
data = json.loads(response.text)

# Extract relevant information from response
price = data["prices"][0]["price"]
store = data["prices"][0]["store"]

# Print results
print(f"The price of milk at {store} in New York is {price}.")
