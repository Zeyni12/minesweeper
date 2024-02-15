from tkinter import Button, Label
import random
import configure
import ctypes
import sys
class Cell:
    all=[]
    cell_count = configure.Cell_count
    cell_count_label_object = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.X=x
        self.Y=y
        Cell.all.append(self)

    def create_btn_object(self,location):
        btn = Button(
            location,
            width=12,
            height=4,
        ) 

        btn.bind('<Button-1>', self.left_click_actions )
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn 

    @staticmethod
    def create_cell_cout_lable(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text= f"Cells left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

        return lbl


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()
            # If Mines count is equal to the cells left count, player won
            if Cell.cell_count == configure.Mines_count:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations ! You won the game!', 'Game over',0)

        # ccancel Left and Right click events if cell is already opend:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')             

    def get_cell_by_axis(self, x,y):
        #Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.X == x and cell.Y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.X - 1, self.Y-1),
            self.get_cell_by_axis(self.X -1, self.Y),
            self.get_cell_by_axis(self.X - 1, self.Y+1),
            self.get_cell_by_axis(self.X , self.Y-1),
            self.get_cell_by_axis(self.X + 1, self.Y-1),
            self.get_cell_by_axis(self.X +1, self.Y),
            self.get_cell_by_axis(self.X + 1, self.Y+1),
            self.get_cell_by_axis(self.X , self.Y+1),
        ]   

        cells = [cell for cell in cells if cell is not None]
        return cells 
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter
    def show_cell(self):
        if not self.is_opened:
           Cell.cell_count -= 1
           self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
           #Replace the text of cell count label with the newer count
           if Cell.cell_count_label_object:
              Cell.cell_count_label_object.configure(
                  text=f"Cells left:{Cell.cell_count}"
                )
        # If this was a mine candidate, then for safety, we should
        # configure the background color to SystemButtonFace
        self.cell_btn_object.configure(
            bg='SystemButtonFace'
        )                 
        # Mark the cell as opened (use is as the last line of this method)
        self.is_opened = True       
        
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game over',0)
        sys.exit()
        #A logic to interrupt the game and display 
       
    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
        
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )   
            self.is_mine_candidate = False 
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, configure.Mines_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
  

    def __repr__(self):
        return f"Cell({self.X}, {self.Y})"   
     
