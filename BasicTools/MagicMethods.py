# Short list of magic/dunder methods with examples

class Magic_Methods:

    def __str__(self):          # string dunder method
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):    # equal dunder method
        return self.title == other.title and self.author == other.author 

    def __lt__(self, other):    # less than dunder method
        return self.num_pages < other.num_pages                              

    def __gt__(self, other):    # greater than dunder method
        return self.num_pages < other.num_pages                             

    def __add__(self, other):   # add dunder method
        return f"{self.num_pages + other.num_pages} pages"                   

    def __contains__(self, keyword): # contains (a specified string, number, etc.) dunder method
        return keyword in self.title or keyword in self.author              

    def __getitem__(self, key):     # access attributes by indexing
        if key == "title":
            return self.title       
        elif key == "author":
            return self.author     
        elif key == "num_pages":
            self.num_pages        
        else:
            return f"Key {key} was not found."

