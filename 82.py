import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.ttk import *
import time
from PIL import Image,ImageTk
from tkinter import PhotoImage
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Playlist:
    def __init__(self):
        self.head = None
        self.current_node = None

    def insert(self, music_name):   
        new_node = Node(music_name)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = self.current_node = new_node
        else:
            last = self.head.prev
            new_node.prev = last
            last.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def delete_element(self, music_name):
        if self.head is None:
            messagebox.showerror(message='PLAYLIST IS EMPTY')
            print("No Music is there to delete!\n")
            return
        ptr = self.head
        while True:
            if ptr.next == ptr and ptr.data == music_name:
                print("One file deleted! Playlist is Empty Now!\n")
                self.head = None
                return
            elif ptr.data == music_name:
                prev = ptr.prev
                next = ptr.next
                prev.next = next
                next.prev = prev
                self.head = next
                messagebox.showinfo(message="Music deleted!")
                return
            ptr = ptr.next
            if ptr == self.head:
                break
        messagebox.showwarning(message="SPECIFIED FILE IS NOT FOUND!")
        print("No Music file is there!\n")

    def show(self):
        playlist_contents = []
        if self.head is None:         
            messagebox.showerror(message='PLAYLIST IS EMPTY!')          
           #print("Playlist is Empty!\n")
        else:
            show_ptr = self.head
            i = 1
            while True:
                playlist_contents.append(f"Song {i}: {show_ptr.data}")
                i += 1
                show_ptr = show_ptr.next
                if show_ptr == self.head:
                    break
        return playlist_contents
    def next_node(self):
        if self.current_node is None:
            messagebox.showwarning(message="NO SONGS IN THE PLAYLIST")
            print("No songs in Playlist!\n")
        else:
            newWindow = tk.Tk()
            newWindow.config(bg='sandy brown')

            label = tk.Label(newWindow, text='PLAYING NEXT SONG', bg='sandy brown', fg='brown4', justify='center')
            label1 = tk.Label(newWindow, text=self.current_node.data, bg='sandy brown', fg='brown4', justify='center')

            label.grid(row=0, column=0, padx=5, pady=5)
            label1.grid(row=1, column=0, padx=5, pady=5)

            # Get window width and height
            window_width = newWindow.winfo_reqwidth()
            window_height = newWindow.winfo_reqheight()

            # Calculate the position to place the labels in the middle of the window
            x_position = (window_width - label.winfo_reqwidth()) / 2
            y_position = (window_height - label.winfo_reqheight() - label1.winfo_reqheight()) / 2

            label.place(x=x_position, y=y_position)
            label1.place(x=x_position, y=y_position + label.winfo_reqheight())
            self.current_node = self.current_node.next

            newWindow.mainloop()
            #self.current_node = self.current_node.next
            print(f"Playing Next Song : {self.current_node.data}")

    def prev_node(self):
        if self.current_node is None:
            messagebox.showerror(message="No songs in Playlist!\n")
        else:
            newWindow = tk.Tk()
            newWindow.config(bg='sandy brown')

            label = tk.Label(newWindow, text='PREVIOUSLY PLAYED', bg='sandy brown', fg='brown4', justify='center')
            label1 = tk.Label(newWindow, text=self.current_node.data, bg='sandy brown', fg='brown4', justify='center')

            label.grid(row=0, column=0, padx=5, pady=5)
            label1.grid(row=1, column=0, padx=5, pady=5)

            # Get window width and height
            window_width = newWindow.winfo_reqwidth()
            window_height = newWindow.winfo_reqheight()

            # Calculate the position to place the labels in the middle of the window
            x_position = (window_width - label.winfo_reqwidth()) / 2
            y_position = (window_height - label.winfo_reqheight() - label1.winfo_reqheight()) / 2

            label.place(x=x_position, y=y_position)
            label1.place(x=x_position, y=y_position + label.winfo_reqheight())
            self.current_node = self.current_node.prev
            newWindow.mainloop()
           

           # self.current_node = self.current_node.prev
            print(f"Playing Previous Song : {self.current_node.data}")
    def first_node(self):
        if self.head is None:
            messagebox.showerror(message="No songs in Playlist!")
            print("Playlist is Empty!\n")
        else:
            newWindow = tk.Tk()
            newWindow.config(bg='sandy brown')

            label = tk.Label(newWindow, text='FIRST SONG IN PLAYLIST', bg='sandy brown', fg='brown4', justify='center')
            label1 = tk.Label(newWindow, text=self.head.data, bg='sandy brown', fg='brown4', justify='center')

            label.grid(row=0, column=0, padx=5, pady=5)
            label1.grid(row=1, column=0, padx=5, pady=5)

            # Get window width and height
            window_width = newWindow.winfo_reqwidth()
            window_height = newWindow.winfo_reqheight()

            # Calculate the position to place the labels in the middle of the window
            x_position = (window_width - label.winfo_reqwidth()) / 2
            y_position = (window_height - label.winfo_reqheight() - label1.winfo_reqheight()) / 2

            label.place(x=x_position, y=y_position)
            label1.place(x=x_position, y=y_position + label.winfo_reqheight())

            newWindow.mainloop()

            print(f"Playing First Music : {self.head.data}")

    def last_node(self):
        if self.head is None:
            messagebox.showerror(message="No songs in Playlist!")
            print("Playlist is Empty!\n")
        else:
            newWindow = tk.Tk()
            newWindow.config(bg='sandy brown')

            label = tk.Label(newWindow, text='LAST SONG IN PLAYLIST', bg='sandy brown', fg='brown4', justify='center')
            label1 = tk.Label(newWindow, text=self.head.prev.data, bg='sandy brown', fg='brown4', justify='center')

            label.grid(row=0, column=0, padx=5, pady=5)
            label1.grid(row=1, column=0, padx=5, pady=5)

            # Get window width and height
            window_width = newWindow.winfo_reqwidth()
            window_height = newWindow.winfo_reqheight()

            # Calculate the position to place the labels in the middle of the window
            x_position = (window_width - label.winfo_reqwidth()) / 2
            y_position = (window_height - label.winfo_reqheight() - label1.winfo_reqheight()) / 2

            label.place(x=x_position, y=y_position)
            label1.place(x=x_position, y=y_position + label.winfo_reqheight())

            newWindow.mainloop()

            print(f"Playing Last Music : {self.head.prev.data}")

    def specific_data(self,music_name):
        if self.head is None:
            messagebox.showerror(message="No songs in Playlist!\n")
            print("No music is there to be searched!\n")
            return

        ptr = self.head
        while True:
            if ptr.data == music_name:
                newWindow = tk.Tk()
                newWindow.config(bg='sandy brown')

                label = tk.Label(newWindow, text='MUSIC FOUND', bg='sandy brown', fg='brown4', justify='center')
                label1 = tk.Label(newWindow, text=f"Playing Music : {ptr.data}", bg='sandy brown', fg='brown4', justify='center')

                label.grid(row=0, column=0, padx=5, pady=5)
                label1.grid(row=1, column=0, padx=5, pady=5)

                # Get window width and height
                window_width = newWindow.winfo_reqwidth()
                window_height = newWindow.winfo_reqheight()

                # Calculate the position to place the labels in the middle of the window
                x_position = (window_width - label.winfo_reqwidth()) / 2
                y_position = (window_height - label.winfo_reqheight() - label1.winfo_reqheight()) / 2

                label.place(x=x_position, y=y_position)
                label1.place(x=x_position, y=y_position + label.winfo_reqheight())

                newWindow.mainloop()

                print("Music Found!\n")
                print(f"Playing Music : {ptr.data}")
                return
            ptr = ptr.next
            if ptr == self.head:
                break
        messagebox.showerror(message='There is no Music file with this name!\n')
    print("There is no Music file with this name!\n")
