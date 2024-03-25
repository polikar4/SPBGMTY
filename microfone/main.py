import turtle
import turtle as t
import math
import random
import cmath as m
import time
import os


rand = random.random
Size_window = 800

filters = [[0.3, 0.03], [0.35, 0.07]]

result_test = True
grafic_mode = True


step_angle = 5

if(result_test):
    step_angle = 1
else:
    step_angle = 5


class Drow():
    pass

class Micro():
    pass


class Plot():
    drow: Drow = None
    step_degree = 1

    def __init__(self, drow: Drow):
        self.drow = drow

    def DrowGraff(self, mass, gerc):
        

        h = Size_window 
        st = Size_window * 0.5
        end = Size_window * 1
        step = (end - st) / len(mass)

        col = "#000000"
        if gerc == 500:
            col = "#000000"
        if gerc == 2000:
            col = "#900000"
        if gerc == 3500:
            col = "#009000"
        if gerc == 5000:
            col = "#000090"

        # Drow filters
        for filt in filters:
            # horison 
            self.drow.DrowLine(st, filt[1] * Size_window, st + filt[0] * st, filt[1] * Size_window, "#FFFFFF") 
            self.drow.DrowLine(Size_window - filt[0] * st, filt[1] * Size_window, Size_window, filt[1]* Size_window, "#FFFFFF") 


        for i in range(len(mass) - 1):
            self.drow.DrowLine(st + int(i * step), int(h *(mass[i])),
            st + int((i + 1) * step), int(h * mass[i+1]),  color = col)
            


    def CreateMass(self, micros, gerc):
        minn = 0
        maxx = 0
        for mm in micros:
            minn = min(mm.pos_x,minn)
            maxx = max(mm.pos_x,maxx)
        
        result = []
        
        for K in range(-90, 90 + 1, step_angle):
            xh_loc = 0
            for i in range(len(micros)):
                delay = (((micros[i].pos_x - minn)/(maxx-minn))  * m.sin(K * m.pi / 180)) / 340
                phase = 2 * m.pi * gerc * delay
                xh_loc += m.exp(1j * phase)
            result.append(abs(xh_loc))

        result = [(x - min(result)) / (max(result) - min(result)) for x in result]
        return result


class Math():
    def F(center_x, center_y, radius, degris):
        deg = degris * math.pi / 180
        return [center_x + radius * math.cos(deg), center_y + radius * math.sin(deg)]

class Drow():
    t: turtle = None

    def __init__(self):
        self.t = turtle
        self.t.hideturtle()
        self.t.tracer(0)                       #mega speed drow
        self.t.setup(Size_window,Size_window)                  #size window
        self.t.bgcolor("#707070")              #color background
        self.t.penup()

    def GoTo(self, x: int, y: int) -> None:
        self.t.goto(x - Size_window/2,y - Size_window/2)
    
    def DrowLine(self, x1: int, y1: int, x2: int, y2: int, color = "#101010") -> None:
        self.t.color(color,color) 
        self.GoTo(x1,y1)
        self.t.pendown()
        self.GoTo(x2,y2)
        self.t.penup()

    def DrowSquare(self, x: int, y: int, size: int, color = "#101010") -> None:
        self.t.color(color,color) 
        self.GoTo(x,y)
        self.t.pendown()
        self.t.begin_fill()
        self.GoTo(x,y+size)
        self.GoTo(x+size,y+size)        
        self.GoTo(x+size,y)
        self.t.end_fill()
        self.t.penup()

    def DrowСircle(self, x: int, y: int, radius: int, color = "#101010") -> None:
        self.t.color(color,color) 
        self.GoTo(x,y)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(radius)
        self.t.end_fill()
        self.t.penup()

    def DrowPole(self) -> None:
        for i in range(0, 360, 60):
            x1, y1 = Math.F(Size_window * 0.25,Size_window * 0.5, Size_window * 0.2, i)
            x2, y2 = Math.F(Size_window * 0.25,Size_window * 0.5, Size_window * 0.2, i + 60)
            self.DrowLine(x1,y1,x2,y2)


class Micro():

    pos_x: float = None 
    pos_y: float = None 
    drow: Drow = None

    def __init__(self, x: int, y: int, drow: Drow):
        self.pos_x = x
        self.pos_y = y
        self.drow = drow

    def DrowMicro(self, drow):
        drow.DrowСircle(int(self.pos_x),int(self.pos_y),1, "#700000")



