import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)
    

def set_playlist_text(text_area, content):
    text_area.delete("1.0", tk.END)
    for x in content:
        text_area.insert(tk.END, x + '\n')

"""
This function reset the both input video and play text boxes
"""
def reset_playlist(text_area):
    text_area.delete("1.0", tk.END)
    video_playlist.clear()
    play_count.clear()

"""
This function shows the total play counts of videos added to input video text
"""    
def play_playlist(text_area,content):
    text_area.delete("1.0", tk.END)
    for x in content:
        text_area.insert(tk.END, str(x) + '\n')
    
    
class CreateVideoList():
    def __init__(self, root):
        if root == None:
            window = tk.Tk()
            fonts.configure()
        else:
            window = tk.Toplevel(root)

        window.geometry("750x600")
        window.title("Create Video List")

        #list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        #list_videos_btn.grid(row=0, column=0, padx=10, pady=10)
        """
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)
        """
        enter_video_lbl = tk.Label(window, text="Enter Video Number to add in playlist")
        enter_video_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_video_txt = tk.Entry(window, width=3)
        self.input_video_txt.grid(row=1, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Add Video", command=self.enter_video_clicked)
        check_video_btn.grid(row=1, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=8, wrap="none")
        self.video_txt.grid(row=3, column=3, sticky="NW", padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset", command=self.reset_button_clicked)
        reset_btn.place(x=550,y=230)

        self.play_count_txt = tk.Text(window, width=24, height=8, wrap="none")
        self.play_count_txt.grid(row=4, column=3, sticky="NW", padx=10, pady=10)
        
        play_btn = tk.Button(window, text="Play", command=self.play_button_clicked)
        play_btn.place(x=550,y=470)
                


        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

        if root == None:
            window.mainloop()

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
    
    def enter_video_clicked(self):
        
        try:
            key = (self.input_video_txt.get())
            name = lib.get_name(key)
            if key=="" or name is None:
                self.list_videos_clicked()
                set_text(self.video_txt, f"Video {key} not found")
            else:
                playlist=lib.get_name(key)
                video_playlist.append(playlist)
                play_count.append(key)
                set_playlist_text(self.video_txt,video_playlist)
                
        except ValueError:
                pass
        self.status_lbl.configure(text="Add Video button was clicked!")

    """
    These functions call the above reset_playlist and play_playlist functions on button click
    """
    def reset_button_clicked(self):
        reset_playlist(self.video_txt)
        reset_playlist(self.play_count_txt)
        self.status_lbl.configure(text="Reset button was clicked!")
        
    def play_button_clicked(self):
        l=[]
       
        for i in play_count:
            a=lib.increment_play_count(i)
            b=lib.get_play_count(i)
            name = lib.get_name(i)
            video_details = f"{name}\nPlays: {b}"
            l.append(video_details)
            play_playlist(self.play_count_txt,l)
            
        print(l)
        
        self.status_lbl.configure(text="Play button was clicked!")

play_count=[]      
video_playlist=[]
if __name__ == "__main__":
    
    CreateVideoList(None)
