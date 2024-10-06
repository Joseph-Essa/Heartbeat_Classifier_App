# Heartbeat Classifier App

## Overview
The Heartbeat Classifier App is a machine learning application that analyzes ECG images to classify heartbeats into normal and various types of arrhythmias. The application employs a two-step classification process to ensure accurate diagnosis.

## Application Structure
- 🖥️ **Backend**: FastAPI
- 🎨 **Frontend**: Qt Designer
- 📊 **Models**:
  - 🔍 **Binary Classification Model**: XGBClassifier to detect if the heartbeat is normal or abnormal.
  - 🏷️ **Multiclass Classification Model**: Random Forest to classify abnormal heartbeats into one of the following categories:
    - Normal (N)
    - Supraventricular Premature Beat (S)
    - Ventricular Premature Beat (V)
    - Fusion of Ventricular and Normal Beat (F)
    - Unknown Beat (Q)

## Datasets
- 📚 **Training Dataset**: Heartbeat Dataset
- 🧪 **Testing Dataset**: ECG Image Data  
  **Note**: The training dataset is imbalanced, which is why a two-model approach was utilized for improved classification performance.

## Features
- 📤 Image upload for heartbeat analysis.
- ⚙️ Extraction of 187 features from ECG images.
- 📈 Visualization of heartbeat patterns.
- ⏳ GIF indicator to show the program's processing status.

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

2. Launch the Qt Designer frontend to upload ECG images for classification.

## Visualizations
- **Visualization of a heartbeat pattern.**
  ![Heartbeat Pattern Visualization](path/to/heartbeat_pattern_image.png)

- **Example image showing one heartbeat.**
  ![Example Heartbeat Image](path/to/example_heartbeat_image.png)

- **GIF indicating program is running.**
  ![Processing GIF](path/to/processing.gif)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- 📊 Kaggle for the datasets.
- 🚀 FastAPI for the backend framework.
- 🎨 Qt Designer for frontend design.
