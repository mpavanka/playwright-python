import pytest

# @pytest.mark.skip
def test_skipFile():
    print("skipping this file")

@pytest.mark.smoke
def test_smokeTest():
    print("smoke test")