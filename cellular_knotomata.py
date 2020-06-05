from random import randint

n = 3

grid = []
y_step = 0
x_step = 0
shadow_grid = []
step_rules = {}
tiles = {}
rec = 0
rec_frame = 0
reset = 0

def tile0(x,y):
    row = y_step * x
    col = x_step * y
    line(row, col, row + x_step, col + y_step)

def tile1(x,y):
    row = y_step * x
    col = x_step * y
    line(row + x_step, col, row, col + y_step)

def tile2(x,y):
    row = y_step * x
    col = x_step * y
    line(row, col, row + x_step, col + y_step)
    line(row + x_step, col, row, col + y_step)
    
    
def flip(g,x,y):
    if g[x][y] == 0:
        g[x][y] = 1
    else:
        g[x][y] = 1

def no_flip(g,x,y):
    pass

def flip_one(g,x,y):
    g[x][y] = 1

def flip_zero(g,x,y):
    g[x][y] = 0

def get_neighborhood(x, y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if x + i < 0 or x + i > n - 1:
                continue
            if y + j < 0 or y + j > n - 1:
                continue
            if grid[(x+i)][(y+j)] == 1:
                count += 1
    return count

def step():
    global grid,shadow_grid  
    for i in range(n):
        for j in range(n):
            gn = get_neighborhood(i,j)
            f = step_rules[gn]
            f(shadow_grid,i,j)
    grid = shadow_grid

def setup():
    global grid, step_rules, x_step, y_step, \
           tiles
    size(600, 600)
    background(0)
    stroke(255)
    frameRate(5)   
    y_step = height//n
    x_step = width//n
    for i in range(n):
        grid.append([0] * n)
        shadow_grid.append([0] * n)
    grid[n//2][n//2] = 1
    for i in range(10):
        p = randint(0,3)
        if p == 0:
            step_rules[i] = flip
        if p == 1:
            step_rules[i] = no_flip
        if p == 2:
            step_rules[i] = flip_one
        if p == 3:
            step_rules[i] = flip_zero
    for i in range(10):
        p = randint(0,2)
        if p == 0:
            tiles[i] = tile0
        if p == 1:
            tiles[i] = tile1
        if p == 2:
            tiles[i] = tile2

def draw():
    global grid, rec_frame, reset
    clear()
    step()
    if reset == 1:
        grid = []
        for i in range(n):
            grid.append([0] * n)
        grid[n//2][n//2] = 1
        reset = 0
    else:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    gn = get_neighborhood(i,j)
                    tile = tiles[gn]
                    tile(i,j)
    if rec == 1:
        saveFrame("frame_temp/frame-{}.png".format(rec_frame))
        rec_frame += 1
    

def keyPressed():
    global rec, reset
    if (key == 's'): #start recording
        if rec == 0:
            print("Start recording")
            rec = 1
        else:
            print("Recording stopped. Frames stored in frame_temp.")
            rec = 0
    if (key == 'r'): #reset
        reset = 1
    
