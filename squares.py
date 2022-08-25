import os
from PIL import Image
jpgs = [f for f in os.listdir("./data/jpgs") if f.endswith("jpg")]
if not os.path.exists("./data/squares"):
    os.makedirs("./data/squares")

for jpg in jpgs:
    print(jpg)
    im = Image.open("./data/jpgs/%s" % jpg)
    w = im.size[0]
    h = im.size[1]
    # crop to square
    if w>h:
        im = im.crop((w/8, 0, w-w/8, h))
    else:
        im = im.crop((0, h/8, w, h-h/8))
    if im.size[0] != im.size[1]:
        print("problem with %s" % jpg)

    # OK, we have a square picture, now take every 400x400 block
    for i in range(0, (im.size[0] // 400) -1):
        for j in range(0, (im.size[1] // 400) -1):
            out = im.crop((i*400, j*400, i*400+400, j*400+400))
            out = out.resize((64,64))
            outname = jpg.replace("_o","_s_%s_%s" % (i, j))
            out.save("./data/squares/%s" % outname)
