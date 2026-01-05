from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

### Tests for simulate_series endpoint ###


# Test to simulate_series endpoint with status 200
def test_simulate_series_success():
    response = client.get("/components/1/simulation")
    assert response.status_code == 200
    assert response.headers["Content-Disposition"] == "attachment; filename=out.json"
    assert response.headers["content-type"] == "application/json"

# Test to simulate_series endpoint with status 422 for negative ID
def test_simulate_series_invalid_component_id():
    response = client.get("/components/-1/simulation")
    assert response.status_code == 422 

# Test to simulate_series endpoint with status 404
# Not applicable since the endpoint returns the same json for any component_id in the MVP


# Test to simulate_series endpoint with status 500
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
