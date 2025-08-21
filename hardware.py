# hardware.py

import torch

def get_best_device():
    """
    Detects and returns the best available device for inference.
    Priority: CUDA > CPU
    """
    if torch.cuda.is_available():
        print("✅ NVIDIA CUDA GPU detected. Using CUDA.")
        return 'cuda'
    
    print("ℹ️ No CUDA GPU found. Falling back to CPU.")
    return 'cpu'