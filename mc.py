import time

from mcpi.minecraft import Minecraft

print("connect to MC...")
mc = Minecraft.create()
mc.postToChat("Hello Minecraft World")
x, y, z = mc.player.getTilePos()
print("player pos: ", x, y, z)

for i in range(16):
    mc.setBlock(x + 3, y, z + i, 35, i)
    time.sleep(0.5)
