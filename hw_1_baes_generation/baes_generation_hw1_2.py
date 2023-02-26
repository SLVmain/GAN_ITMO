import cv2
import glob
import os
import numpy as np
from PIL import Image
from collections import Counter
import random
from tqdm import tqdm

img_path = 'avatars'
full_pathes = glob.glob(os.path.join(img_path, '*png'))

img = cv2.imread(full_pathes[0], 1) # 1 - без альфа-канала
print(type(img))

print(img.shape)

print(img[0,0,:])

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image так как очень долго считает полный размер
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',img.shape)


img_h = img.shape[0]
img_w = img.shape[1]
img_ch = img.shape[2]
num_img = len(full_pathes)

print(img_h, img_w, img_ch, num_img)
n = 0
ppxh = []
for h in tqdm(range(img_h)):
    ppxw = []
    for w in range(img_w):
        ppxch = []
        for ch in range(img_ch):
            px_list =[]
            for im in range(num_img):
                iii = full_pathes[im]
                iii = cv2.imread(iii, 1)
                iii = cv2.resize(iii, dim, interpolation = cv2.INTER_AREA)
                #print(h, w, ch)
                #print(iii[h, w, ch])
                px_list.append(iii[h, w, ch])
            
            cnt = Counter(px_list)
            for k in cnt:
                cnt[k] = cnt[k] / 11
            
            res = random.choices(list(cnt.keys()), weights=cnt.values())[0]
            
            ppxch.append(res)
            
        print(ppxch)
        ppxw.append(ppxch)
    
    ppxh.append(ppxw)

ppxh = np.array(ppxh)
print(ppxh.shape)

cv2.imwrite(f"ppxh1.jpg", ppxh)

cv2.imshow("Generated image", ppxh)
cv2.waitKey(0)
cv2.destroyAllWindows()