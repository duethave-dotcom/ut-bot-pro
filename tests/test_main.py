import os

import pytest

from main import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_home_returns_successful_response(client):
    response = client.get("/")

    assert response.status_code == 200


def test_home_contains_project_status(client):
    response = client.get("/")
    page = response.get_data(as_text=True)

    assert "MetaTrader 5 Bot System" in page
    assert "Online & Live" in page
    assert "Waiting for MT5 Configuration" in page


def test_unknown_route_returns_not_found(client):
    response = client.get("/does-not-exist")

    assert response.status_code == 404


def test_port_defaults_to_10000(monkeypatch):
    monkeypatch.delenv("PORT", raising=False)

    port = int(os.environ.get("PORT", 10000))

    assert port == 10000


def test_port_can_be_read_from_environment(monkeypatch):
    monkeypatch.setenv("PORT", "5000")

    port = int(os.environ.get("PORT", 10000))

    assert port == 5000
