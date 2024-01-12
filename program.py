import os
import random
import pickle
from tkinter import Tk, Label, Button, PhotoImage, messagebox, Frame
from PIL import Image, ImageTk

STARTING_ELO = 1500  # Adjust this value as needed
k_factor = 16  # Adjust this based on how much impact each match should have
target_screen_fraction = 0.6  # Adjust this to change the size of the player images
button_size = 100  # Adjust this to change the size of the vote buttons
current_folder_path = "" # Insert folder path


class FootballPlayer:
    def __init__(self, name, image_path, elo_rating=STARTING_ELO):
        self.name = name
        self.elo_rating = elo_rating
        self.image_path = image_path

def get_player_list(folder_path):
    player_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            player_name = os.path.splitext(filename)[0]
            player = FootballPlayer(player_name, os.path.join(folder_path, filename))
            player_list.append(player)
    return player_list

class PlayerComparisonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Football Player Comparison")

        self.players = self.load_players()  # Load players from saved data or generate new ones

        # Create a frame for the ELOs
        elo_frame = Frame(master)
        elo_frame.pack(side="top")

        # Center the ELO frame
        elo_frame.place(relx=0.5, rely=0.0, anchor=CENTER)

        self.label_elo1 = Label(elo_frame, text="")
        self.label_elo1.pack(side="left")

        self.label_elo2 = Label(elo_frame, text="")
        self.label_elo2.pack(side="left")

        self.label1 = Label(master, text="")
        self.label1.pack()

        self.image1 = None
        self.label_image1 = Label(master, image=self.image1)
        self.label_image1.pack(side="left")

        self.label2 = Label(master, text="")
        self.label2.pack()

        self.image2 = None
        self.label_image2 = Label(master, image=self.image2)
        self.label_image2.pack(side="left")

        # Create a frame for the vote buttons
        button_frame = Frame(master)
        button_frame.pack(side="bottom")

        # Center the button frame
        button_frame.place(relx=0.5, rely=1.0, anchor=CENTER)

        self.vote_button1 = Button(button_frame, text="Select Image 1", command=self.vote_player1, width=button_size)
        self.vote_button1.pack(side="left")

        self.vote_button2 = Button(button_frame, text="Select Image 2", command=self.vote_player2, width=button_size)
        self.vote_button2.pack(side="left")

        self.next_comparison()

    def load_players(self):
        # Get the list of players from the folder
        player_list = get_player_list(current_folder_path)
    
        # Check if any of the image paths are no longer valid
        valid_players = []
        for player in player_list:
            if os.path.isfile(player.image_path):
                valid_players.append(player)
    
        # Save the list of valid players
        self.players = valid_players
    
        # Check if any new pictures have been added to the folder
        saved_player_names = {player.name for player in self.players}
        current_player_names = {os.path.splitext(filename)[0] for filename in os.listdir(current_folder_path)}
        if saved_player_names != current_player_names:
            # Reload the list of players from the folder
            self.players = get_player_list(current_folder_path)
            self.save_players(self.players)
    
        return self.players

    def save_players(self, players):
        with open('players_data.pkl', 'wb') as file:
            pickle.dump((players, current_folder_path), file)

    def load_and_resize_image(self, image_path):
        try:
            original_image = Image.open(image_path)
        except FileNotFoundError:
            messagebox.showerror("Error", "Could not load image: " + image_path)
            return None

        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate target size based on a fraction of the screen size
        target_width = int(screen_width * target_screen_fraction)
        target_height = int(screen_height * target_screen_fraction)

        # Calculate new dimensions while preserving the aspect ratio
        width, height = original_image.size
        aspect_ratio = width / height

        # Calculate new dimensions based on the desired width or height
        if target_width / aspect_ratio > target_height:
            new_width = int(target_height * aspect_ratio)
            new_height = target_height
        else:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)

        # Resize the image
        resized_image = original_image.resize((new_width, new_height))

        return ImageTk.PhotoImage(resized_image)
    
    def next_comparison(self):
        if len(self.players) < 2:
            messagebox.showinfo("Info", "No more players to compare.")
            return

        random.shuffle(self.players)
        self.player1 = self.players[0]
        self.player2 = self.players[1]

        self.label_elo1.config(text=f"{self.player1.name} - ELO: {round(self.player1.elo_rating, 1)}")
        self.label_elo2.config(text=f"{self.player2.name} - ELO: {round(self.player2.elo_rating, 1)}")

        self.label1.config(text=f"{self.player1.name}")
        self.image1 = self.load_and_resize_image(self.player1.image_path)
        self.label_image1.config(image=self.image1)

        self.label2.config(text=f"{self.player2.name}")
        self.image2 = self.load_and_resize_image(self.player2.image_path)
        self.label_image2.config(image=self.image2)

    def vote_player1(self):
        self.update_elo(self.player1, self.player2)
        self.next_comparison()
        self.save_players(self.players)

    def vote_player2(self):
        self.update_elo(self.player2, self.player1)
        self.next_comparison()
        self.save_players(self.players)

    def update_elo(self, winner, loser):
        if winner == loser:
            return

        expected_winner = 1 / (1 + 10 ** ((loser.elo_rating - winner.elo_rating) / 400))
        expected_loser = 1 / (1 + 10 ** ((winner.elo_rating - loser.elo_rating) / 400))

        winner.elo_rating += k_factor * (1 - expected_winner)
        loser.elo_rating += k_factor * (0 - expected_loser)

if __name__ == "__main__":
    root = Tk()
    app = PlayerComparisonApp(root)
    root.mainloop()
