from drawbot_skia.drawbot import oval, saveImage, fill

x = 150
step = 100

fill(1, 0, 0)

for i in range (10):

    oval(300, x, 150, 100)
    x = x + step

saveImage('task_1.pdf')
