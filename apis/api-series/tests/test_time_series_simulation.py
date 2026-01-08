from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)

# Tests for simulate_series endpoint #

def test_simulate_series_success():
    response = client.get("/components/1/simulation")
    assert response.status_code == 200
    assert response.headers["Content-Disposition"] == "attachment; filename=out.json"
    assert response.headers["content-type"] == "application/json"



def test_simulate_series_invalid_component_id():
    response = client.get("/components/-1/simulation")
    assert response.status_code == 422 
    

@pytest.mark.skip(reason="MVP returns same JSON for any component_id")
def test_simulate_series_404():
    """
    Test for the /simulate_series endpoint expecting HTTP 404.

    This test is currently not applicable because, in the MVP,
    the endpoint returns the same JSON response for any component_id.
    """


def test_simulate_series_internal_error(mocker):
    mocker.patch(
        "src.routes.route.SimulationController.stream_data",
        side_effect=Exception("Erro forçado")
    )

    response = client.get("/components/1/simulation")

  
    assert response.status_code == 500
    body = response.json()

    assert body["detail"]["error_code"] == "500_INTERNAL_SERVER_ERROR"
    assert "message" in body["detail"]
