import requests

# Make a GET request to the API
response = requests.get("https://api.postalpincode.in/pincode/712415")

# Extract the JSON data from the response
data = response.json()

# Access the dictionary inside the list and print the number of pincodes found
print(data[0]["Message"])

print("Post Offices:")
for post_office in data[0]["PostOffice"]:
    print("Name:", post_office["Name"])
    print("Branch Type:", post_office["BranchType"])
    print("Delivery Status:", post_office["DeliveryStatus"])
    print("Circle:", post_office["Circle"])
    print("District:", post_office["District"])
    print("Division:", post_office["Division"])
    print("Region:", post_office["Region"])
    print("Block:", post_office["Block"])
    print("State:", post_office["State"])
    print("Country:", post_office["Country"])
    print("Pincode:", post_office["Pincode"])
    print()
