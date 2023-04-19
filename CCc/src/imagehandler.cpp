#include "imagehandler.hpp"

void RGBtoYCbCr(Uint8 r, Uint8 g, Uint8 b, Uint8 &Y, Uint8 &Cb, Uint8 &Cr)
{
	Y = 0.299 * r + 0.587 * g + 0.114 * b;
	Cb = 128 - 0.168736 * r - 0.331264 * g + 0.5 * b;
	Cr = 128 + 0.5 * r - 0.418688 * g - 0.081312 * b;
}

void convertRGBtoYCbCr(SDL_Surface *src, SDL_Surface *dest)
{

	// locking surfaces to easily access the pixels
	SDL_LockSurface(src);
	SDL_LockSurface(dest);

	int w = src->w;
	int h = src->h;
	Uint32 *srcPixels = (Uint32 *)src->pixels;
	Uint32 *destPixels = (Uint32 *)dest->pixels;

	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			Uint32 pixel = srcPixels[y * w + x];
			Uint8 R = (pixel >> 16) & 0xFF;
			Uint8 G = (pixel >> 8) & 0xFF;
			Uint8 B = pixel & 0xFF;

			Uint8 Y, Cb, Cr;
			RGBtoYCbCr(R, G, B, Y, Cb, Cr);

			destPixels[y * w + x] = SDL_MapRGB(dest->format, Cr, Cb, Y);
		}
	}

	SDL_UnlockSurface(src);
	SDL_UnlockSurface(dest);
}

void convertRGBtoYCbCrPrev(SDL_Surface *src, SDL_Surface *dest)
{

	// locking surfaces to easily access the pixels
	SDL_LockSurface(src);
	SDL_LockSurface(dest);

	int w = src->w;
	int h = src->h;

	Uint32 *destPixels = (Uint32 *)dest->pixels;

	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			Uint8 r, g, b;
			SDL_GetRGB(*(Uint32 *)((Uint8 *)src->pixels + y * src->pitch + x * 4), src->format, &r, &g, &b);

			Uint8 Y, Cb, Cr;
			RGBtoYCbCr(r, g, b, Y, Cb, Cr);

			Uint8 pix[4] = {Y, Cb, Cr, 0};
			// destPixels[y * w + x] = (Y << 16) | (Cb << 8) | (Cr << 0);
			destPixels[y * w + x] = *(Uint32 *)pix;

			/* *(Uint8 *)((Uint8 *)dest->pixels + y * dest->pitch + x * 3) = Y;
			 *(Uint8 *)((Uint8 *)dest->pixels + (y + 1) * dest->pitch + x * 3) = Cb;
			 *(Uint8 *)((Uint8 *)dest->pixels + (y + 2) * dest->pitch + x * 3) = Cr; */
		}
	}

	SDL_UnlockSurface(src);
	SDL_UnlockSurface(dest);
}