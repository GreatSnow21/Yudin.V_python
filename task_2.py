from drawbot_skia.drawbot import oval, saveImage, fill

x = 90
step = 150

fill(200, 200, 0)

for i in range(10):
    y = 40
    for z in range(10):
        oval(x, y, 150, 150)
        y = y + step
    x = x + step

saveImage('task_2.pdf')
