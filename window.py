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
    
    #track the"Running" state of window to True, set to False earlier by default, then call redraw() method in a while loop to keep visuals rendered    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
    
    #close method, set running to False
    def close(self):
        self.__running=False