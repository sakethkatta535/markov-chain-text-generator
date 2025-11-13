# Markov Chain Text Generator with Custom Hash Table

**Course:** CSC 120 - Introduction to Computer Science II  
**Programming Language:** Python  
**Project Type:** Natural Language Processing & Data Structures  
**Semester:** Fall 2024

## Overview

A Python implementation of a Markov chain-based statistical text generator featuring a **custom hash table** built from scratch (without using Python's built-in dictionaries). The project analyzes source texts to build n-gram models and generates coherent random text that preserves the linguistic patterns and statistical properties of the original document.

## What Makes This Project Unique

This project combines **two distinct computer science domains**:

1. **Low-Level Data Structures:** Implements hash table internals including hash functions, collision resolution, and key-value storage
2. **Natural Language Processing:** Applies Markov chain theory for statistical text generation—foundational to modern predictive text and language models

Unlike typical introductory projects, this demonstrates understanding of **how fundamental data structures work internally**, not just how to use built-in implementations.

## Technical Implementation

### Custom Hash Table

Built entirely from scratch without Python's `dict` data type, featuring:

**Polynomial Rolling Hash Function:**
def _hash(self, key):
p = 0
for c in key:
p = 31 * p + ord(c)
return p % self._size

- Uses prime constant 31 for uniform distribution
- Computes hash values for string keys
- Modulo operation ensures values fit table size

**Linear Probing Collision Resolution:**

index = self._hash(key)
while self._pairs[index] is not None:
if self._pairs[index] == key:
self._pairs[index].append(value)​
return
index = (index - 1) % self._size

- Handles hash collisions using open addressing
- Searches backward through array until empty slot found
- Appends duplicate suffixes to preserve frequency statistics

**Key Features:**
- Dynamic value lists for multiple suffixes per prefix
- `put()`, `get()`, and `__contains__()` operations
- O(1) average-case lookup and insertion
- No dependency on built-in dictionary types

### Markov Chain Text Generation

Implements statistical language modeling using n-gram analysis:

**Algorithm Overview:**
1. **Build Phase:** Analyze source text to create prefix-suffix mappings
   - Prefix: n consecutive words
   - Suffix: word that follows each prefix
   - Multiplicity: Track frequency of prefix-suffix pairs

2. **Generation Phase:** Construct new text probabilistically
   - Start with `NONWORD` boundary markers
   - Randomly select suffixes weighted by frequency
   - Update sliding window prefix after each selection

**N-Gram Flexibility:**
Supports arbitrary prefix lengths (not just fixed 2-word prefixes):
words = [NONWORD] * n + source_text.split() + [NONWORD]
for i in range(len(words) - n):
prefix = ' '.join(words[i:i + n])
suffix = words[i + n]
table.put(prefix, suffix)


**Statistical Preservation:**
Maintains original text characteristics by storing suffix multiplicities:
If "the cat" → "sat" appears 3 times and "ran" appears once:
hash_table["the cat"] = ["sat", "sat", "sat", "ran"]

"sat" has 3x higher probability of selection


## Project Structure

markov-chain-text-generator/
├── writer_bot_ht.py # Main implementation
├── CSc-120_-Bot-Writer.pdf # Project specification
├── sample_texts/ # Example input texts (optional)
│ ├── alice.txt # Alice in Wonderland
│ ├── shakespeare.txt # Shakespeare works
│ └── gettysburg.txt # Gettysburg Address
└── README.md # This file


## How to Run

### Input Format

The program accepts four inputs via `input()`:
1. Source text filename
2. Hash table size (integer)
3. Prefix length n (integer)
4. Number of words to generate (integer)

### Execution
python writer_bot_ht.py


### Example Session
alice.txt
10000
2
100


This reads `alice.txt`, creates a 10,000-slot hash table, uses 2-word prefixes, and generates 100 words.

### Output Format

Generated text is printed 10 words per line:
Alice was beginning to get very tired of sitting by
her sister on the bank, and of having nothing to
do: once or twice she had peeped into the book
her sister was reading, but it had no pictures or
conversations in it, 'and what is the use of a
book,' thought Alice 'without pictures or conversations?' So she was
considering in her own mind (as well as she could,
for the hot day made her feel very sleepy and
stupid), whether the pleasure of making a daisy-chain would be
worth the trouble of getting up and picking the daisies,


## Algorithm Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| Hash Table `put()` | O(1) | O(n) | Linear probing in pathological cases |
| Hash Table `get()` | O(1) | O(n) | Depends on hash distribution |
| Build Markov Table | O(m) | O(m) | m = words in source text |
| Generate Text | O(k) | O(k) | k = words to generate |

## Skills Demonstrated

### Data Structures
- **Hash table design:** Hash functions, collision resolution strategies
- **Array manipulation:** Fixed-size arrays with dynamic content
- **Key-value storage:** Immutable keys (tuples) with mutable values (lists)

### Algorithms
- **Hashing:** Polynomial rolling hash for string keys
- **Text processing:** Tokenization, sliding window, n-gram extraction
- **Probabilistic selection:** Frequency-weighted random choice
- **State machines:** Prefix-based state transitions

### Programming Concepts
- **Object-oriented design:** Custom class with encapsulation
- **File I/O:** Reading and parsing text files
- **Randomization:** Seeded RNG for reproducible results
- **String manipulation:** Joining, splitting, processing word sequences

### Problem-Solving
- **Statistical modeling:** Capturing linguistic patterns through frequency
- **Edge case handling:** Boundary markers (`NONWORD`) for clean logic
- **Collision management:** Linear probing strategy
- **Output formatting:** Structured text with line breaks

## Implementation Highlights

### Boundary Handling with NONWORD

Uses artificial boundary tokens to simplify algorithm logic:

NONWORD = '@'

Wrap source text with boundaries
words = [NONWORD] * n + source_text.split() + [NONWORD]

Start generation from NONWORD prefix
prefix = ' '.join([NONWORD] * n)


This eliminates special cases for text start/end positions.

### Multiplicity Preservation

Maintains suffix frequency by storing duplicates:

Prefix "half the" appears with suffix "bee" twice
table.put("half the", "bee") # First occurrence
table.put("half the", "bee") # Second occurrence

Result: table["half the"] = ["bee", "bee"]


This ensures generated text mirrors original statistical properties.

### Arbitrary N-Gram Support

Unlike fixed 2-word implementations, supports any prefix length:

Works with n=1 (unigrams), n=2 (bigrams), n=3 (trigrams), etc.
for i in range(len(words) - n):
prefix = ' '.join(words[i:i + n]) # Join n words
suffix = words[i + n]
table.put(prefix, suffix)


## Learning Outcomes

This project improved understanding of:

- **Data structure internals:** How hash tables work beneath the surface
- **Statistical NLP:** How early language models generated human-like text
- **Trade-offs:** Hash table size vs. collision frequency
- **Algorithm design:** Sliding window patterns and state machines
- **Code quality:** Writing clean, well-documented, maintainable code

## Connections to Advanced Topics

### Natural Language Processing
- **Markov chains** are predecessors to modern language models (GPT, BERT)
- **N-gram models** are foundational for text prediction and autocomplete
- **Statistical generation** is used in early chatbots and text completion

### Data Structures
- **Hash tables** power dictionaries, databases, caches, and compilers
- **Collision resolution** strategies impact real-world performance
- **Load factor analysis** determines optimal table sizing

### Applications
- **Predictive text** on smartphones
- **Autocomplete** in search engines
- **Text synthesis** for creative writing
- **Language modeling** in NLP pipelines

## Design Decisions

### Why the Custom Hash Table?

The project requirement to implement hashing from scratch demonstrates:
- Understanding of **how** dictionaries work, not just **using** them
- Knowledge of collision resolution strategies
- Appreciation for Python's optimized built-in implementations

### Why Linear Probing?

Linear probing was chosen for:
- **Simplicity:** Easy to implement and understand
- **Cache efficiency:** Sequential access patterns
- **No extra memory:** No chaining or secondary structures

### Why Tuples for Keys?

Tuples are used because:
- **Immutability:** Required for hash table keys
- **Joinability:** Easy to construct from word lists
- **Hashability:** Built-in `__hash__()` method

## Testing Examples

### Small Input (Eric the Half-a-Bee)

**Source text:** Monty Python song lyrics  
**Prefix length:** 2  
**Generated output:** Statistically coherent phrases matching original style

### Large Input (Alice in Wonderland)

**Source text:** Full novel text  
**Prefix length:** 3  
**Generated output:** Longer, more coherent passages with Victorian English patterns

## References

- Kernighan & Pike, *The Practice of Programming* (Markov chain text generation)
- [Markov Chain Theory - Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
- [Hash Table Fundamentals](https://en.wikipedia.org/wiki/Hash_table)

---

**Author:** Saketh Katta  
**University:** University of Arizona  
**Major:** Computer Science (Junior)  
**Course:** CSC 120 - Introduction to Computer Science II  
**Semester:** Fall 2024
