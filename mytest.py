import torch
import torchvision

model = torchvision.models.mobilenet_v3_large()

print(model.features)