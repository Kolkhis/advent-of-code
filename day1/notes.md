
# Notes for Day 1  
my messy ass notes 🙃


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
    * Compare index of last letter in word to index of digit.  



* Use `find` and `rfind` to get the index of the word.  
* These return the index where the word *starts*.  
```python  
idx_first = item.find('one')    # Find first occurrence  
idx_last  = item.rfind('one')   # Find last occurrence  
```

So now I should enumerate all of the items when searching for a digit,  
so that I can check the `idx_first` against `digit_index` for first num, 
and `idx_last + len(word) - 1` against the 2nd `digit_index`





Return locations of numbers along with the numbers themselves.  
Return the end? location of the word?  

---  

