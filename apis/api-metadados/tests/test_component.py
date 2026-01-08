from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Tests for get_component_by_id endpoint #

def test_get_component_success():
    response = client.get("/components/0")
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_component_id_negativo():
    response = client.get("/components/-1")
    assert response.status_code == 422


def test_get_component_not_found():
    response = client.get("/components/50000")
    assert response.status_code == 404

    body = response.json()
    assert body["detail"]["error_code"] == "404_COMPONENT_NOT_FOUND"


def test_get_component_internal_error(mocker):
    mocker.patch(
        "src.routes.route.ComponentController.get_component_by_id",
        side_effect=Exception("Erro forçado")
    )

    response = client.get("/components/0")

    assert response.status_code == 500
    body = response.json()

    assert body["detail"]["error_code"] == "500_INTERNAL_SERVER_ERROR"
    assert "message" in body["detail"]



# Tests for get_component_by_criteria endpoint #

def test_get_component_by_criteria_success():
    response = client.get("/components/search?type=w1&install_timestamp=2022-06-22")
    assert response.status_code == 200
    print(response.json())
    assert isinstance(response.json(), list)

def test_get_component_by_criteria_no_results():
    response = client.get("/components/search?type=type&install_timestamp=2050-06-22")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"]["error_code"] == "404_NO_COMPONENTS_FOUND"
    assert "message" in data["detail"]
    

def test_get_component_by_criteria_internal_error(mocker):
    mocker.patch(
        "src.routes.route.ComponentController.get_component_by_criteria",
        side_effect=Exception("Erro forçado")
    )

    response = client.get("/components/search?type=w1&install_timestamp=2022-06-22")

    assert response.status_code == 500
    body = response.json()

    assert body["detail"]["error_code"] == "500_INTERNAL_SERVER_ERROR"
    assert "message" in body["detail"]  
