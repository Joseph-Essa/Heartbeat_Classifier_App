# Heartbeat Classifier App

## Overview
The Heartbeat Classifier App is a machine learning application that analyzes ECG images to classify heartbeats into normal and various types of arrhythmias. The application employs a two-step classification process to ensure accurate diagnosis.

## Application Structure
- **Backend**: FastAPI
- **Frontend**: Qt Designer
- **Models**:
  - **Binary Classification Model**: XGBClassifier to detect if the heartbeat is normal or abnormal.
  - **Multiclass Classification Model**: Random Forest to classify abnormal heartbeats into one of the following categories:
    - Supraventricular Premature Beat (S)
    - Ventricular Premature Beat (V)
    - Fusion of Ventricular and Normal Beat (F)
    - Unknown Beat (Q)

## Datasets
- **Use Dataset**: [Heartbeat Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat)
- **Testing Dataset**: [ECG Image Data](https://www.kaggle.com/datasets/erhmrai/ecg-image-data)
- **Note**: The training dataset is Unbalanced, which is why a two-model approach was utilized for improved classification performance.


-    **Visualization of Unbalanced Distribution of Category.**

  ![Heartbeat Pattern Visualization](images/Screenshot%202024-10-06%20214310.png)

-    **Example image showing one heartbeat.**

  ![Example Heartbeat Image](images/Screenshot%202024-10-06%20214251.png)


## Features
- Image upload for heartbeat analysis.
- Extraction of 187 features from ECG images.
  ![Extraction](images/Screenshot%202024-10-06%20215738.png)
    ```bash
    _, thresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    signal_pixels = []
    for x in range(thresholded.shape[1]):
         y = np.argmax(thresholded[:, x])
      if thresholded[y, x] == 255: 
         signal_pixels.append(y)
    ```
- Evaluation for Binary classification to detect normal or abnormal heartbeats (XGBClassifier).

   ```bash
    Classification Report (Binary Model):
               precision    recall  f1-score   support

           0       0.94      0.94      0.94      3774
           1       0.99      0.99      0.99     18118

    accuracy                           0.98     21892
    macro avg       0.96      0.96      0.96     21892
    weighted avg       0.98      0.98      0.98     21892

    ```
- Evaluation for Multiclass classification to identify specific types of arrhythmias (Random Forest to classify).

  ```bash
    Classification Report (Multiclass Model):
               precision    recall  f1-score   support

         0.0       0.96      0.94      0.95       556
         1.0       0.96      0.97      0.97      1448
         2.0       0.83      0.88      0.85       162
         3.0       0.99      0.99      0.99      1608

    accuracy                           0.97      3774
    macro avg       0.94      0.94      0.94      3774
    weighted avg       0.97      0.97      0.97      3774
    ```
- Visualization of heartbeat patterns.

  ![Visualization](images/Screenshot%202024-10-06%20224614.png)


## Installation
1. Clone this repository:
    ```bash
    git clone <repository-url>
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Launch the Qt Designer frontend to upload ECG images for classification:
    ```bash
    python main.py
    ```
    
## Acknowledgments
- Kaggle for the datasets.
- FastAPI for the backend framework.
- Qt Designer for frontend design.
