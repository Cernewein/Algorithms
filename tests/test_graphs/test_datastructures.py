from graphs.datastructures import Graph, MinHeap


def test_MinHeap():
    heap = MinHeap()
    heap.insert("a", 10)
    heap.insert("b", 3)
    heap.insert("c", 6)
    heap.insert("d", 5)
    heap.insert("e", 2)
    heap.insert("f", 7)

    assert heap.keys == [2, 3, 6, 10, 5, 7]
    assert heap.nodes == ["e", "b", "c", "a", "d", "f"]

    assert heap.extract_min() == "e"

    assert heap.keys == [3, 5, 6, 10, 7]
    assert heap.nodes == ["b", "d", "c", "a", "f"]
