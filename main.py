import turtle
import os
import math    

if os.path.exists("import.VECTOR"):
    with open("import.VECTOR", "r") as f: 
        exec(f"points={f.readline().strip()}")
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

if os.path.exists("import.CONF"):
    with open("import.CONF", "r") as f:
        settingsRaw = f.readlines()
    settings = []
    for setting in settingsRaw:
        settings.append(float(setting))
    del setting
    del settingsRaw
else:
    settings = [5,5,5]
    print("Settings not found: Loaded defaults")

vectors = []
for point in points:
    x = float(point[0]) * settings[1]
    y = float(point[1]) * settings[1]
    if y == 0 and x == 0:
        angle = 0
        magnitude = 0
    elif x == 0 and y != 0:
        if y < 0:
            angle = -90
        else:
            angle = 90
    elif x != 0 and y == 0:
        if x < 0:
            angle = 180
        else:
            angle = 0
    elif x < 0 and y > 0:
        angle = 180 + math.degrees(math.atan(y / x))
    else:
        angle = math.degrees(math.atan(y / x))
    magnitude = math.sqrt((x**2) + (y**2))
    vectors.append([angle, magnitude])
    del angle
    del magnitude
    del x
    del y
del point
del points

turtle.hideturtle()
turtle.speed(settings[0])
turtle.width(settings[2])
del settings

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