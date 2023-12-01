
# Notes for Day 1


## python

### part 1
read data
sanitize data, strip newlines

find first occurrence of digit by for-loop

for last occurrence of digit, also use for-loop,
but use slice to reverse
```python
for char in item[::-1]
```

### part 2
words

get list of the words
```py
word = ['one', 'two', 'three']
```
etc.

Do if check
```py
if word in item:
```

Ideas: 
* Check for both the digits and words. 
    * Compare last index of word to index of digit.



Use `find` and `rfind` to get the index of the word.  
These return the index where the word *starts*.
```python
idx_first = item.find('one')    # Find first occurrence
idx_last  = item.rfind('one')   # Find last occurrence
```

To get the index range of the word inside `item`

```python
idx_range = [idx_first, idx_first + len('one')]

item[ idx_first : idx_first + len('one') ]
```

so now we should enumerate all of the items when searching for a digit,
so that we can check the `idx_first + len(word)` against `digit_index`






