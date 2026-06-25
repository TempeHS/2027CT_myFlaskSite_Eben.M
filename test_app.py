import pytest
from flask import url_for
from app import app, PAGES


@pytest.fixture
def client():
    """Create a test client for our Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    """Test that the home page returns status 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_has_title(client):
    """Test that the home page contains our site title."""
    response = client.get("/")
    assert b"My Flask Site" in response.data


def test_home_page_has_bootstrap(client):
    """Test that Bootstrap CSS is linked."""
    response = client.get("/")
    assert b"bootstrap" in response.data


def test_home_page_has_searchbar(client):
    """Test that navbar contains searchbar."""
    response = client.get("/")
    assert b"search" in response.data


def test_contact_page_loads(client):
    """Test that the contact page returns status 200."""
    response = client.get("/contact")
    assert response.status_code == 200


def test_contact_page_has_form(client):
    """Test that the contact page has a form."""
    response = client.get("/contact")
    assert b"<form" in response.data


def test_about_page_loads(client):
    """Test that the about us page returns status 200"""
    response = client.get("/about")
    assert response.status_code == 200


def test_library_page_loads(client):
    """Test that the library page returns status 200"""
    response = client.get("/library")
    assert response.status_code == 200


def test_library_page_has_all_links(client):
    """Test that library page contains links for all entries in PAGES."""
    response = client.get("/library")
    assert response.status_code == 200

    with app.test_request_context():
        for page in PAGES:
            expected_href = f'href="{url_for(page["endpoint"])}"'.encode()
            expected_title = page["title"].encode()

            assert expected_href in response.data
            assert expected_title in response.data
