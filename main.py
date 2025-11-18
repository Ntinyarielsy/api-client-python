from src.api_client import get_request, post_request, put_request, patch_request, delete_request


def main():
    """
    Entry point for running example API calls.

    - Performs a GET, POST, PUT, PATCH and DELETE request to a public test API.
    - Demonstrates basic error handling.
    - Prints response details for inspection.
    """

    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        print(f"Sending GET request to {url}")

        response = get_request(url)

        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())

    except Exception as e:
        print("An error occurred:", str(e))

    try:
        post_url = "https://jsonplaceholder.typicode.com/todos"
        post_data = {
            "userId": 7,
            "title": "Respond to emails",
            "completed": False
            
        },
        headers = {
            "Content-Type": "application/json"
        }
        print(f"\nSending POST request to {post_url} with data: {post_data}")

        post_response = post_request(post_url, json=post_data , headers=headers)

        print("POST Response Status Code:", post_response.status_code)
        print("POST Response JSON:", post_response.json())
    except Exception as e:
        print("An error occurred during POST request:", str(e))

    try:
        put_url = "https://jsonplaceholder.typicode.com/todos/5"
        put_data = {
            "userId": 1,
            "title": "Updated Title",
            "completed": True
        }
        headers = {
            "Content-Type": "application/json"
        }
        print(f"\nSending PUT request to {put_url} with data: {put_data}")

        put_response = put_request(put_url, json=put_data, headers=headers)

        print("PUT Response Status Code:", put_response.status_code)
        print("PUT Response JSON:", put_response.json())
    except Exception as e:
        print("An error occurred during PUT request:", str(e))

    try:
        patch_url = "https://jsonplaceholder.typicode.com/todos/5"
        patch_data = {
            "title": "Patched Title"
        }
        headers = {
            "Content-Type": "application/json"
        }
        print(f"\nSending PATCH request to {patch_url} with data: {patch_data}")

        patch_response = patch_request(patch_url, json=patch_data, headers=headers)

        print("PATCH Response Status Code:", patch_response.status_code)
        print("PATCH Response JSON:", patch_response.json())
    except Exception as e:
        print("An error occurred during PATCH request:", str(e))
    
    try:
        delete_url = "https://jsonplaceholder.typicode.com/todos/5"
        print(f"\nSending DELETE request to {delete_url}")

        delete_response = delete_request(delete_url)

        print("DELETE Response Status Code:", delete_response.status_code)
        print("DELETE Response JSON:", delete_response.json())
    except Exception as e:
        print("An error occurred during DELETE request:", str(e))


if __name__ == "__main__":
    main()