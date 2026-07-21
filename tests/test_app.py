from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_them_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
