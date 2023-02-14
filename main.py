import turtle
import os
import math    

if not os.path.exists("import.VECTOR"):
    with open("import.VECTOR", "r") as f: 
        exec(f"points={f.read().strip()}")
else:
    print("Custom points not found: Attempting to load default")
    if os.path.exists("default.VECTOR"):
        with open("default.VECTOR", "r") as f:
            exec(f"points={f.read().strip()}")
        print("Loaded default points")
    else:
        print("Default points not found: Stopping...")
        input()
        exit()
print(points)
if os.path.exists("import.CONF"):
    with open("import.CONF", "r") as f:
        settingsRaw = f.readlines()
    settings = []
    for setting in settingsRaw:
        settings.append(int(setting))
else:
    settings = [5,5,5]
    print("Settings not found: Loaded defaults")

vectors = []
for x in range(0, len(points)):
    points[x][1] *= settings[1]
    points[x][0] *= settings[1]
    if int(points[x][1]) == 0 and int(points[x][0]) == 0:
        angle = 0
        magnitude = 0
    elif int(points[x][0]) == 0 or int(points[x][1]) == 0:
        angle = 0
    else:
        angle = math.degrees(math.atan(int(points[x][1]) / int(points[x][0])))
    magnitude = math.sqrt((int(points[x][0]) * int(points[x][0])) + (int(points[x][1]) * int(points[x][1])))
    if angle == 0.0:
        angle = 0
    if magnitude == 0.0:
        magnitude = 0
    if angle == 0 and points[x][0] < 0:
        magnitude *= -1
    elif angle == 0 and points[x][1] < 0:
        angle = -90
    elif angle == 0 and points[x][1] > 0:
        angle = 90
    vectors.append([angle, magnitude])

turtle.hideturtle()
turtle.speed(settings[0])
turtle.width(settings[2])

pendown = True
turtle.pendown()

for x in range(0, len(vectors)):
    if vectors[x] == [0,0] and not pendown:
        turtle.pendown()
        pendown = True
    elif vectors[x] == [0,0] and pendown:
        turtle.penup()
        pendown = False
    else:
        if vectors[x][0] != 0:
            turtle.left(vectors[x][0])
        turtle.forward(vectors[x][1])
        if vectors[x][0] != 0:
            turtle.right(vectors[x][0])
turtle.done()