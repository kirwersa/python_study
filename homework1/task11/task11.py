from playlist import Playlist


def main():
    playlist = Playlist({1: "track 1", 2: "track 2", 3: "track 3"})
    # print(playlist.__getitem__(1))
    print(playlist[1])
    # playlist.__setitem__(4,"track 4")
    playlist[4] = "track 4"
    print(playlist)


if __name__ == '__main__':
    main()
