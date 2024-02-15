from tkinter import*
from unit import Cell
import configure
import new

root = Tk()
root.configure(bg = "black")
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False,False)

top_frame = Frame(root, bg = "black",
                  width = configure.WIDTH,
                  height = new.height_prct(25))

top_frame.place(x=0 , y=0)

game_title= Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=new.width_prct(25), y=0
)
left_frame=Frame(
    bg='black',
    width=new.width_prct(25),
    height=new.height_prct(75)
)

left_frame.place(x=0, y=new.height_prct(25))

center_frame = Frame(
    root, 
    bg="black",
    width = new.width_prct(75),
    height = new.height_prct(75),
)

center_frame.place(
    x=new.width_prct(25),
    y=new.height_prct(25),
)

for x in range(configure.grid_size):
    for y in range(configure.grid_size):
       c1 = Cell(x,y)
       c1.create_btn_object(center_frame)
       c1.cell_btn_object.grid(
          column=x , row=y
       )
       y+=1
    x+=1

#call the label from the call class
Cell.create_cell_cout_lable(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)   
     
Cell.randomize_mines()

for c in Cell.all:
    print(c.is_mine)
root.mainloop()

