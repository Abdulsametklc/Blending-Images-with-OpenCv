import cv2

import matplotlib.pyplot as plt

#karıştırma

img1 = cv2.imread("img1.JPG")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#bu metod ile bu görüntüleri BGR renk düzeninden RGB renk düzenine çeviriyoruz.
img2 = cv2.imread("img2.JPG")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (600,600))
print(img1.shape)
img2 = cv2.resize(img2, (600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#birleştirme = alpha*img1 + beta*img2 
blended = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta =0.5, gamma =0 )
plt.figure()
plt.imshow(blended)
#cv2.addWeighted() fonksiyonu, iki görüntüyü ağırlıklandırıp birleştirir. 
#Bu satırda, img1 ve img2 görüntülerini eşit ağırlıklandırarak (alpha=0.5, beta=0.5) blended adlı yeni bir görüntü oluşturuyorsunuz. 
#Bu birleştirme sonucunda ortaya çıkan görüntüyü Matplotlib ile görselleştiriyorsunuz.


