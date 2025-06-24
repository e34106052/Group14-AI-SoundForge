from datetime import datetime
import scipy.io.wavfile
import os
from transformers import AutoProcessor, MusicgenForConditionalGeneration

from music_gen.predict import predict_music_genre, model, scaler
from music_gen.prompt import generate_optimized_prompts


# 載入 MusicGen 模型
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
musicgen = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

genres = list(generate_optimized_prompts().keys())

def generate_and_predict(prompt, filename, duration_tokens=1503, save_dir=None):
    # 設定儲存路徑，包含預設(C:\AI_SoundForge)
    if save_dir is None:
        save_dir = "C:\\AI_SoundForge"
        os.makedirs(save_dir, exist_ok=True)
    
    """生成音樂並進行風格預測"""
    current_time = datetime.now().strftime("%H%M")
    filename_with_time = f"{filename.rsplit('.', 1)[0]}_{current_time}.wav"
    full_path = os.path.join(save_dir, filename_with_time)

    # 生成音樂
    inputs = processor(text=[prompt], padding=True, return_tensors="pt")
    audio_values = musicgen.generate(**inputs, max_new_tokens=duration_tokens)
    sampling_rate = musicgen.config.audio_encoder.sampling_rate

    # 儲存音樂檔案
    #scipy.io.wavfile.write(filename_with_time, rate=sampling_rate, data=audio_values[0, 0].numpy())
    scipy.io.wavfile.write(full_path, rate=sampling_rate, data=audio_values[0, 0].numpy())
    print(f"已保存: {full_path}")

    # 使用風格分類器進行預測
    predicted_genre, confidence, all_probs = predict_music_genre(full_path, model, scaler)

    if predicted_genre is not None:
        return {
            "filename": full_path,
            "predicted_genre": predicted_genre,
            "confidence": confidence,
            "probabilities": all_probs
        }
    else:
        return {
            "filename": full_path,
            "predicted_genre": None,
            "confidence": None,
            "probabilities": None,
            "error": "預測失敗，請檢查音檔路徑和格式"
        }
