import torch

print(torch.__version__)

# 检查是否有可用的 GPU
if torch.cuda.is_available():
    print("CUDA is available.")
    # 获取 CUDA 版本信息
    cuda_version = torch.version.cuda
    print(f"CUDA version: {cuda_version}")
    # 获取 GPU 设备名称
    gpu_name = torch.cuda.get_device_name(0)
    print(f"GPU device name: {gpu_name}")
else:
    print("CUDA is not available.")
