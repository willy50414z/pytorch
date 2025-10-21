import numpy as np
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

for i in range(10):
    writer.add_scalar("y=5x", 5*i, i)

img_PIL = Image.open("imgs/S__101490696.jpg")
img_arrary = np.array(img_PIL)

print(type(img_arrary))
print(img_arrary.shape)

writer.add_image("img", img_arrary, 1, dataformats="HWC")

writer.close()

# tensorboard.exe --logdir=logs