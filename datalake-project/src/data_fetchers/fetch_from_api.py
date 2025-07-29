def fetch_data_from_api(url, params=None):
    import requests

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def fetch_data_from_multiple_apis(api_list):
    data = {}
    for api in api_list:
        url = api.get('url')
        params = api.get('params')
        data[url] = fetch_data_from_api(url, params)
    return data

# Example usage
if __name__ == "__main__":
    api_list = [
        {"url": "https://api.example.com/data1", "params": {"key": "value1"}},
        {"url": "https://api.example.com/data2", "params": {"key": "value2"}},
    ]
    fetched_data = fetch_data_from_multiple_apis(api_list)
    print(fetched_data)