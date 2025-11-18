import requests
import json


def get_request(url, headers=None, params=None):
    """
    Sends a GET request to the specified URL with optional headers and parameters.

    Args:
        url (str): The URL to send the GET request to.
        headers (dict, optional): A dictionary of HTTP headers to include in the request.
        params (dict, optional): A dictionary of query parameters to include in the request.

    Returns:
        requests.Response: The response object returned by the requests library.
    """
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response

def post_request(url, json=None, headers=None):
    """
    Sends a POST request to the specified URL with optional headers, data, and JSON body.

    Args:
        url (str): The URL to send the POST request to.
        headers (dict, optional): A dictionary of HTTP headers to include in the request.
        json (dict, optional): A JSON serializable object to include in the body of the request.

    Returns:
        requests.Response: The response object returned by the requests library.
    """
    response = requests.post(url, json=json, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response

def put_request(url, json=None, headers=None):
    """
    Sends a PUT request to the specified URL with optional headers, data, and JSON body.

    Args:
        url (str): The URL to send the PUT request to.
        headers (dict, optional): A dictionary of HTTP headers to include in the request.
        json (dict, optional): A JSON serializable object to include in the body of the request.

    Returns:
        requests.Response: The response object returned by the requests library.
    """
    response = requests.put(url, json=json, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response

def patch_request(url, json=None, headers=None):
    """
    Sends a PATCH request to the specified URL with optional headers, data, and JSON body.

    Args:
        url (str): The URL to send the PATCH request to.
        headers (dict, optional): A dictionary of HTTP headers to include in the request.
        json (dict, optional): A JSON serializable object to include in the body of the request.

    Returns:
        requests.Response: The response object returned by the requests library.
    """
    response = requests.patch(url, json=json, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response

def delete_request(url, headers=None):
    """
    Sends a DELETE request to the specified URL with optional headers.

    Args:
        url (str): The URL to send the DELETE request to.
        headers (dict, optional): A dictionary of HTTP headers to include in the request.

    Returns:
        requests.Response: The response object returned by the requests library.
    """
    response = requests.delete(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response