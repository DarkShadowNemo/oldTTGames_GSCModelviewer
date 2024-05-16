import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import glob
import numpy as np
from struct import unpack, pack
import math

vertices=[]
vertices2=[]
strips=[]
uvs=[]
vcolors=[]

gCamAng = 0.
gCamHeight = 3.
distanceFromOrigin = 45

v_mx = 0
v_my = 0
v_mz = 0

modeFlag = 0

def dropCallback(window, paths):
    fa=-1
    fb=0
    fc=1
    fileName = paths[0].split("\\")[-1]
    dropped=1
    if (paths[0].split(".")[1].lower() != "gsc"):
        print("invalid File\nPlease provide an game scene file")
        return
    with open(paths[0], "rb") as f:
        while 1:
            Chunk = f.read(4)
            if Chunk == b"\x03\x01\x00\x01":
                f.seek(1,1)
                value1 = unpack("B", f.read(1))[0]
                vertexCount = unpack("B", f.read(1))[0]
                flags = unpack("B", f.read(1))[0]
                if flags == 0x6C:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type1 = unpack("B", f.read(1))[0]==False
                        value1 = unpack("B", f.read(1))[0]
                        f.seek(-2,1)
                        vertices.append([vx,vy,vz])
                        normalZ = unpack("<f", f.read(4))[0]
                        
                            
            elif Chunk == b"SST0":
                break




def main():
    global gCamAng, gCamHeight, distanceFromOrigin, v_mx, v_my, v_mz, modeFlag
    if not glfw.init():
        return
    windowWidth = 640
    windowHeight = 480
    window = glfw.create_window(windowWidth, windowHeight, "GSC 3d model Viewer V1.0.0", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_drop_callback(window, dropCallback)

    while not glfw.window_should_close(window):
        glClearColor(0,0,0,255)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(distanceFromOrigin, 1, 0.1,1000)
        #glOrtho(0, windowWidth, windowHeight, 0, 0, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(5*math.sin(gCamAng),gCamHeight,5*math.cos(gCamAng), 0,0,0, 0,1,0)
        state = glfw.get_key(window, glfw.KEY_1)
        state2 = glfw.get_key(window, glfw.KEY_2)
        
        state3 = glfw.get_key(window, glfw.KEY_3)
        state4 = glfw.get_key(window, glfw.KEY_4)

        state5 = glfw.get_key(window, glfw.KEY_5)
        state6 = glfw.get_key(window, glfw.KEY_6)

        state7 = glfw.get_key(window, glfw.KEY_R)
        state8 = glfw.get_key(window, glfw.KEY_D)
        state9 = glfw.get_key(window, glfw.KEY_A)
        state10 = glfw.get_key(window, glfw.KEY_S)
        state11 = glfw.get_key(window, glfw.KEY_W)

        state12 = glfw.get_key(window, glfw.KEY_UP)
        state13 = glfw.get_key(window, glfw.KEY_DOWN)

        state14 = glfw.get_key(window, glfw.KEY_Z)
        state15 = glfw.get_key(window, glfw.KEY_F)
        
        if state == glfw.PRESS:
            gCamAng += math.radians(-10%360)
        if state2 == glfw.PRESS:
            gCamAng += math.radians(10%360)
        if state3 == glfw.PRESS:
            gCamHeight += 0.1
        if state4 ==glfw.PRESS:
            gCamHeight -= 0.1

        if state5 == glfw.PRESS:
            distanceFromOrigin -= 1
        if state6 ==glfw.PRESS:
            distanceFromOrigin += 1

        if state7 == glfw.PRESS:
            gCamAng = 0
            gCamHeight =1
            distanceFromOrigin
            v_mz=0
            v_my=0
            v_mx=0

        glBegin(GL_TRIANGLE_STRIP)
        for i, v in enumerate(vertices,1):
            glVertex3fv([v[0]+v_mx,v[1]+v_my,v[2]+v_mz])
        glEnd()


        if state8 == glfw.PRESS:
            v_mx-=1
        if state9 == glfw.PRESS:
            v_mx+=1
        if state10 == glfw.PRESS:
            v_mz-=1
        if state11 == glfw.PRESS:
            v_mz+=1
        if state12 == glfw.PRESS:
            v_my-=1
        if state13 == glfw.PRESS:
            v_my+=1
        if state14 == glfw.PRESS:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if state15 == glfw.PRESS:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                

        #drawFrame()
        
        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
                        
                            
                        
                    
