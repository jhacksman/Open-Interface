"""FastAPI endpoints for Molmo browser test."""
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, Response
import cv2
import numpy as np
import base64
from ..models.molmo_integration import MolmoBrowserTest
from ..config import settings

router = APIRouter()
model = MolmoBrowserTest(model_path=settings.MODEL_PATH)

@router.post("/detect", response_model=dict)
async def detect_ui_elements(file: UploadFile = File(...)):
    """Detect UI elements in uploaded image.
    
    Args:
        file: Uploaded image file
        
    Returns:
        JSON response containing detected coordinates and bounding boxes
    """
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid image file"
            )
            
        results = model.detect_ui_elements(img)
        return JSONResponse(content=results)
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )

@router.post("/detect-with-overlay")
async def detect_ui_with_overlay(file: UploadFile = File(...)):
    """Detect UI elements and return image with pink dot overlay.
    
    Args:
        file: Uploaded image file
        
    Returns:
        JSON response containing:
        - coordinates: Detected UI element coordinates
        - image: Base64 encoded image with pink dot overlay
    """
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid image file"
            )
        
        # Detect UI elements
        results = model.detect_ui_elements(img)
        
        # Draw pink dots for points
        img_with_dots = model.draw_pink_dots(img, results["points"])
        
        # Draw bounding boxes
        img_with_overlay = model.draw_bounding_boxes(img_with_dots, results["boxes"])
        
        # Convert image to base64
        _, buffer = cv2.imencode('.png', img_with_overlay)
        img_str = base64.b64encode(buffer).decode()
        
        return JSONResponse(content={
            "coordinates": results,
            "image": f"data:image/png;base64,{img_str}"
        })
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )
