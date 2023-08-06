import os.path
import pickle
import time

from mcpi.minecraft import Minecraft
from color import get_block_from_rgb
from image2point import get_point_cloud_from_image
from point_e.util.plotting import plot_point_cloud
from text2point import get_point_cloud_from_text

# Offset of the grid drawn in Minecraft
Y_OFFSET = 100
# Object size of the grid drawn in Minecraft
SIZE = 50
# Prompt to draw in Minecraft, leave empty to draw an image
PROMPT = ''
# Path to the image to draw in Minecraft
IMAGE_PATH = 'images/chick.jpg'
# Number of objs to draw in Minecraft
COUNT = 1


def main():
    time.sleep(3)
    print('connect to Minecraft...')
    mc = Minecraft.create()
    mc.postToChat('Hello Minecraft')
    y, z, x = mc.player.getTilePos()
    print('player pos:', y, z, x)

    if PROMPT != '':
        name = PROMPT + '.pkl'
        pc_path = os.path.join('pcs/text', name)
    else:
        name = os.path.splitext(os.path.basename(IMAGE_PATH))[0] + '.pkl'
        pc_path = os.path.join('pcs/image', name)

    if os.path.exists(pc_path):
        print('load point cloud...')
        with open(pc_path, 'rb') as f:
            pc = pickle.load(f)
    else:
        print('draw point cloud...')
        if PROMPT != '':
            pc = get_point_cloud_from_text(PROMPT)
        else:
            pc = get_point_cloud_from_image(IMAGE_PATH)
        with open(pc_path, 'wb') as f:
            pickle.dump(pc, f)

    print('draw in Minecraft...')
    fig = plot_point_cloud(pc, grid_size=3, fixed_bounds=((-0.75, -0.75, -0.75), (0.75, 0.75, 0.75)))
    fig.show()

    for i in range(len(pc.coords)):
        # Color
        r = int(pc.channels['R'][i] * 255)
        g = int(pc.channels['G'][i] * 255)
        b = int(pc.channels['B'][i] * 255)

        mc_block = get_block_from_rgb((r, g, b))
        print(mc_block)

        # Position
        _x, _y, _z = pc.coords[i]

        # -0.5~0.5 -> 0~1
        _x += 0.5
        _y += 0.5
        _z += 0.5

        _x *= SIZE
        _y *= SIZE
        _z *= SIZE

        _y += Y_OFFSET

        print(_y, _z, _x)

        offset = 0
        if SIZE > 16:
            offset = SIZE // 33

        count = COUNT
        for cc in range(-count + 1, count):
            for xx in range(-offset, offset + 1):
                for yy in range(-offset, offset + 1):
                    for zz in range(-offset, offset + 1):
                        mc.setBlock(y + _y + yy, z + _z + zz, x + _x + xx + SIZE * cc * 1.2, mc_block[1], mc_block[3])


if __name__ == '__main__':
    main()
