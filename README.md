# MSCS 532 Assignment 3 – Understanding Algorithm Efficiency and Scalability

This project contains my implementation and analysis for Assignment 3 in MSCS 532 – Algorithms and Data Structures.

## Project Overview

The assignment focuses on two topics:

1. Randomized Quicksort and its performance compared with Deterministic Quicksort.
2. A hash table that uses chaining for collision handling.

## Files

- `assignment3.py` – Python implementation and performance testing
- `Hanusha Assignment 3.docx` – Assignment 3 written report
- `README.md` – Project information and instructions

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python assignment3.py
```
## Quicksort Testing

I tested Randomized Quicksort and Deterministic Quicksort with input sizes of 100, 500, 1000, and 2000.

The tests use four types of input:

- Random data
- Sorted data
- Reverse-sorted data
- Repeated elements

The deterministic version always selects the first element as the pivot. The randomized version selects a random pivot during each recursive call.

## Hash Table

The hash table uses chaining to handle collisions and supports insert, search, and delete operations. The bucket index is calculated using a randomized multiply-mod-prime hashing approach. Python's `hash()` value is first converted to a non-negative integer before the bucket calculation is performed.

## Summary of Findings

In my tests, Randomized Quicksort remained efficient on random, sorted, and reverse-sorted inputs. Deterministic Quicksort became much slower on sorted and reverse-sorted data as the input size increased because selecting the first element repeatedly created highly unbalanced partitions.

For the hash table, chaining allows multiple key-value pairs to remain in the same bucket when collisions occur. Its expected performance depends on keeping the load factor reasonably low so that the bucket chains remain short.