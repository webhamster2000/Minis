import PIL
import random
from PIL import Image, ImageDraw

y0s = 20
m0s = 0.75
dev = 30

xrange = 500
yrange = int(xrange * m0s + y0s)

pos = []
for a in range(1, xrange):
    pos.append((a, (m0s*a + y0s) + random.gauss(0, 1) * dev))

#print(pos)

def getError(m, y0, pos):
    error = 0
    for p in pos:
        ny = m * p[0] + y0
        error += abs(p[1] - ny) 
    return error / len(pos)

m0 = 1
y0 = 0

ms = 0.1
ys = 0.1

history = []
minErrorImprovement = 0.001
run = 0

localsfound = 0

while localsfound < 20:
    run += 1
    error = getError(m0 + ms, y0, pos)
    if len(history) == 0 or error < history[-1][2]:
        m0 += ms
        history.append((m0, y0, error))
    else:
        error = getError(m0 - ms, y0, pos)
        if len(history) == 0 or error < history[-1][2]:
            m0 -= ms
            history.append((m0, y0, error))
        else:
            error = getError(m0, y0 - y0s, pos)
            if len(history) == 0 or error < history[-1][2]:
                y0 -= y0s
                history.append((m0, y0, error))
            else:
                error = getError(m0, y0 + y0s, pos)
                if len(history) == 0 or error < history[-1][2]:
                    y0 += y0s
                    history.append((m0, y0, error))
                else:
                    print("found local optima")
                    ms /= 2
                    ys /= 2
                    localsfound += 1
                    continue

    if len(history) > 1:
        if history[-1][2] < minErrorImprovement:
            print( "end: " + str(history[-1]))
            break
    if run % 25 == 0: print(str(run) + ": " + str(history[-1]))

im = Image.new("RGBA", (xrange, yrange), (255, 255, 255, 0))
draw = ImageDraw.Draw(im)
for p in pos:
    draw.ellipse((p[0]-2, yrange - (p[1]+2), p[0]+2, yrange - (p[1]-2)), fill = (128, 128, 255))

draw.line([(0, yrange - y0), (xrange, yrange - (xrange * m0 + y0))], fill = (255, 0, 0), width=2)

# write to stdout
im.show()