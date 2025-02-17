from classes import *

def main():
    win = Window(800,600)
    
    cell1 = Cell(win)
    
    cell1.draw(100,100,200,200)
    cell2 = Cell(win)
    cell2.draw(100,200,200,300)
    

    

    
    
    win.wait_for_close()
    


if __name__ == "__main__":
    main()