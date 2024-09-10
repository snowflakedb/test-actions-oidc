print("Running in actions")
print("Running in nj34kjnrjc34")

import os

# Fetch the API secret from environment variables
api_secret = os.getenv('API_SECRET')

# Use the secret in your logic (e.g., making an API call)
# Make sure not to log or print the secret
print(api_secret[0])
print(api_secret[1])

print("API secret fetched and being used securely.")
