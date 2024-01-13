class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        # Parameters:
        #   title: a string
        #   artist: a string
        # Side-effects:
        #   Sets the title and artist properties
        

    def format(self):
        return f"{self.title} by {self.artist}"
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        
