import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# test_app.py
def test_home(client):
    response = client.get('/')
    response2 = client.get('/home')
    assert response.status_code == 200
    assert response2.status_code == 200

