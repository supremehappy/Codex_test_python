# Codex_test_python

This project demonstrates a simple FastAPI application implemented with a basic MVC pattern and secure coding practices.

## Pre‑installation

1. Install Python 3.9 or higher from [python.org](https://www.python.org/downloads/).
2. Install project dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the development server using **uvicorn**:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000` by default.

Interactive API documentation powered by Swagger UI is available at
`http://127.0.0.1:8000/api/docs`.

To view the Swagger UI:

1. Ensure the server is running.
2. Open your browser and navigate to `http://127.0.0.1:8000/api/docs`.
3. Use the page to explore and test the API endpoints.

The raw OpenAPI specification can be downloaded from
`http://127.0.0.1:8000/api/v1/openapi.json`.

## API Specification

| Method | URI                     | Description                           |
|-------|------------------------|---------------------------------------|
| GET   | `/sample/getHello`     | Returns a greeting message.           |
| POST  | `/sample/postContext`  | Accepts JSON `{ "text": "..." }` and echoes it back. |

### Example Usage

**GET /sample/getHello**

```bash
curl http://127.0.0.1:8000/sample/getHello
```

Response:
```json
{"message":"Hello, world!"}
```

**POST /sample/postContext**

```bash
curl -X POST http://127.0.0.1:8000/sample/postContext \
  -H "Content-Type: application/json" \
  -d '{"text": "some text"}'
```

Response:
```json
{"message":"Received: some text"}
```

## Project Structure

```
app/
  controllers/
    sample_controller.py  # Route handlers
  models/
    sample_model.py       # Pydantic models
  main.py                 # FastAPI application instance
requirements.txt          # Dependency list
```

This structure loosely follows the MVC pattern, separating models, controllers, and the application entry point (views are implicit in the response models).
