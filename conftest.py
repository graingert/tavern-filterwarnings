import warnings

import pytest

import urllib3.exceptions


@pytest.fixture
def filter_insecure_request_warning(request):
    request.applymarker(
        pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
    )
