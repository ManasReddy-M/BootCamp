import requests
from requests.auth import HTTPBasicAuth
import json # Not strictly needed here, but kept for context

def fetch_json(
    url: str,
    username: str = None,
    password: str = None,
    timeout_sec: int = 10
) -> dict:
    """
    Makes a GET request to a URL and returns a structured dictionary.
    """

    auth = HTTPBasicAuth(username, password) if username and password else None

    try:
        # Perform the GET request
        response = requests.get(url, auth=auth, timeout=timeout_sec)
        print(f"Status Code: {response.status_code}")

        # Handle different status codes
        if response.status_code == 200:
            try:
                # Success: Return parsed JSON data
                return {
                    "success": True,
                    "status_code": response.status_code,
                    "headers": response.headers, # Headers object
                    "data": response.json(),
                    "error": None
                }
            except ValueError:  # JSON parsing failed
                return {
                    "success": False,
                    "status_code": response.status_code,
                    "headers": response.headers,
                    "data": None,
                    "error": "Invalid JSON response"
                }

        elif response.status_code == 401:
            return {"success": False, "status_code": 401, "headers": response.headers, "data": None, "error": "Unauthorized access"}
        elif response.status_code == 404:
            return {"success": False, "status_code": 404, "headers": response.headers, "data": None, "error": "Resource not found"}
        else:
            return {
                "success": False,
                "status_code": response.status_code,
                "headers": response.headers,
                "data": None,
                "error": "Unexpected status code received"
            }

    except requests.Timeout:
        return {"success": False, "status_code": None, "headers": None, "data": None, "error": "Request timed out"}
    except requests.ConnectionError:
        return {"success": False, "status_code": None, "headers": None, "data": None, "error": "Connection error"}
    except Exception as e:
        return {"success": False, "status_code": None, "headers": None, "data": None, "error": str(e)}

# --- Test Execution ---
data = fetch_json("https://jsonplaceholder.typicode.com/todos/1")

print("\n--- Structured Output ---")
for key, value in data.items():
    if key == "headers" and value is not None:
        # If the value is the headers dictionary.
        print(f" {key} :")
        for h_key, h_value in value.items():
            print(f"    - {h_key}: {h_value}")
    else:
        # Print all other keys normally
        print(f" {key} : {value} ")