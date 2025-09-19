from pgmagick.api import Image

img = Image('2.png')

# scaling image up to 1.5x
img.scale((150, 100), 'fox_scaled')