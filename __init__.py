import os

user = input()
try:
    import numpy as np
    from PIL import Image
    import default
    wc = default.data_create(width=800, hight=800, user=user, mask=img_array)
    img = Image.open('./sampleImage/img.jpg')
    img_array = np.array(img)
    default.image_show(wc=wc)

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')
