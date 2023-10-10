import os
import shodan
import json

# Read Shodan API key from the environment variable
SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')

# Read Shodan query from the environment variable or provide a default query
SHODAN_QUERY = os.getenv('SHODAN_QUERY')

def shodan_search(api_key, query):
    try:
        # Initialize the Shodan API client
        api = shodan.Shodan(api_key)

        # Perform the Shodan search
        results = api.search(query)

        # Create a list to store the results
        formatted_results = []

        # Iterate through the results and format them
        for result in results['matches']:
            formatted_result = {
                'IP': result['ip_str'],
                'Port': result['port'],
                'Organization': result.get('org', 'N/A'),
                'Location': result.get('location', 'N/A'),
                'Data': result.get('data', 'N/A')
            }
            formatted_results.append(formatted_result)

        # Write the formatted results to a JSON file
        with open('shodan_results.json', 'w') as json_file:
            json.dump(formatted_results, json_file, indent=4)

        print(f'Successfully saved {len(formatted_results)} results to shodan_results.json')

    except shodan.APIError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # Call the shodan_search function with your API key and query
    shodan_search(SHODAN_API_KEY, SHODAN_QUERY)
