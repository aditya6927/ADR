from fastapi import FastAPI

app = FastAPI(title="ADR Security Laboratory")

@app.get("/health")
def health():
    return {"status": "ok"}