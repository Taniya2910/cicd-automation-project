from fastapi import FastAPI

app = FastAPI(title="GitLab CI/CD Assignment")

@app.get("/")
def home():
    return {"message": "My GitLab CI/CD application"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.get("/info")
def app_info():
    return {
        "application": "CI/CD Automation Project",
        "platform": "FastAPI",
        "status": "running"
    }