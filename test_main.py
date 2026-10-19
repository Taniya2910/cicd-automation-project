from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "My GitLab CI/CD application"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_app_info():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json() == {
        "application": "CI/CD Automation Project",
        "platform": "FastAPI",
        "status": "running"
    }