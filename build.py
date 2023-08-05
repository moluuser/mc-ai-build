import os.path
import pickle

from mcpi.minecraft import Minecraft
from color import get_block_from_rgb
from image2point import get_point_cloud_from_image
from point_e.util.plotting import plot_point_cloud
from text2point import get_point_cloud_from_text

# Offset of the grid drawn in Minecraft
Z_OFFSET = 10
# Object size of the grid drawn in Minecraft
SIZE = 100
# Prompt to draw in Minecraft, leave empty to draw an image
PROMPT = ''
# Path to the image to draw in Minecraft
IMAGE_PATH = 'images/duck.png'


def main():
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

        print(_y, _z, _x)

        offset = 0
        if SIZE > 16:
            offset = SIZE // 33
        for xx in range(-offset, offset + 1):
            for yy in range(-offset, offset + 1):
                for zz in range(-offset, offset + 1):
                    mc.setBlock(y + _y + yy, z + _z + zz, x + _x + xx, mc_block[1], mc_block[3])


if __name__ == '__main__':
    main()
