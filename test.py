import tkinter as tk         # This has all the code for GUIs.
import tkinter.font as font  # This lets us use different fonts.


def center_window_on_screen():
    """
    This centres the window when it is not maximised.  It
    uses the screen and window height and width variables
    defined in the program below.
    :return: Nothing
    """
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def first_message():
    """
    The wording of the message is got from the
    entry box and the label message is then set
    to that.
    :return: Nothing
    """
    msg = 'You are a programmer!'
    lbl_message.config(text=msg)


def second_message():
    """
    The wording of the message is got from the
    entry box and the label message is then set
    to that.
    :return: Nothing
    """
    msg = 'You have made this work.'
    lbl_message.config(text=msg)


# Now we get to the program itself:-
root = tk.Tk()
root.title("A GUI with a menu")
root.configure(bg='lightyellow')
# Set the icon used for your program
# root.iconphoto(True,
#                tk.PhotoImage(file='info.png'))

# This creates a menu bar.
menu_bar = tk.Menu(root)
# This adds the first menu item and its sub-items.
message_menu = tk.Menu(menu_bar, tearoff=0)
message_menu.add_command(label='First message',
                         command=first_message)
message_menu.add_separator()
message_menu.add_command(label='Second message',
                         command=second_message)
# This adds the new menu to the menu bar.
menu_bar.add_cascade(label='Messages',
                     menu=message_menu)

# The Exit menu item can now be added.
menu_bar.add_cascade(label='Exit',
                     command=quit)

# This adds the frame that holds the message label.
message_frame = tk.Frame(root)

width, height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

lbl_font = font.Font(family='Georgia',
                     size='18',
                     weight='bold')
lbl_message = tk.Label(message_frame,
                       text='This is where messages appear.',
                       font=lbl_font,
                       bg='brown', fg='lightyellow')
lbl_message.pack()
message_frame.pack(pady=10)

root.config(menu=menu_bar)
root.mainloop()