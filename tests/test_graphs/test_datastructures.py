from graphs.datastructures import MinHeap


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

    assert heap.extract_min() == ("e", 2)

    assert heap.keys == [3, 5, 6, 10, 7]
    assert heap.nodes == ["b", "d", "c", "a", "f"]

    heap.delete("d")
    assert heap.keys == [3, 7, 6, 10]
    assert heap.nodes == ["b", "f", "c", "a"]


def test_GraphWeighted(test_graph_weighted):
    assert test_graph_weighted.get_distance("s", "w") == 4