def add_music(playlist, entry, listbox):
    music_name = entry.get()
    if music_name:
        playlist.insert(music_name)
        entry.delete(0, tk.END)
        refresh_playlist(playlist, listbox)

def delete_music(playlist, entry, listbox):
    music_name = entry.get()
    if music_name:
        playlist.delete_element(music_name)
        entry.delete(0, tk.END)     
        refresh_playlist(playlist, listbox)

def refresh_playlist(playlist,listbox):
    listbox.delete(0, tk.END)
    playlist_contents = playlist.show()
    for item in playlist_contents:
        listbox.insert(tk.END, item)

def play_next(playlist):
    playlist.next_node()

def play_previous(playlist):
    playlist.prev_node()

def play_first(playlist):
    playlist.first_node()

def play_last(playlist):
    playlist.last_node()

def play_specific(playlist):
    music_name = "" 
    def submit():
        nonlocal music_name  # Use nonlocal to modify outer variable
        music_name = entry.get()
        playlist.specific_data(music_name)
        newWindow.destroy()
        # Close the window after submitting

        # Initialize music_name
    newWindow = tk.Tk()
    newWindow.config(bg="sandy brown")
    entry = tk.Entry(newWindow,fg='brown4',bg='sandy brown',bd=1)
    submitb = tk.Button(newWindow, text="SUBMIT", fg='brown4', bg='sandy brown', command=submit)
    submitb.grid(row=1, column=1, padx=5, pady=5)
    entry.grid(row=0, column=0, padx=5, pady=5)
    newWindow.mainloop()
    
