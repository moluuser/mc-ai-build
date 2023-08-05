import time
from mcpi.minecraft import Minecraft

from image2point import get_point_cloud_from_image


def main():
    print('connect to Minecraft...')
    mc = Minecraft.create()
    mc.postToChat('Hello Minecraft')
    x, y, z = mc.player.getTilePos()

    print('draw point cloud...')
    pc = get_point_cloud_from_image('point_e/examples/example_data/cube_stack.jpg')
    print('draw in Minecraft...')
    for p in pc:
        mc.setBlock(x + p[0], y + p[1], z + p[2], 35, p[3])
        time.sleep(0.01)


if __name__ == '__main__':
    main()
