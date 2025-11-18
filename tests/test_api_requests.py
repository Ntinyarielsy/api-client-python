"""
Tests for the API client.
"""

import requests
from api_client.request import get_request, post_request, put_request, patch_request, delete_request

def test_get_request_success(mocker):
    mock_get = mocker.patch("requests.get")
    mock_response = mocker.Mock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {'key': 'value'}
    mock_get.return_value = mock_response

    
    url = 'https://api.example.com/data'
    headers = {'Authorization': 'Bearer token'}
    params = {'query': 'test'}

    response = get_request(url, headers=headers, params=params)

    mock_get.assert_called_once()
    called_args, called_kwargs = mock_get.call_args
    assert called_args[0] == url
    assert called_kwargs['headers'] == headers
    assert called_kwargs['params'] == params
    
    assert response.status_code == 200
    assert response.json() == {'key': 'value'}

def test_post_request_success(mocker):
    mock_post = mocker.patch('requests.post')
    mock_response = mocker.Mock(spec=requests.Response)
    mock_response.status_code = 201
    mock_response.json.return_value = {'id': 1, 'name': 'test'}
    mock_post.return_value = mock_response

    url = 'https://api.example.com/data'
    json_data = {'name': 'test'}
    headers = {'Content-Type': 'application/json'}

    response = post_request(url, json=json_data, headers=headers)

    mock_post.assert_called_once_with(url, json=json_data, headers=headers)
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'test'}

def test_put_request_success(mocker):
    mock_put = mocker.patch('requests.put')
    mock_response = mocker.Mock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': 1, 'name': 'updated'}
    mock_put.return_value = mock_response

    url = 'https://api.example.com/data/1'
    json_data = {'name': 'updated'}
    headers = {'Content-Type': 'application/json'}

    response = put_request(url, json=json_data, headers=headers)

    mock_put.assert_called_once_with(url, json=json_data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'updated'}

def test_patch_request_success(mocker):
    mock_patch = mocker.patch('requests.patch')
    mock_response = mocker.Mock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': 1, 'name': 'patched'}
    mock_patch.return_value = mock_response

    url = 'https://api.example.com/data/1'
    json_data = {'name': 'patched'}
    headers = {'Content-Type': 'application/json'}

    response = patch_request(url, json=json_data, headers=headers)

    mock_patch.assert_called_once_with(url, json=json_data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'patched'}

def test_delete_request_success(mocker):
    mock_delete = mocker.patch('requests.delete')
    mock_response = mocker.Mock(spec=requests.Response)
    mock_response.status_code = 204
    mock_delete.return_value = mock_response

    url = 'https://api.example.com/data/1'
    headers = {'Authorization': 'Bearer token'}

    response = delete_request(url, headers=headers)

    mock_delete.assert_called_once_with(url, headers=headers)
    assert response.status_code == 204