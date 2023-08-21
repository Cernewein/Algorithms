# Algorithms and data structures
> This project stores the algorithms and data structures that I implement in python along my journey revisiting the basics.
> It is also an opportunity for me to learn more about proper testing in Python using Pytest and TDD.

## Table of Contents
* [Project implementations](#project-implementations)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)

## Project implementations

The project is subdivided into different folders containing a number of algorithms and datastructures. Here are the elements you can find in the project : 

### Graphs
1. [Datastructures](./graphs/datastructures.py)
    * Graph
    * Min heap
    * Binary Tree
    * Sigma Tree (for storing an alphabet encoding)
2. [Combinations](./graphs/combinations.py)
    * Combinations generator (uses DFS)
    * Combinations with replacement generator (uses DFS)
3. [Dijkstra](./graphs/dijkstra.py)
    * Dijkstra algorithm for shortest path
    * Dijkstra algorithm optimized by using a heap^
4. [Kosaraju](./graphs/kosaraju.py)
    * Compute strongly connected components in a graph
5. [Median](./graphs/median.py)
    * Class for the median maintenance problem using two heaps
6. [Topology](./graphs/topology.py)
    * Topological sort using DFS
7. [Two sum](./graphs/two_sum.py)
    * An algorithm using a lookup table in order to find if there are two numbers in a list that can be added to get a provided input

### Greedy algorithms
1. [Huffman encoding](./greedy/huffman.py)
    * An implementation for the huffman encoding algorithm

### Miscellaneous
1. [Karatsuba multiplication](./miscellaneous/karatsuba_multiplication.py)
    * An implementation of a divide and conquer multiplication approach : karatsuba multiplication

### Selection
1. [Rselect](./selection/rselect.py)
    * Rselect algorithm for selecting the ith smallest element in a list

### Sorting
1. [Merge sort](./sort/mergesort.py)
    * Merge sort algorithm for sorting a list
    * Merge sort and count split inversion algorithm
2. [Quick sort](./sort/quicksort.py)
    * Quick sort algorithm for sorting a list


## Technologies Used
Base python 3.11.


## Setup

1. Install python 3.11
2. Install [poetry](https://python-poetry.org/docs/#installation)
3. Install project dependencies
```bash
poetry init
``` 


## Project Status
Project is: _in progress_.


## Acknowledgements

This project implements algorithms as taught in the [Algorithms illuminated book series](https://www.algorithmsilluminated.org/).