import random
from tkinter import Button, Frame, Tk, ttk

class Framework:
    def __init__(self):
        self.title = "Title"
        self.height = 300
        self.width = 300
        self.x = int((1920 - self.width) / 2)
        self.y = int((1080 - self.height) / 2)
        self.root = Tk()

    def set_title(self, title):
        """Set the title of the window."""
        self.title = title
        return self

    def set_size(self, *dimensions):
        """Set the size of the window. Accepts either one value for square dimensions or two values for width and height."""
        if len(dimensions) == 1:
            self.height = dimensions[0]
            self.width = dimensions[0]
        if len(dimensions) == 2:
            self.height = dimensions[0]
            self.width = dimensions[1]
        return self

    def set_window_location(self, x, y):
        """Set the location of the window on the screen."""
        self.x = x
        self.y = y
        return self

    def get_window_location(self):
        """Get the formatted string for the window location."""
        return "+" + str(self.x) + "+" + str(self.y)

    def create_window(self):
        """Create the main window."""
        self.root.title(self.title)
        self.root.geometry(str(self.width) + "x" + str(self.height) + self.get_window_location())
        self.root.resizable(False, False)
        return self.root

    def set_background_color(self, red, green, blue):
        """Set the background color of the window."""
        self.root.config(background="#%s%s%s" % (red, green, blue))
        return self

    def shuffle_buttons(self, buttons):
        """Shuffle the buttons randomly on the window."""
        random.shuffle(buttons)
        for button in buttons:
            button.pack_forget()
            button.pack()


def create_empty_space(frame, size):
    """Create an empty space in the frame with a specified size."""
    ttk.Label(frame, text=" ", font=("", size), background=frame["bg"]).pack()


try:
    framework = Framework().set_background_color("00", "00", "00").set_size(500)
    main_window = framework.create_window()

    b1 = Button(main_window, text=' 1 ', font='None 20 bold', background="#F00")
    b2 = Button(main_window, text=' 2 ', font='None 20 bold', background="#F00")
    b3 = Button(main_window, text=' 3 ', font='None 20 bold', background="#F00")
    b4 = Button(main_window, text=' 4 ', font='None 20 bold', background="#F00")
    b5 = Button(main_window, text=' 5 ', font='None 20 bold', background="#F00")

    label_win = ttk.Label(main_window, text="win", font=("None", 20), background="#000", foreground="#0F0")

    def shuffle():
        """Shuffle the buttons on the window when called."""
        label_win.pack_forget()
        buttons = [b1, b2, b3, b4, b5]
        framework.shuffle_buttons(buttons)

    create_empty_space(main_window, 30)
    shuffle()

    b6 = Button(main_window, text=' Shuffle ', font='None 20 bold', background="#0F0")
    b6.place(x=185, y=400)

    def get_y_coordinate(element):
        """Get the y-coordinate of an element."""
        return element.winfo_rooty()

    def play(button):
        """Show and hide a button on the window."""
        button.pack_forget()
        button.pack()
        button.pack_forget()
        button.pack()

        # Check if buttons are packed in the order b1, b2, b3, b4, b5
        if (get_y_coordinate(b1) < get_y_coordinate(b2) and
            get_y_coordinate(b2) < get_y_coordinate(b3) and
            get_y_coordinate(b3) < get_y_coordinate(b4) and
            get_y_coordinate(b4) < get_y_coordinate(b5)):
            
            # Hide all buttons
            b1.pack_forget()
            b2.pack_forget()
            b3.pack_forget()
            b4.pack_forget()
            b5.pack_forget()
            
            # Show "win" message
            label_win.pack()

    b1.config(command=lambda: play(b1))
    b2.config(command=lambda: play(b2))
    b3.config(command=lambda: play(b3))
    b4.config(command=lambda: play(b4))
    b5.config(command=lambda: play(b5))
    b6.config(command=lambda: shuffle())
    main_window.mainloop()

except BaseException as ex:
    print(ex)
    input("Press enter to exit".upper())