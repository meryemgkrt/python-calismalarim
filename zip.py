list1 = [1,2,3,4,5]
list2= ["a","b","c","d","e"]
list3= ["armut","börtlen", "ceviz","dut","elma"]

# Liste uzunluklarını alalım
""" sonuc=list(zip(list1,list2,list3))
print(sonuc) """

##for item in zip(list1,list2,list3):
##print(item)
    
    
for x,y,z in zip(list1,list2,list3):
    print(x,y,z)