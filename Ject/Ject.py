from numpy import asarray
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

def RELU(Input):
    if Input > 0:
        return Input
    else:
        return 0

image = Image.open("Pic\\rgb.jpg");
Map = Image.open("Pic\\rc.jpg")

image = image.resize((72,128))
Map = Map.resize((32, 32))

array = asarray(image);
MapArray = asarray(Map)
print(array.shape)
print(MapArray.shape)

total = (array.shape[0]-MapArray.shape[0])*(array.shape[1]-MapArray.shape[1])*3
i = 0;
canvas = {}
canvas[0] = np.zeros([array.shape[0]-MapArray.shape[0], array.shape[1]-MapArray.shape[1]])
canvas[1] = canvas[0]
canvas[2] = canvas[0]
canvas[3] = canvas[0]
print("Total Section : " + str(total))
for layer in range(3):
    for xImage in range(array.shape[1]-MapArray.shape[1]):
        for yImage in range(array.shape[0]-MapArray.shape[0]):
            print("Section : " + str(yImage) + "  " + str(xImage) + " Section left : " + str(total - i))
            value = 0
            for xMap in range(MapArray.shape[0]):
                for yMap in range(MapArray.shape[1]):
                    #print(str(yMap + yImage)+"  "+ str(xMap + xImage)+"  "+ str(yMap)+"  "+ str(xMap))
                    value = RELU(MapArray[yMap][xMap][layer] - array[yMap + yImage][xMap+ xImage][layer])
            canvas[layer][yImage][xImage] = value;
            i+=1

for R1, R2, R3, R4 in zip(canvas[0], canvas[1], canvas[2], canvas[3]):
    for v1, v2, v3, v4 in zip(R1, R2, R3, R4):
        v4 = (v1+v2+v3)/3

H = canvas[3];
fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(H)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()
