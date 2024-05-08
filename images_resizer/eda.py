import pandas as pd
import requests

# Load the CSV data
data = pd.read_csv('final_perfume_data.csv', encoding='latin1')

# Check for null values
print("Null values in dataset:")
print(data.isnull().sum())

# Function to check if URLs are accessible
def check_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Check the Image URLs
data['URL Working'] = data['Image URL'].apply(check_url)

# Display the data with URL check results
print(data[['Name', 'Image URL', 'URL Working']])