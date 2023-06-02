import csv
import requests

def get_coordinates(address):
    api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your actual API key
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        results = data['results']
        if results:
            location = results[0]['geometry']['location']
            longitude = location['lng']
            latitude = location['lat']
            return longitude, latitude
    return None, None

def update_csv_with_coordinates(csv_file):
    updated_csv_file = 'updated_restaurants1.csv'
    with open(csv_file, 'r', encoding='utf-8') as file, open(updated_csv_file, 'w', newline='', encoding='utf-8') as updated_file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ['Longitude', 'Latitude']
        writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            address = row['Location']
            longitude, latitude = get_coordinates(address)
            row['Longitude'] = longitude
            row['Latitude'] = latitude
            writer.writerow(row)
    return updated_csv_file

# Example usage
csv_file = 'restaurant_data.csv'  # Replace with your actual CSV file name
updated_csv_file = update_csv_with_coordinates(csv_file)
print(f"Updated CSV file: {updated_csv_file}")
