import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)



class UpdateVideos():
    def __init__(self, root):
        if root == None:
            window = tk.Tk()
            fonts.configure()
        else:
            window = tk.Toplevel(root)

        window.geometry("750x500")
        window.title("Update Videos")

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
        enter_new_lbl = tk.Label(window, text="Enter Video Number to update")
        enter_new_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_new_txt = tk.Entry(window, width=3)
        self.input_new_txt.grid(row=1, column=2, padx=10, pady=10)

        rating_lbl = tk.Label(window, text="Enter New Rating    ")
        rating_lbl.grid(row=2, column=1, padx=10, pady=10)

        self.rating_input_txt = tk.Entry(window, width=3)
        self.rating_input_txt.grid(row=2, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked)
        check_video_btn.grid(row=1, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=3, column=3, sticky="NW", padx=10, pady=10)

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

    """
    This function update the ratings of videos using the set_rating function
    from videolibrary.py file and show it to text box using get_rating function
    """
    def update_video_clicked(self):
            try:
                key = (self.input_new_txt.get())
                rating = int(self.rating_input_txt.get())
                name = lib.get_name(key)
                if key=="" or rating=="" or name is None:
                    set_text(self.video_txt, f"Video {key} not found")

                else:
                    r=lib.set_rating(key ,rating)
                    director = lib.get_director(key)
                    rating = lib.get_rating(key)
                    play_count = lib.get_play_count(key)
                    video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                    set_text(self.video_txt, video_details)
                    self.list_videos_clicked()
            except ValueError:
                pass
            self.status_lbl.configure(text="Update Video button was clicked!")
        

if __name__ == "__main__":
    UpdateVideos(None)
