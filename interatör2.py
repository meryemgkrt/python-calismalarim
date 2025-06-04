class Counter:
    def __init__(self,satart,stop):
        self.start = satart
        self.stop = stop
    def __iter__(self):
       
        return self
    def __next__(self):
        if self.start <= self.stop:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration
        
""" for i in Counter(1, 5):
        print(i) """ 
iterator = iter(Counter(20,30))   
""" print(next(iterator))  
print(next(iterator)) """
""" while True:
    try:
        print(next(iterator))
    except StopIteration:
        break """
""" genarator = (i for i in range(1, 6))"""
def sayac(max):
    say=1
    while say<=max:
        yield say
        say += 1
generator= sayac(10)
for i in generator:
    """ print(i) """

list=(i for i in range(1, 12))
for i in list:
    print(i)
