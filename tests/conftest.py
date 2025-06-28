import sys, os
import pytest

# Set import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock Redis client
class MockRedis:
    def __init__(self):
        self._cache = {}

    async def get(self, key):
        return self._cache.get(key)

    async def set(self, key, value):
        self._cache[key] = value

# Patch the cache used by the application
@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    mock = MockRedis()
    monkeypatch.setattr("services.cache.cache", mock)
    return mock
