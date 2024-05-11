class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
            self.tail = new_song
            self.current_song = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song

    def play_current_song(self):
        if self.current_song:
            print(f"Playing: {self.current_song.title} - {self.current_song.artist}")
        else:
            print("No song in the playlist")

    def play_next_song(self):
        if self.current_song and self.current_song.next:
            self.current_song = self.current_song.next
            self.play_current_song()
        else:
            print("No next song")

    def play_previous_song(self):
        if self.current_song and self.current_song.prev:
            self.current_song = self.current_song.prev
            self.play_current_song()
        else:
            print("No previous song")

    def display_playlist_forward(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.title} - {current_node.artist}")
            current_node = current_node.next

    def display_playlist_backward(self):
        current_node = self.tail
        while current_node:
            print(f"{current_node.title} - {current_node.artist}")
            current_node = current_node.prev

# Usage example
playlist = Playlist()
playlist.add_song("Song 1", "Artist 1")
playlist.add_song("Song 2", "Artist 2")
playlist.add_song("Song 3", "Artist 3")

print("Playlist in forward direction:")
playlist.display_playlist_forward()

print("\nPlaylist in backward direction:")
playlist.display_playlist_backward()

print("\nPlaying current song:")
playlist.play_current_song()

print("\nPlaying next song:")
playlist.play_next_song()

print("\nPlaying previous song:")
playlist.play_previous_song()
