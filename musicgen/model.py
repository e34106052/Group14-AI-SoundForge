import torch
import torch.nn as nn

# ### 音樂風格分辨器模型
# Define classifier
class GenreClassifier(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, 1024),  # 增加第一層神經元
            nn.ReLU(),
            nn.Dropout(0.6),              # 降低Dropout
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, 10)
        )

        
    def forward(self, x):
        return self.layers(x)