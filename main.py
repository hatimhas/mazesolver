from classes import *

def main():
    win = Window(800,600)
    
    point1 =Point(100,100)
    point2 =Point(700,500)
    
    line = Line(point1,point2)
    win.draw_line(line,"yellow")
    
    
    win.wait_for_close()
    


if __name__ == "__main__":
    main()