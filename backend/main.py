# backend/main.py
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
import os
from process import process_image_and_generate_art

app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/generate")
async def generate_art(image: UploadFile = File(...), style: str = Form(...)):
    # Save uploaded image temporarily
    upload_path = "temp_image.png"
    with open(upload_path, "wb") as f:
        f.write(await image.read())

    # Process and generate art
    output_paths = process_image_and_generate_art(upload_path, style)

    # Clean up
    os.remove(upload_path)

    # Return URLs
    response = {
        "urls": {
            "low": f"http://localhost:8000/{output_paths['low']}",
            "high": f"http://localhost:8000/{output_paths['high']}"
        }
    }
    print("Sending response:", response)  # Log for debugging
    return JSONResponse(content=response)

@app.get("/{file_path:path}")
async def serve_file(file_path: str):
    return FileResponse(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)