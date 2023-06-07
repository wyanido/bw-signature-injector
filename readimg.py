import os
from PIL import Image

grayscale = True
filename = "image.png"

# Grab in-game accurate palette list from image
palette = Image.open("grayscale.bmp" if grayscale else "palette.bmp")
palette_rgb = Image.open("palette.bmp").convert('RGB')
colours = []

for y in range(0, palette_rgb.height):
	for x in range(0, palette_rgb.width):
		colours.append(palette_rgb.getpixel((x, y)))

# Convert target image into the correct dimensions
with Image.open(filename) as image:
	(width, height) = (192, 64)
	image = image.resize((width, height))
	image = image.convert(mode="RGB", colors=256)
	image = image.quantize(palette=palette)
	image_rgb = image.convert('RGB').load()

# Iterate through image pixels
for yy in range(0, 8):
	for xx in range(0, 24):
		for y in range(0, 8):
			for x in range(0, 8):
				# Get index of current colour in game palette
				col = image_rgb[(xx * 8) + x, (yy * 8) + y]
				val = colours.index(col)
				
				# Convert to Hex and print
				px = f"{val:x}".upper()
				hex_byte = "0" + px if len(str(px)) == 1 else px
				print(f'{hex_byte} ', end = '')

# Hold window open for copy-pasting & don't interfere with hex output
k = input("")