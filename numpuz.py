import tkinter as tk
import random
from tkinter import messagebox



gamesize = 3
gamehight = gamesize*96
gamewidth = gamesize*80


class Numpuz:
    def __init__(self, master):
        self.master = master
        self.master.title("Numpuz")
        self.master.geometry(f"{gamewidth}x{gamehight}")
        
        self.tiles = []
        self.blank_tile = None
        self.timer_label = tk.Label(self.master, text="00:00:00", font=("New Times Roman", 16))
        self.timer_label.grid(row=0,column=2)
        self.sec = 0
        self.min = 0
        self.timer_running = False
        
        self.create_tiles()
        self.draw_tiles()
        self.start_timer()
    
    def create_tiles(self):
        numbers = list(range(1, gamesize*gamesize)) + [None]
        random.shuffle(numbers)
        
        for i, number in enumerate(numbers):
            row = i // gamesize
            col = i % gamesize
            tile = Tile(self.master, number, row, col)
            self.tiles.append(tile)
            if number is None:
                self.blank_tile = tile
    
    def draw_tiles(self):
        for tile in self.tiles:
            tile.button.grid(row=tile.row+1, column=tile.col+1)
    
    def move_tile(self, tile):
        if self.can_move(tile):
            self.swap_tiles(tile, self.blank_tile)
            self.draw_tiles()
            if self.check_win():
                messagebox.showinfo("Congratulations!", "You have won the game!")
                if messagebox.askyesno("Numpuz", "you want to restart?") : 
                    root.destroy()
                    root = tk.Tk()
                    root.numpuz = Numpuz(root)
                    root.mainloop()
                else:
                    root.destroy()
    
    def can_move(self, tile):
        row_diff = abs(tile.row - self.blank_tile.row)
        col_diff = abs(tile.col - self.blank_tile.col)
        return row_diff + col_diff == 1
    
    def swap_tiles(self, tile1, tile2):
        tile1.row, tile2.row = tile2.row, tile1.row
        tile1.col, tile2.col = tile2.col, tile1.col
    
    def check_win(self):
        correct_order = list(range(1, gamesize*gamesize )) + [None]
        current_order = sorted(self.tiles, key=lambda x: (x.row, x.col))
        current_numbers = [tile.number for tile in current_order]
        return current_numbers == correct_order
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()
    
    def update_timer(self):
        if self.timer_running:
            self.sec += 1
            self.timer_label.config(text=f"{self.min}:{self.sec}")
            if self.sec == 59:
                self.min += 1
                self.sec = -1
            self.master.after(1000, self.update_timer)
    
    def stop_timer(self):
        self.timer_running = False

class Tile:
    def __init__(self, master, number, row, col):
        self.master = master
        self.number = number
        self.row = row
        self.col = col
        self.create_button()
    
    def create_button(self):
        if self.number is not None:
            self.button = tk.Button(self.master, text=str(self.number), width=10, height=5, 
                                    command=lambda: self.master.numpuz.move_tile(self))
        else:   
            self.button = tk.Button(self.master, text="", width=10, height=5, state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False,False)
    root.numpuz = Numpuz(root)
    root.mainloop()