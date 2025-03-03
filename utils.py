import json
import re


def extract_valid_json(response, verbose=False):
    if verbose:
        print(response)
    try:
        # Try to parse the response as JSON
        json_data = json.loads(response)
        return json_data
    except ValueError:
        # If it's not valid JSON, try to find JSON within plain text
        try:
            start_idx = response.index('{')
            end_idx = response.rindex('}') + 1
            json_data = json.loads(response[start_idx:end_idx])
            return json_data
        except ValueError as e:
            print(f"Error extracting JSON: {e}")
            return None
