from drawbot_skia.drawbot import rect
from drawbot_skia.drawbot import saveImage

x = 150

step = 150

for i in range(5):
    rect(x, 400, 100, 100)
    x = x + step

saveImage("output-02.pdf")