#include <iostream>
#include "imagehandler.hpp"

#define WIDTH 410
#define HEIGHT 300

int main(int argc, char const *argv[])
{
	(void)argc;
	(void)argv;
	if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
	{
		std::cout << "SDL error\n";
	}
	if (IMG_Init(IMG_INIT_PNG) == 0)
	{
		std::cout << "Error SDL2_image Initialization";
		return 2;
	}
	SDL_Surface *image = IMG_Load("../img/lettuce.jpeg");
	if (image == NULL)
	{
		std::cout << IMG_GetError() << "\n";
		exit(0);
	}

	SDL_Surface *out = SDL_CreateRGBSurface(0, image->w, image->h, 32, 0xFF000000, 0x00FF0000, 0x0000FF00, 0x000000FF);
	convertRGBtoYCbCr(image, out);
	IMG_SaveJPG(out, "../img/ycrcb.ycrcb", 100);

	SDL_FreeSurface(image);
	SDL_FreeSurface(out);
	IMG_Quit();
	SDL_Quit();

	return 0;
}
