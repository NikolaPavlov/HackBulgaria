class Song:

    def __init__(self, title="unknow", artist="unknow", album="unknow", length=0):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        return (self.title, self.artist, self.length) == (other.title, other.artist, other.length)
    def __hash__(self):
        return hash(self.title + self.artist + self.album)

    def length_of_mp3(self, seconds=False, minutes=False, hours=False):
        all_seconds = 0

        if isinstance(self.length, int):
            return int(self.length)

        split_time = self.length.split(":")
        if len(split_time) == 3:
            all_seconds = int(split_time[0]) * 60 * 60 + int(split_time[1]) * 60 + int(split_time[2])

        elif len(split_time) == 2:
            all_seconds = int(split_time[0]) * 60 + int(split_time[1])

        if seconds is True:
            return all_seconds
        if minutes is True:
            return float("%.2f" % (all_seconds / 60))
        if hours is True:
            return float("%.2f" % (all_seconds / 3600))

    def length_to_str(self):
        return self.length
