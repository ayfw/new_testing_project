import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entry must have title or content")
        self._title = title
        self._contents = contents
        self._read_so_far = 0


    def format(self):
        return f"{self._title}: {self._contents}"
    
    def count_words(self):
        word_count = self.format().split()
        amount_of_words = len(word_count)
        return amount_of_words
    
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Reading time wpm is 0 can't calculate!")
        count_contents = len(self._contents.split())
        return math.ceil(count_contents / wpm)
    
    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0
            
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_words)
    
    
    
   

    

        
