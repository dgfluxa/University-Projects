#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include "color.h"
#include <math.h>

/** Inicializa un color dentro de los rangos establecidos */
Color color_init(uint8_t R, uint8_t G, uint8_t B)
{
	return (Color)
	{
		.R = (double)R/255.0,
		.G = (double)G/255.0,
		.B = (double)B/255.0,
	};
}