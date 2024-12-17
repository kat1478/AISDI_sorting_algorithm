# Sorting Algorithms Project

## **Project Description**

This project implements **five classical sorting algorithms** in Python:

1. **Bubble Sort**
2. **Selection Sort**
3. **Insertion Sort**
4. **Merge Sort**
5. **Quick Sort**

The main goal of the project is to compare the performance of these algorithms using input data from the file `pan-tadeusz.txt` (a list of words).

---

## **Project Structure**

```plaintext
project/
│-- README.md                # Project description file
│-- sortowanie.py            # Main file that runs all tests
│-- pan-tadeusz.txt          # Input data file (list of words)
│-- src/                     # Folder with sorting algorithm implementations
│   │-- bubble_sort.py       # Bubble Sort implementation
│   │-- selection_sort.py    # Selection Sort implementation
│   │-- insertion_sort.py    # Insertion Sort implementation
│   │-- merge_sort.py        # Merge Sort implementation
│   │-- quick_sort.py        # Quick Sort implementation
│-- images/                  # Folder containing generated performance graphs
```

---

## **Setup Instructions**

### 1. Requirements

- Python version **3.8** or newer
- **matplotlib** library for generating graphs

Install the required library:

```bash
pip install matplotlib
```

---

### 2. Running the Project

1. Copy the `pan-tadeusz.txt` file into the main project directory.

2. Run the main script `sortowanie.py`:

```bash
python sortowanie.py
```

### **What the script does**:

- Tests all implemented sorting algorithms.
- Reads words from the `pan-tadeusz.txt` file for list sizes ranging from **1000** to **10,000** (increments of 1000).
- Measures the execution time for each sorting algorithm.
- Generates and saves performance graphs in the **images/** folder.

---

## **Implemented Sorting Algorithms**

### 1. **Bubble Sort**

- **File**: `src/bubble_sort.py`
- **Time Complexity**:
  - Average and Worst-case: \( O(n^2) \)
  - Best-case: \( O(n) \)
- **Description**:  
  Compares adjacent elements and swaps them if they are in the wrong order. Larger elements "bubble up" to the end of the list.

---

### 2. **Selection Sort**

- **File**: `src/selection_sort.py`
- **Time Complexity**: \( O(n^2) \)
- **Description**:  
  Finds the smallest element in the unsorted part of the list and swaps it with the first element of that part.

---

### 3. **Insertion Sort**

- **File**: `src/insertion_sort.py`
- **Time Complexity**:
  - Average and Worst-case: \( O(n^2) \)
  - Best-case: \( O(n) \)
- **Description**:  
  Inserts each element into its correct position in the sorted part of the list.

---

### 4. **Merge Sort**

- **File**: `src/merge_sort.py`
- **Time Complexity**: \( O(n \log n) \)
- **Description**:  
  Recursively divides the list into halves, sorts them, and merges the sorted halves into one list.

---

### 5. **Quick Sort**

- **File**: `src/quick_sort.py`
- **Time Complexity**:
  - Average: \( O(n \log n) \)
  - Worst-case: \( O(n^2) \)
- **Description**:  
  Selects a "pivot" element and divides the list into two parts:
  - Elements smaller than the pivot.
  - Elements greater than the pivot.  
    These parts are sorted recursively.

---

## **Performance Results**

The script generates graphs showing the execution time of each algorithm as a function of the input list size. The graphs are saved in the **images/** folder with the following names:

- `Bubble Sort.png`
- `Selection Sort.png`
- `Insertion Sort.png`
- `Merge Sort.png`
- `Quick Sort.png`

---

## **Example Output**

After running the script, the console output will look like this:

```plaintext
Testing algorithm: Bubble Sort
Bubble Sort - Number of elements: 1000, Time: 0.01562 s
Bubble Sort - Number of elements: 2000, Time: 0.06250 s
...

Testing algorithm: Merge Sort
Merge Sort - Number of elements: 1000, Time: 0.00200 s
Merge Sort - Number of elements: 2000, Time: 0.00420 s
...
```

---

## **Authors**

- **kat1478**

## **License**

This project is licensed under the **MIT License**.