def main1():
    playlist = Playlist()

    root = tk.Tk()
    root.title("Song Playlist Application")

    entry_label = tk.Label(root,text="Music Name:",fg='brown4',bg='sandy brown',bd=10)
    entry_label.grid(row=0, column=0, padx=5, pady=5)

    entry = tk.Entry(root,fg='brown4',bg='sandy brown')
    entry.grid(row=0, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Add Music",fg='brown4',bg='sandy brown', command=lambda: add_music(playlist, entry, listbox))
    add_button.grid(row=0, column=2, padx=5, pady=5)

    delete_button = tk.Button(root, text="Delete Music",fg='brown4',bg='sandy brown', command=lambda: delete_music(playlist, entry, listbox))
    delete_button.grid(row=1, column=2, padx=5, pady=5)

    show_button = tk.Button(root, text="Refresh Playlist",fg='brown4',bg='sandy brown',command=lambda: refresh_playlist(playlist, listbox))
    show_button.grid(row=2, column=2, padx=5, pady=5)

    listbox = tk.Listbox(root,fg='brown4',bg='sandy brown',state='normal')
    listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    next_button = tk.Button(root, text="Play Next",fg='brown4',bg='sandy brown', command=lambda: play_next(playlist))
    next_button.grid(row=4, column=0, padx=5, pady=5)

    previous_button = tk.Button(root, text="Play Previous",fg='brown4',bg='sandy brown', command=lambda: play_previous(playlist))
    previous_button.grid(row=4, column=1, padx=5, pady=5)

    first_button = tk.Button(root, text="Play First",fg='brown4',bg='sandy brown', command=lambda: play_first(playlist))
    first_button.grid(row=5, column=0, padx=5, pady=5)

    last_button = tk.Button(root, text="Play Last",fg='brown4',bg='sandy brown', command=lambda: play_last(playlist))
    last_button.grid(row=5, column=1, padx=5, pady=5)

    specific_button = tk.Button(root, text="Play Specific",fg='brown4',bg='sandy brown', command=lambda: play_specific(playlist))
    specific_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    exit_button = tk.Button(root, text="Exit",fg='brown4',bg='sandy brown', command=root.quit)
    exit_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

    root.config(bg='sandy brown')

    root.mainloop()



def main():
    window = tk.Tk()
    window.config(bg='sandy brown')
    window.geometry('1500x800')

   # frame1 = Frame(top, highlightbackground="blue", highlightthickness=2)
   # frame1.pack(padx=20, pady=20)
   # image = Image.open("C:\\Users\\sammy\\OneDrive\\Desktop\\istockphoto-1175435360-612x612.jpg")
    
   # photo = ImageTk.PhotoImage(image)

# Create a label to display the image
    #image_label = tk.Label(window, image=photo)
    #image_label.pack()

    label=tk.Label(window, text="MUSIC PLAYLIST",font=('Cooper Black',25),fg='brown4',bg='sandy brown',height=5,width=25)
    label.place(relx=0.5,rely=0.1,anchor='center')
    
    button=tk.Button(window, text="OPEN",font=('Cooper Black',15),fg='brown4',bg='sandy brown',height=5,width=25,command=main1)
    button.place(relx=0.5, rely=0.5, anchor='center')

   
    window.mainloop()

if __name__ == "__main__":
    main()