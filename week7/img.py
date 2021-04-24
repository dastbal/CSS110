from PIL import Image
img = Image.open('./beach.jpg')
pimg= img.load()
for x in range(10,15):
    for y in range(100,150):
        pimg[x,y]=(0,0,0)
for x in range(20,60):
    for y in range(100,105):
        pimg[x,y]=(255,255,255)
for x in range(20,60):
    for y in range(145,150):
        pimg[x,y]=(255,0,0)
for x in range(60,65):
    for y in range(100,150):
        pimg[x,y]=(1,1,255)
# for x in range(1,400):
#     for y in range(1,400):
#         pimg[x,y]=(0,0,0)
# for x in range(401,800):
#     for y in range(401,600):
#         pimg[x,y]=(255,255,255)
# for x in range(401,800):
#     for y in range(1,400):
#         pimg[x,y]=(255,0,0)
# for x in range(1,400):
#     for y in range(401,600):
#         pimg[x,y]=(1,1,255)
img.show()
print(img.size)

