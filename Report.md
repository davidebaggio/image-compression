## Project choises

The project contains two main folders representing two different section:

- DCTpy (the entire program for image compression)
- CCc “Color Conversion in c++” (libraries to convert a .jpeg or .png image from RGB to YCbCr color space)

Note that the DCTpy is the complete program that can run standalone. The CCc part is made in order to understand and experience how color conversion works. It is explained in [Optional.pdf](./Optional.pdf).

### DCTpy

This section is written in python because this language provides useful modules such as opencv, matplotlib and numpy. These modules are use to manage images, plot charts and manage arrays. It supports JPEG, PGM and BMP formats as required.

## Instruction

Having [GNU Make](https://www.gnu.org/software/make/) for building projects will simplify the execution of the program.
The "img" folder contains some image to test.

### DCTpy

This project requires some modules as previously stated. First of all [pip](https://www.python.org/downloads/) module installer for python needs to be installed and added to the PATH. On linux if you have python already install type `sudo apt install python3-pip`.

#### With Make

```console
$ make install
$ make exe

	# or

$ make all
```

#### Without Make

```console
$ python3 -m pip install opencv-python
$ python3 -m pip install matplotlib
$ python3 -m pip install numpy

$ python3 -B ./DCTpy/src/main.py
```

Once the program is running, it will ask to insert the filepath of the image, the block size and the parameters of quantization. It is common use to adopt higher values of percentage of quantization for crominance as the human eyes are more suited for luminance. It will show the split between the Y, Cb, Cr channels, the relative DCT, the quantization and the relative IDCT to build up the "compressed" image again. Then the program will make the same process on the same image with different values of percentage of quantization. At the end a chart of the _MSE_ and _PSNR_ will be display.

## Example DCTpy

Considering:

- image = ./img/man.jpeg
- block size = 32
- parameter of quantization for luminance = 80
- parameter of quantization for crominance: 95

```console
$ make exe

$ Image filepath: ./img/man.jpeg
$ Block size: 32
$ Parameter of quantization for luminance: 80
$ Parameter of quantization for crominance: 95

	# images of the components will be shown as demonstration (skip them by pressing any key)

$ MSE: 0.7298258867413668
$ PSNR: 49.49861097249607
$ Compression parameter R= 10 ...
$ Compression parameter R= 20 ...
$ Compression parameter R= 30 ...
$ Compression parameter R= 40 ...
$ Compression parameter R= 50 ...
$ Compression parameter R= 60 ...
$ Compression parameter R= 70 ...
$ Compression parameter R= 80 ...
$ Compression parameter R= 92 ...
$ Compression parameter R= 94 ...
$ Compression parameter R= 96 ...
$ Compression parameter R= 98 ...
$ Compression parameter R= 99 ...

	# plot of MSE and PSNR
```

For the image "./img/man.jpeg" with blocks 8x8, 16x16 and 32x32 these are the result of the progression of _MSE_ and _PSNR_ (consider that **R%** value is the same for luminance and crominance):
![](./8x8.jpeg)
![](./16x16.jpeg)
![](./32x32.jpeg)

The charts demonstrate that as the parameter of quantization **R%** increases, the _Mean Square Error_ between the channels before and after the compression increases in an exponential way, due to the fact that when the **R%** is really close to 100 most of the coefficients in the _NxN_ block matrix are set to 0. On the other side the _PSNR_ is decreasing for the same reason: the noise is getting bigger each step.

At the same time blocks of dimension 8x8 give more precision when compressing images with low values of **R%** because they represent smaller sections of the images but result in less precision (higher _MSE_) with high values of **R%** because as the DCT and quantization is performed the error propagation increases in a much faster pace (larger number of blocks per image) than other blocks dimensions.
