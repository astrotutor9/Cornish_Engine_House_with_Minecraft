from mcpi import minecraft
from time import sleep
from random import randint
from mcpi import block
# place blocks with block.NAME.id

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getTilePos()

# Place a standing on block
#mc.setBlock(x, y-1, z, 22)

# Build basic block for chimney 3 x 3 x 12
mc.setBlocks(x+10, y, z, x+10+2, y+12, z+2, 4) # Cobblestone

# Place brick top to chimney
mc.setBlocks(x+10, y+13, z, x+10+2, y+19, z+2, 45) # Brick top

# Make it hollow like a chimney
mc.setBlocks(x+11, y, z+1, x+11, y+19, z+1, 0) # Air middle



# Place a basic cobblestone block house down and hollow it out
mc.setBlocks(x+2, y, z+3, x+10, y+10, z+9, 4) # Cobblestone
mc.setBlocks(x+3, y, z+4, x+9, y+10, z+8, 0) # Air

# Windows Front
mc.setBlocks(x+2, y+4, z+5, x+2, y+6, z+7, 0)

# Window Side 1
mc.setBlocks(x+5, y+4, z+3, x+7, y+6, z+3, 0)
mc.setBlock(x+6, y+7, z+3, 0)

# Window Side 2
mc.setBlocks(x+5, y+4, z+9, x+7, y+6, z+9, 0)
mc.setBlock(x+6, y+7, z+9, 0)

# back door
mc.setBlocks(x+10, y, z+6, x+10, y+1, z+6, 64) # Door_wood

# Roof
# y+1 each level, z+1 from left, z-1 from right
height = 11
change_width_by = 0
while height < 16:
    mc.setBlocks(x+2, y+height, z+2+change_width_by, x+10, y+height, z+10-change_width_by, 98) # Stonebricks
    height += 1
    change_width_by += 1

# Shaft for water extraction
mc.setBlocks(x-1, y-1, z+5, x-3, y-6, z+7, 0)
mc.setBlocks(x-1, y-7, z+5, x-3, y-20, z+7, 8) # water


# Beam Engine
mc.setBlocks(x+4, y+8, z+6, x-2, y+8, z+6, 5) # Woodenplank
mc.setBlocks(x-2, y-6, z+6, x-2, y+7, z+6, 107) # Fencegate

# Lets start mining!

# Dig down
# y-1 each step down x-1 move forward

depth = 1
step = 0
adit_length = 0
while depth < 100:
    mc.setBlocks(x+4+step, y-depth, z+5, x+7+step, y-depth, z+7, 0)
    if depth%4 == 0:
        for adit_length in range(0,50):
            mc.setBlocks(x+4+step, y-depth, z+7+adit_length, x+5+step, y+1-depth, z+6+adit_length, 0)
            mc.setBlocks(x+4+step, y-depth, z+4-adit_length, x+5+step, y+1-depth, z+5-adit_length, 0)
    depth += 1
    step += 1

