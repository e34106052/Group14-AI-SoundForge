# Imports for prediction module

# ## MusicGen 音樂生成及預測系統
import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import librosa
import warnings
from .features import extract_features_for_prediction
from .model import GenreClassifier

warnings.filterwarnings('ignore')
# 設定隨機種子
SEED = 12
torch.manual_seed(SEED)
np.random.seed(SEED)
# 載入資料與預處理
data = pd.read_csv('data_features.csv')
X = data.drop(['filename', 'label'], axis=1).values
# 標準化 (使用原 notebook 相同邏輯)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Predict genre
def predict_music_genre(audio_path, model, scaler):
    """預測音樂風格"""
    
    # 音樂類型標籤 (與訓練時相同順序)
    genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 
              'jazz', 'metal', 'pop', 'reggae', 'rock']
    
    # 提取特徵
    features = extract_features_for_prediction(audio_path)
    
    if features is None:
        return None, None, None
    
    # 標準化特徵 (使用訓練時的 scaler)
    features_scaled = scaler.transform(features)
    
    # 轉換為 PyTorch tensor
    features_tensor = torch.tensor(features_scaled, dtype=torch.float32).to(device)
    
    # 預測
    model.eval()
    with torch.no_grad():
        outputs = model(features_tensor)
        probabilities = torch.softmax(outputs, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0, predicted_class].item()
    
    predicted_genre = genres[predicted_class]
    all_probabilities = probabilities[0].cpu().numpy()
    
    return predicted_genre, confidence, all_probabilities

# 載入最佳模型
# 初始化模型
# Load pretrained model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GenreClassifier(input_size=X.shape[1]).to(device)
model.load_state_dict(torch.load('best_model.pth'))
model.eval()