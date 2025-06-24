import numpy as np
import librosa

# Extract features
def extract_features_for_prediction(audio_path):
    """提取與訓練時相同的26維特徵，使用3秒片段"""
    try:
        # 載入音頻檔案
        y, sr = librosa.load(audio_path, sr=22050)
        
        # 計算可以切成幾個3秒片段
        segment_length = sr * 3  # 3秒的樣本數
        num_segments = len(y) // segment_length
        
        if num_segments == 0:
            # 如果音頻長度不足3秒，補零
            y = np.pad(y, (0, segment_length - len(y)), 'constant')
            num_segments = 1
        
        # 儲存所有片段的特徵
        all_features = []
        
        # 處理每個3秒片段
        for i in range(num_segments):
            start = i * segment_length
            end = start + segment_length
            segment = y[start:end]
            
            features = []
            
            # 1. chroma_stft
            chroma_stft = librosa.feature.chroma_stft(y=segment, sr=sr)
            features.append(np.mean(chroma_stft))
            
            # 2. rmse (使用 rms)
            rms = librosa.feature.rms(y=segment)
            features.append(np.mean(rms))
            
            # 3. spectral_centroid
            spectral_centroid = librosa.feature.spectral_centroid(y=segment, sr=sr)
            features.append(np.mean(spectral_centroid))
            
            # 4. spectral_bandwidth
            spectral_bandwidth = librosa.feature.spectral_bandwidth(y=segment, sr=sr)
            features.append(np.mean(spectral_bandwidth))
            
            # 5. rolloff
            rolloff = librosa.feature.spectral_rolloff(y=segment, sr=sr)
            features.append(np.mean(rolloff))
            
            # 6. zero_crossing_rate
            zcr = librosa.feature.zero_crossing_rate(segment)
            features.append(np.mean(zcr))
            
            # 7-26. mfcc1 到 mfcc20
            mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=20)
            for j in range(20):
                features.append(np.mean(mfcc[j]))
            
            all_features.append(features)
        
        # 計算所有片段特徵的平均值
        mean_features = np.mean(all_features, axis=0)
        return mean_features.reshape(1, -1)
        
    except Exception as e:
        print(f"特徵提取失敗: {e}")
        return None