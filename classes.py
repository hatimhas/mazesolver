import time
from tkinter import Tk, BOTH, Canvas
import random

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




class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        # Initialize data members
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        # Create the grid of cells
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        # Initialize the 2D list of cells
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                # Calculate the top-left and bottom-right coordinates of the cell
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                # Create a new Cell object
                cell = Cell(x1, y1, x2, y2, self.win)
                column.append(cell)
            self._cells.append(column)

        # Draw each cell
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Get the cell from the grid
        cell = self._cells[i][j]

        # Draw the cell
        cell.draw()

        # Animate the drawing process
        self._animate()

    def _animate(self):
        # Redraw the window
        self.win.redraw()

        # Pause for a short duration to create an animation effect
        time.sleep(0.05)