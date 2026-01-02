from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

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


# def test_get_component_internal_error(mocker):
#     mocker.patch(
#         "src.controller.component_controller.ComponentController.get_component_by_id",
#         side_effect=Exception("Erro forçado")
#     )

#     response = client.get("/components/0")
#     print("entrei aqui 3")
#     assert response.status_code == 500

