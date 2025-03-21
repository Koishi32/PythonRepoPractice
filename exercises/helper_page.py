# TODO: complete this class
import math

class PaginationHelper:
    Num_pages=0
    PageContainer=[]
    collection=[]
    items_per_page=0
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.items_per_page=items_per_page
        self.collection = collection
        self.Num_pages = math.ceil(len(self.collection)/self.items_per_page)
        for i in range(0,self.Num_pages):
            rate= i*self.items_per_page
            if(i == self.Num_pages-1):
                self.PageContainer.append(collection[rate:])
            else:
                self.PageContainer.append(collection[rate:rate+self.items_per_page])
            print(self.PageContainer)
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return self.Num_pages
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if (page_index<0 or page_index>=self.Num_pages):
            return -1
        else:
            return len(self.PageContainer[page_index])
        
        
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if (item_index<0 or item_index>=len(self.collection)):
            return -1
        else:
            item_page = math.floor(item_index / self.items_per_page)
            return item_page

