from PIL import Image

#opening the image
im1 = Image.open('A.png')
im2 = Image.open('B.png')
im3 = Image.open('C.png')

# Resizing all image with the same height and width
new_height = 680
new_width  = 680
im1 = im1.resize((new_width, new_height), Image.ANTIALIAS)
im2 = im2.resize((new_width, new_height), Image.ANTIALIAS)
im3 = im3.resize((new_width, new_height), Image.ANTIALIAS)

#appending image and saving to form a .gif
im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=1000, loop=0)