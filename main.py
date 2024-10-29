from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(a: float, b: float):
    result = a + b  # Default operation: Sum of three numbers
    return {"a": a, "b": b, "result": result}

