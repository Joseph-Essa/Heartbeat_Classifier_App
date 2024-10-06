from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import joblib


app = FastAPI()

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
 
    if file is None:
        return JSONResponse(content={"error": "No file uploaded"}, status_code=400)
    
    if not file.content_type.startswith('image/'):
        return JSONResponse(content={"error": "File is not an image"}, status_code=400)
    
    image = Image.open(io.BytesIO(await file.read()))
    image = np.array(image)
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    signal_pixels = []
    for x in range(thresholded.shape[1]):
        y = np.argmax(thresholded[:, x])
        if thresholded[y, x] == 255: 
            signal_pixels.append(y)

    signal_data = np.array(signal_pixels)

    min_value = np.min(signal_data)
    max_value = np.max(signal_data)
    normalized_signal_data = 1-((signal_data - min_value) / (max_value - min_value))

    num_features = 187
    if len(normalized_signal_data) > num_features:
        indices = np.linspace(0, len(normalized_signal_data) - 1, num_features).astype(int)
        extracted_features = normalized_signal_data[indices]
    else:
        extracted_features = normalized_signal_data
    
    model_B = joblib.load(r"D:\FCAI\NTI\Tech\Day_6\Heartbeat_ Classifier_App\binary_classification_model.pkl")
    model_M = joblib.load(r"D:\FCAI\NTI\Tech\Day_6\Heartbeat_ Classifier_App\multiclass_classification_model.pkl")

    test_sample = extracted_features.reshape(1,-1)

    predictions_B = model_B.predict(test_sample)

    if predictions_B == 1 :
        return JSONResponse(content={"message": "Normal beat"})
        
    else :
        predictions_M = model_M.predict(test_sample)
        if predictions_M == 0 : 
            return JSONResponse(content={"message": "Supraventricular beat"})
        elif predictions_M == 1 : 
            return JSONResponse(content={"message": "Ventricular beat"})
        elif predictions_M == 2 : 
            return JSONResponse(content={"message": "Fusion beat"})
        elif predictions_M == 3 : 
            return JSONResponse(content={"message": "Unknown beat"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
