import warnings

import pytest

import urllib3.exceptions


@pytest.fixture
def filter_insecure_request_warning(request):
    with warnings.catch_warnings():
        warnings.simplefilter(
            "ignore", category=urllib3.exceptions.InsecureRequestWarning
        )
        yield
