from mcpi.minecraft import Minecraft

mc = Minecraft.create("minecraft-server")

block = 24 # sandstone
height = 50
levels = range(height)
mc.postToChat(levels)
levels = reversed(levels)
#mc.postToChat(levels)

pos = mc.player.getTilePos()
print(f'Original player pos: {pos}')
x, y, z = pos.x + height + 10, pos.y, pos.z
#print(f'Player pos: {x}, {y}, {z}')

for level in levels:
    print(level)
    print 
    x1 = x - level
    y1 = y
    z1 = z - level
    print(f'{x1}, {y1}, {z1}')

    x2 = x + level
    y2 = y
    z2 = z + level
    print(f'{x2}, {y2}, {z2}')

    mc.setBlocks(x1, y1, z1, x2, y2, z2, block)
    y += 1