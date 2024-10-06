# Heartbeat Classifier App

## Overview

The Heartbeat Classifier App is a machine learning application designed to analyze heartbeat images, extract features, and classify the heartbeats based on their characteristics. The application utilizes a two-step classification process:

1. **Binary Classification**: Determines if the heartbeat is normal or abnormal.
2. **Multiclass Classification**: If the heartbeat is abnormal, it classifies the type of abnormal heartbeat into one of the following categories:
   - Normal (N)
   - Supraventricular Premature Beat (S)
   - Ventricular Premature Beat (V)
   - Fusion of Ventricular and Normal Beat (F)
   - Unknown Beat (Q)

## Technology Stack

- **Backend**: FastAPI
- **Frontend**: Qt Designer
- **Machine Learning Models**:
  - Binary Classification: XGBoost Classifier (XGBClassifier)
  - Multiclass Classification: Random Forest Classifier
- **Python Libraries**:
  - NumPy
  - Pandas
  - scikit-learn
  - XGBoost
  - Matplotlib (for visualization, if applicable)

## Datasets

- **Training Dataset**: [Heartbeat Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat) - Used for training the binary classification model.
- **Testing Dataset**: [ECG Image Data](https://www.kaggle.com/datasets/erhmrai/ecg-image-data) - Used for testing the classification models with heartbeat images.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Heartbeat_Classifier_App.git
   cd Heartbeat_Classifier_App
