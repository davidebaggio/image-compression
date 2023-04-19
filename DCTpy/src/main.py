from image_compression import *

filepath = str(input("Image filepath: "))
image = get_image(filepath)
block_size = int(input("Block size: "))
image = img_resize(image, block_size)
if filepath != "./img/ycrcb.ycrcb":
    image = color2YCrCb(image)

L = float(input("Parameter of quantization for luminance: "))
while L <= 0 or L >= 100:
    L = float(input("This value must be in range (0, 100): "))

C = float(input("Parameter of quantization for crominance: "))
while C <= 0 or C >= 100:
    C = float(input("This value must be in range (0, 100): "))

mse_1, psnr_1 = img_comp(image, block_size, [L, C], info=True)
print("MSE: %s" % mse_1)
print("PSNR: %s" % psnr_1)

jumps = [10, 20, 30, 40, 50, 60, 70, 80, 92, 94, 96, 98, 99]
mse = []
psnr = []

for i in jumps:
    print("Compression parameter R= %s ..." % i)
    m, p = img_comp(image, block_size, [i, i])
    mse.append(m)
    psnr.append(p)

for i in range(len(jumps)):
    mse[i] = round(mse[i], 3)
    psnr[i] = round(psnr[i], 3)

fig, (ax1, ax2) = plt.subplots(2)
ax1.set_title("MSE " + str(block_size) + "x" + str(block_size))
ax1.set_xlabel("R%")
for i, txt in enumerate(mse):
    ax1.annotate(txt, (jumps[i], mse[i]))
ax2.set_title("PSNR " + str(block_size) + "x" + str(block_size))
ax2.set_xlabel("R%")
ax2.set_ylabel("dB")
for i, txt in enumerate(psnr):
    ax2.annotate(txt, (jumps[i], psnr[i]))
ax1.plot(jumps, mse, '-o')
ax2.plot(jumps, psnr, '-o')
plt.show()
