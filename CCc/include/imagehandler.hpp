#ifndef IMAGE_LOADER_H
#define IMAGE_LOADER_H

#define SDL_MAIN_HANDLED
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

void RGBtoYCbCr(Uint8, Uint8, Uint8, Uint8 &, Uint8 &, Uint8 &);
void convertRGBtoYCbCr(SDL_Surface *, SDL_Surface *);

#endif