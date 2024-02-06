class MusicListening():
    def __init__(self):
        self.music_history = []

    def add_tracks(self, tracks):
        if type(tracks) != str:
            raise Exception("Track names only")
        # return self.music_history.append(tracks)
        # for tracks in self.music_history:
        #     if tracks not in self.music_history:
        #         self.music_history.append(tracks)
        return self.music_history.append(tracks)
    
    def show_list(self):

        # unique_list = list(set(self.music_history))
        # return unique_list
        
        return list(set(self.music_history))

