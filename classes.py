from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,height,width):
        #Creating root widget
        self.__root = Tk()
        self.__root.title("Maze Solver")
        
        #Creating Canvas widget
        self.__canvas = Canvas(self.__root,bg="black",width=width,height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        
        #Creating data member to represent windows "runnnig"
        self.__running = False
        
        #Creating protocol to close the window
        #WMDELETEWINDOW is the close button, will call self.close when clicked
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
     
    #Redraw method to call when to render visuals    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    #draw line method to draw line btween 2 point
    def draw_line(self,line,fill_color="yellow"):
        line.draw(self.__canvas,fill_color)
    
    #track the"Running" state of window to True, set to False earlier by default, then call redraw() method in a while loop to keep visuals rendered    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
    
    #close method, set running to False
    def close(self):
        self.__running=False
        
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Line():
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self,canvas,fill_color="yellow"):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y, fill=fill_color,width=2)
        

class Cell():
    def __init__(self,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        
        self._win = win
        
    def draw(self,x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self._win is None:
            return
        
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line)
            # If the wall doesn't exist, draw a background-colored line to "erase" it
        else:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line,"black")
            
         
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line)
            # If the wall doesn't exist, draw a background-colored line to "erase" it
        else:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line,"black")
            
         
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line)
            # If the wall doesn't exist, draw a background-colored line to "erase" it
        else:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line,"black")
            
         
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line)
            # If the wall doesn't exist, draw a background-colored line to "erase" it
        else:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line,"black")
            
    def draw_move(self,to_cell,undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center1 = half_length + self._x1
        y_center1 = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center1, y_center1), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