class Program():
    drow: Drow = None
    obr = 0

    def __init__(self):
        self.drow = Drow()

    def DataToTest(self):
        file = os.listdir()
        name_file = ""
        while(True):
            name_file = file[self.obr]
            if name_file.split(".")[-1] != "txt":
                self.obr += 1
            else:
                break
        
        my_file = open(name_file, 'r')
        self.obr += 1
        angel_deviation  = float(my_file.readline().split(" = ")[1])
        count_lepest = int(my_file.readline().split(" = ")[1])
        count_dot = int(my_file.readline().split(" = ")[1])
        radius_platform = float(my_file.readline().split(" = ")[1])
        first_delta = float(my_file.readline().split(" = ")[1])
        my_file.close()
        return angel_deviation, count_lepest, count_dot, radius_platform, first_delta

    

    


if __name__ == "__main__":
    prog = Program()

    while True:
        start_time = time.time()

        prog.drow.t.clear()
        # Drow 6-angle 
        if grafic_mode:
            prog.drow.DrowPole()
        # spiral param
        angel_deviation = 0
        count_lepest = 0
        count_dot = 0
        radius_platform = 0
        first_delta = 0
        

        if(result_test):
            angel_deviation, count_lepest, count_dot, radius_platform, first_delta = prog.DataToTest()
        else:
            angel_deviation = 360 * rand()
            count_lepest = int(19 * rand()) + 1
            count_dot = int(128 / count_lepest)
            radius_platform = 60 + 80 * rand()
            first_delta = 10 * rand()
        
        # Create mictofone
        micro = []

        x, y = Math.F(Size_window * 0.25,Size_window * 0.5, 0, 0)
        micro.append(Micro(x,y,prog.drow))
        if grafic_mode: 
            micro[-1].DrowMicro(prog.drow)

        for i in range(count_lepest):
            for j in range(1, count_dot + 1):
                x, y = Math.F(Size_window * 0.25,Size_window * 0.5, radius_platform * j / count_dot + first_delta, 360 * i / count_lepest + j * angel_deviation)
                micro.append(Micro(x,y,prog.drow))

                if grafic_mode: 
                    micro[-1].DrowMicro(prog.drow)

        # Drow graphic and result
        res_itog = []
        for i in [500, 2000, 3500, 5000]:
            plot = Plot(prog.drow)
            res = plot.CreateMass(micro, i)
            res_itog.append(res)

            if grafic_mode: 
                plot.DrowGraff([0] + res + [0], i)  
        
        prog.drow.t.update()

        # Test result
        flag = True

        for i in range(1, 3+1):
            for filt in filters:
                for prosent in range(0, int(180 / step_angle * filt[0])):
                    if(res_itog[i][prosent] > filt[1] and res_itog[i][ int(180 / step_angle) - prosent - 1] > filt[1]):
                        flag = False
                        break

        if flag and not result_test:
            my_file = open(str(angel_deviation) + ".txt", "w")
            my_file.write("angel_deviation = " + str(angel_deviation) + "\n" +
                          "count_lepest = " + str(count_lepest) + "\n" +
                          "count_dot = " + str(count_dot) + "\n" +
                          "radius_platform = " + str(radius_platform) + "\n" +
                          "first_delta = " + str(first_delta)) 
            my_file.close()


        if(result_test and flag):
            my_file = open("result\\result - " + str(angel_deviation) + ".txt", "w")
            my_file.write("angel_deviation = " + str(angel_deviation) + "\n" +
                          "count_lepest = " + str(count_lepest) + "\n" +
                          "count_dot = " + str(count_dot) + "\n" +
                          "radius_platform = " + str(radius_platform) + "\n" +
                          "first_delta = " + str(first_delta) + 
        '''
        \n
        if(result_test):\n
            angel_deviation, count_lepest, count_dot, radius_platform, first_delta = prog.DataToTest()\n
        else:\n
            angel_deviation = 360 * rand()\n
            count_lepest = int(19 * rand()) + 1\n
            count_dot = int(128 / count_lepest)\n
            radius_platform = 60 + 80 * rand()\n
            first_delta = 10 * rand()\n
        
        # Create mictofone\n
        micro = []\n

        x, y = Math.F(Size_window * 0.25,Size_window * 0.5, 0, 0)\n
        micro.append(Micro(x,y,prog.drow))\n
        if grafic_mode: \n
            micro[-1].DrowMicro(prog.drow)\n

        for i in range(count_lepest):\n
            for j in range(1, count_dot + 1):\n
                x, y = Math.F(Size_window * 0.25,Size_window * 0.5, radius_platform * j / count_dot + first_delta, 360 * i / count_lepest + j * angel_deviation)\n
                micro.append(Micro(x,y,prog.drow))\n

                if grafic_mode: \n
                    micro[-1].DrowMicro(prog.drow)\n
            my_file.close()\n
            time.sleep(5)\n
            print(angel_deviation)\n
        ''')

        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Elapsed time: ', elapsed_time)
         