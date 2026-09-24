import random
import time

def randomized_quicksort(arr):
    # Stop recursion when the list has zero or one element
    if len(arr) <= 1:
        return arr
    # Randomly select a pivot from the current list
    pivot = random.choice(arr)
    # Divide elements based on their relationship to the pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    # Recursively sort the smaller and greater partitions

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

test_array = [8, 3, 5, 1, 9, 3, 7]
print("Original Array:", test_array)
print("Randomized Quicksort:", randomized_quicksort(test_array))

def deterministic_quicksort(arr):
     # Stop recursion when the list has zero or one element
    if len(arr) <= 1:
        return arr
 # Always use the first element as the pivot
    pivot = arr[0]
# Divide the remaining elements around the pivot
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
 # Recursively sort the smaller and greater partitions
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

print("Deterministic Quicksort:", deterministic_quicksort(test_array))

# Measure the execution time of a sorting algorithm
def measure_time(sort_function, data):
    # Record the starting time
    start_time = time.perf_counter()

    # Sort a copy so the original dataset is not changed
    sort_function(data.copy())

    # Record the ending time
    end_time = time.perf_counter()

    # Return the total execution time
    return end_time - start_time

# Create datasets for performance testing
data_size = 500

# Randomly ordered numbers
random_data = [random.randint(1, 1000) for _ in range(data_size)]

# Numbers already in sorted order
sorted_data = list(range(data_size))

# Numbers in reverse-sorted order
reverse_data = list(range(data_size, 0, -1))

# Dataset containing many repeated values
repeated_data = [random.randint(1, 10) for _ in range(data_size)]

# Compare both Quicksort algorithms on each dataset
datasets = {
    "Random": random_data,
    "Sorted": sorted_data,
    "Reverse Sorted": reverse_data,
    "Repeated Elements": repeated_data
}

print("\nPerformance Comparison")

for name, data in datasets.items():
    # Measure Randomized Quicksort
    randomized_time = measure_time(randomized_quicksort, data)

    # Measure Deterministic Quicksort
    deterministic_time = measure_time(deterministic_quicksort, data)

    # Display the execution times
    print(f"\n{name} Dataset:")
    print(f"Randomized Quicksort: {randomized_time:.6f} seconds")
    print(f"Deterministic Quicksort: {deterministic_time:.6f} seconds")

    # Hash table implementation using chaining
class HashTable:
    def __init__(self, size=10):
        # Create an empty bucket for each position in the table
        self.size = size
        self.table = [[] for _ in range(size)]

            # Convert a key into a bucket index
    def hash_function(self, key):
        # Python's hash function creates a hash value,
        # and modulo keeps the index within the table size
        return hash(key) % self.size

        # Insert a key-value pair into the hash table
    def insert(self, key, value):
        # Find the bucket where the key belongs
        index = self.hash_function(key)

        # Check whether the key already exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Add the new key-value pair to the bucket
        self.table[index].append([key, value])

            # Search for a key in the hash table
    def search(self, key):
        # Find the bucket where the key should be stored
        index = self.hash_function(key)

        # Search through the key-value pairs in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        # Return None if the key is not found
        return None

        # Delete a key-value pair from the hash table
    def delete(self, key):
        # Find the bucket where the key should be stored
        index = self.hash_function(key)

        # Search for the key inside the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True

        # Return False if the key was not found
        return False

    # Test the hash table operations
hash_table = HashTable()

# Insert sample key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

# Search for values
print("\nHash Table Test")
print("Search apple:", hash_table.search("apple"))
print("Search banana:", hash_table.search("banana"))

# Delete a key and check the result
print("Delete banana:", hash_table.delete("banana"))
print("Search banana after deletion:", hash_table.search("banana"))