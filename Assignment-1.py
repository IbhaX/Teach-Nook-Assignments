""" TeachNook September Batch - Assignment 1 """

class String:
  ''' Very Common String Functions '''
  def __init__(self, string):
    self.string = string
  
  def chars(self):
    # Returns all characters in a string
    return [i for i in self.string]
  
  def vowels(self):
    # Returns all vowels in a string
    return [i for i in self.string if i in "aeiou"]
  
  def char_count(self):
    # Counts the number of repetition for each character in a        string except for symbols
    count = {i:self.string.count(i) for i in self.string if i not in '\"\':;?!.,/()=+-&_$#@\n\t '}
    return count
        
  def string_len(self):
    # Returns length of string in terms of characters
    return len(self.string)
  
  def word_replace(self, word, repl):
    # Returns a string replaced with new word
    return self.string.replace(word, repl)
  
  def capitalize(self):
    # Returns Capitalized string
    return self.string.capitalize()
  
  def upper(self):
    # Returns the string all in uppercase
    return self.string.upper()
  
  def lower(self):
    # Returns the string all in lowercase
    return self.string.lower()
  
  def title(self):
    # Returns the string, all words capitalized
    return self.string.title()
  
  def word_count(self):
    # Returns count of number of words
    return len(self.string.split())
  
  
class List:
  ''' Very Common List Functions '''
  def __init__(self, lst):
    self.list = lst
    self.types = self.element_types()
    self.len = self.list_len()
  
  def append_element(self, element):
    # Returns the list with new element added at the end
    self.list.append(element)
    return self.list
  
  def extend_element(self, lst):
    # Returns the list with new list merged
    self.list.extend(lst)
    return self.list
  
  def element_types(self):
    # Returns a dict with all the elements in a list with its types
    return {str(type(i)).split("'")[-2]:i for i in self.list}
  
  def list_len(self):
    # Returns length of the list
    return len(self.list)
  
  def insert(self, val, idx=0):
    # Returns a list with new element added to a specific insex location
    self.list.insert(val, idx)
    return self.list

class Tuple:
  ''' Very Common Tuple Functions '''
  def __init__(self, tup):
    self.tuple = tup
  
  def count_element(self, element):
    # Returns the count of a particular element in a tuple
    return self.tuple.count(element)
  
  def element_index(self, element):
    # Returns the value of an element in a specific index location
    return self.tuple.index(element)
    
  
class Dict:
    ''' Very Common Tuple Functions '''
    def __init__(self, dictionary):
      self.dict = dictionary
    
    def dict_keys(self):
      # Returns all the keys in a dictionary
      return self.dict.keys()
    
    def dict_values(self):
      # Returns all the values in a dictionary
      return self.dict.values()
    
    def dict_append(self, obj):
      # Returns a dict with new object added
      self.dict.update(obj)
      return self.dict
    
    def dict_get(self, key):
      # Returns the value of key and it doesn't traceback any         error if the key is not available, instead it returns None
      return self.dict.get(key)
        
    def dict_popitem(self):
      # Returns the last object in a dictionary
      self.dict.popitem()
      return self.dict
    
    def dict_default(self, key):
      # Returns the value of key if the key is present inside the dictionary else it returns a default value
      default = "Item not available"
      return self.dict.setdefault(key, default)
    
    def dict_items(self):
      # Returns iyems present inside the Dictonary
      return self.dict.items()
    


if __name__ == "__main__":
  list1 = (1,2, "hello", (1,2,3), True, None, type).index("hello")
  dict1 = {
    "a": "acv",
    2: "b"
  }
  d = Dict(dict1)
  print(d.dict_keys())
  
