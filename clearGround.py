from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

mc.setBlocks(-200, 0, -200, 200, -5, 200, block.GRASS.id)

mc.setBlocks(-200, 1, -200, 200, 50, 200, block.AIR.id)
