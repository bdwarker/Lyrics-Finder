import lyricsgenius as lg

genius = lg.Genius("aWsgGLnbyIj0H_TK0S3NQnfV3aDfa8reDweRRn3vGxCyneajcAsLfhwyqzN2S3iq")


def get_lyrics(artist, song):
    song = genius.search_song(song, artist)
    return song.lyrics

artist = input("Please Enter the name of the artist\n")
song = input("Please Enter the name of the song\n")

print(get_lyrics(artist, song))