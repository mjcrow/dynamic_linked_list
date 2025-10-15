from dynamic_linked_list import PlayList

def test_insert_head_and_tail():
    pl = PlayList()
    pl.insertHead("Song A")
    pl.insertTail("Song B")
    pl.insertTail("Song C")
    assert pl.listSongs() == ["Song A", "Song B", "Song C"]

def test_get():
    pl = PlayList()
    pl.insertTail("Track 1")
    pl.insertTail("Track 2")
    assert pl.get(0) == "Track 1"
    assert pl.get(1) == "Track 2"
    assert pl.get(2) == "Not found"

def test_remove():
    pl = PlayList()
    pl.insertTail("X")
    pl.insertTail("Y")
    pl.insertTail("Z")
    assert pl.remove(1) is True
    assert pl.listSongs() == ["X", "Z"]
    assert pl.remove(5) is False

def test_find():
    pl = PlayList()
    pl.insertTail("Sang Real")
    pl.insertTail("Red Rain")
    pl.insertTail("Revolution is My Name")
    assert pl.find("Red Rain") == 1
    assert pl.find("Schism") == -1

if __name__ == "__main__":
    test_insert_head_and_tail()
    test_get()
    test_remove()
    test_find()
    print("All playlist tests passed.")
