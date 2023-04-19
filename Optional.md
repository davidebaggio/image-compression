## Optional

### CCc

This section is written in C++. It is an optional feature of the entire project that basically allows you to convert an image (JPEG and PNG formats) from RGB to YCbCr color space with the use of SDL2 and SDL2_image libraries.

## Instructon

### CCc

This optional section of the project uses SDL2 for color space transormation. It doesn't perform the discrete cosine transformation or quantization of the image. On windows all packages are already present in the workspace folder.
In linux:

```console
$ sudo apt-get install libsdl2-dev
$ sudo apt-get install libsdl2-image-dev
```

#### With Make

```console
$ cd CCc
$ make all
```

#### Without Make

Linux:

```console
$ cd CCc
$ g++ -std=c++17 -I./include -I./SDL2/include -Wall -Wextra -c ./src/imagehandler.cpp -lSDL2 -lSDL2main -lSDL2_image -o ./build/imagehandler.o
$ ar ruv ./build/lib/libimg.a ./build/imagehandler.o
$ ranlib ./build/lib/libimg.a
$ g++ -std=c++17 -I./include -I./SDL2/include -Wall -Wextra ./tests/main.cpp ./build/lib/libimg.a -lSDL2 -lSDL2main -lSDL2_image -o ./build/executable/main

$ ./build/executable/main
```

Windows:

```console
$ cd CCc
$ g++ -std=c++17 -I./include -I./SDL2/include -Wall -Wextra -Wpedantic -c ./src/imagehandler.cpp -o ./build/imagehandler.o -lSDL2 -lSDL2main -lSDL2_image -L./SDL2/lib
$ ar ruv ./build/lib/libimg.a ./build/imagehandler.o
$ ranlib ./build/lib/libimg.a
$ g++ -std=c++17 -I./include -I./SDL2/include -Wall -Wextra -Wpedantic ./tests/main.cpp ./build/lib/libimg.a -lSDL2 -lSDL2main -lSDL2_image -L./SDL2/lib -o ./build/executable/main

$ ./build/executable/main
```

This section creates an image with YCbCr color space named "ycrcb.ycrcb" in the image folder of the parent workspace. Then run DCTpy section on this image to perform DCT and quantization.

## Example CCc

Considering:

- image = ../img/lettuce.jpeg `# ../ because we are in CCc folder`

```console
$ cd CCc
$ make all

# image ycrcb.ycrcb will be saved into "img" folder
# now we can perform DCTpy directly

$ cd ..
$ make exe
$ Image filepath: ./img/ycrcb.ycrcb
$ ...
$ ...
```
