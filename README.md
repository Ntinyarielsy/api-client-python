# REST API Client

A simple and reusable REST API client library for sending GET, POST, PUT, PATCH and DELETE requests.

## Highlights

- Thin wrapper around `requests` with convenience functions: `get_request`, `post_request`, `put_request`, `patch_request`, `delete_request`.
- Each function calls `response.raise_for_status()` to surface HTTP errors as exceptions.
- Unit-tested with `pytest` and uses `pytest-mock` for mocking `requests` in tests.

## Requirements

- Python 3.9+
- The package depends on `requests` (see `pyproject.toml`).

## Installation

Clone the repository and install in editable/development mode.

1. Clone the repo:

```bash
git clone <repo-url>
cd REST_API
```

2. (Optional) Create and activate a virtual environment. The repository contains an `api-venv/` folder; you can either use that or create a new one:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the package and (optionally) dev dependencies:

```bash
pip install -e .
pip install -e ".[dev]"   # installs pytest, pytest-cov, pytest-mock
```

Note: Installing with `-e .` makes the package importable as `api_client` (the package directory is `src/api_client`).

## Usage

You can import the client functions in two common ways depending on whether you run from the repository source or after installing the package.

- When running from the repository (used by `main.py`):

```python
from src.api_client import get_request, post_request, put_request, patch_request, delete_request

resp = get_request("https://api.example.com/data")
print(resp.status_code, resp.json())
```

- When the package is installed (`pip install -e .`):

```python
from api_client import get_request, post_request, put_request, patch_request, delete_request

# GET with params
resp = get_request("https://api.example.com/data", params={"page": 1, "limit": 10})

# POST with JSON body
resp = post_request("https://api.example.com/data", json={"name": "example"}, headers={"Content-Type": "application/json"})

# PUT / PATCH / DELETE follow the same pattern:
put_resp = put_request("https://api.example.com/data/1", json={"name": "updated"})
patch_resp = patch_request("https://api.example.com/data/1", json={"name": "patched"})
del_resp = delete_request("https://api.example.com/data/1")
```

Tips:
- The functions return `requests.Response` objects. Use `response.json()` to get parsed JSON, and `response.status_code` to inspect status codes.
- Exceptions: the client calls `response.raise_for_status()` so `requests.HTTPError` will be raised for 4xx/5xx responses unless caught.

### Running the example

Run the example script that demonstrates basic calls and printing responses:

```bash
python main.py
```

## Running Tests

Run the test suite with `pytest` (the project config is in `pyproject.toml`):

```bash
pytest
```

Run coverage (optional):

```bash
pytest --cov=src
```

The tests use `pytest-mock` to patch `requests.*` functions and validate that the wrapper functions call `requests` with the expected arguments.

## Project Structure

```
REST_API/
├── api-venv/              # Optional local virtual environment (included in repo)
├── src/
│   └── api_client/        # Package: import as `api_client` after installation
│       ├── __init__.py
│       └── request.py     # Request helper functions
├── tests/                 # Unit tests
│   └── test_api_requests.py
├── main.py                # Example script demonstrating usage
├── pyproject.toml         # Project metadata and dependencies
└── README.md              # This file
```

## Notes / Known Issues

- `main.py` imports the helpers from `src.api_client` so it works when running inside the repo. When consuming this package from another project, import from `api_client` after installation.
- The package `__version__` is set in `src/api_client/__init__.py` (currently `0.1.0`).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes and add tests
4. Run `pytest` and ensure all tests pass
5. Submit a pull request

## License

MIT License