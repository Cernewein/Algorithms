import heapq
from typing import Union


class RunningMedianHeap:
    """Class that is using two heaps (one min and one max) in order to track the running median."""

    def __init__(self) -> None:
        self.bigger_elements = []
        self.smaller_elements = []

    def insert(self, element: Union[int, float]) -> None:
        """Insert a new element into the collection of elements

        Args:
            element (Union[int, float]): Element to be inserted into the collection
        """
        if len(self.smaller_elements) == 0:
            heapq.heappush(self.smaller_elements, -element)

        # if the element is smaller than the maximum element in the smaller elements heap it needs to be inserted here
        elif element <= -heapq.nsmallest(1, self.smaller_elements)[0]:
            heapq.heappush(self.smaller_elements, -element)
            # Check if the heaps need to be rebalanced
            if len(self.smaller_elements) > len(self.bigger_elements) + 1:
                element_to_move = -heapq.heappop(self.smaller_elements)
                heapq.heappush(self.bigger_elements, element_to_move)

        elif len(self.bigger_elements) == 0:
            heapq.heappush(self.bigger_elements, element)

        # if the element is bigger than the minimum element in the bigger elements heap it needs to be inserted here
        elif element >= heapq.nsmallest(1, self.bigger_elements)[0]:
            heapq.heappush(self.bigger_elements, element)
            # Check if the heaps need to be rebalanced
            if len(self.bigger_elements) > len(self.smaller_elements) + 1:
                element_to_move = heapq.heappop(self.bigger_elements)
                heapq.heappush(self.smaller_elements, -element_to_move)
        # otherwise the element to be inserted is in between the two values and is therefore inserted in such a way to keep the heaps balanced
        else:
            if len(self.smaller_elements) > len(self.bigger_elements):
                heapq.heappush(self.bigger_elements, element)
            else:
                heapq.heappush(self.smaller_elements, -element)

    def get_median(self) -> Union[int, float]:
        """Get and return the median of the collection of elements

        Returns:
            Union[int, float]: The median element
        """
        if len(self.smaller_elements) > len(self.bigger_elements):
            return -heapq.heappop(self.smaller_elements)
        else:
            return heapq.heappop(self.bigger_elements)
