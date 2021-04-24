from PIL import Image
earth = Image.open('./earth.jpg')
p_earth = earth.load()
cactus = Image.open('./cactus.jpg')
p_cactus = cactus.load()
my_img_1 = Image.new('RGB', cactus.size)
p_my_img_1 = my_img_1.load()
x = 0
y = 0

# first image
for x in range(800):
    for y in range(600):
        (r, g, b) = p_cactus[x, y]
        if r < 110 and g > 200 and b < 50:
            p_my_img_1[x, y] = p_earth[x, y]
        else:
            p_my_img_1[x, y] = p_cactus[x, y]

my_img_1.show()


# Second image

background = Image.open('./desert.jpg')
p_background = background.load()
my_img_2 = Image.new('RGB', cactus.size)
p_my_img_2 = my_img_2.load()
for x in range(800):
    for y in range(600):
        (r, g, b) = p_cactus[x, y]
        if r < 110 and g > 200 and b < 50:
            p_my_img_2[x, y] = p_background[x, y]
        else:
            p_my_img_2[x, y] = p_cactus[x, y]

my_img_2.show()

# thrid image


cat = Image.open('./cat.jpg')
p_cat = cat.load()
my_img_3 = Image.new('RGB', cactus.size)
p_my_img_3 = my_img_3.load()

for x in range(800):
    for y in range(600):
        (r, g, b) = p_cat[x, y]
        if r < 110 and g > 220 and b < 50:
            p_my_img_3[x, y] = p_background[x, y]
        else:
            p_my_img_3[x, y] = p_cat[x, y]

my_img_3.show()

# seving a new image
name = input('the to save the image of the cat in the desert: ')
name = './' + name + '.jpg'
my_img_3.save(name)

c = Image.open(name)
c.show()
