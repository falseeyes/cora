import random

count=random.randrange(1000)

for x in range(count, 0, -1):
    
    if x==1 :
        drink= "bottle of thing"
    else:
        drink= "bottles of thing"
        
    print (x, drink, "on the wall,")
    print (x, drink)
    
    if x > 1:
        print ("and if one of those bottles should happen to fall there'll be,")
    else:
        print ("and if that bottle should happen to fall there'll be,")
    
    print (x-1, "bottles of thing on the wall.")
    print ()
    
print ("No more bottles of thing on the w@ll, no more bottles of th!ng, if you g0 t0 the",
"store @nd buy $0me m0re, there'll be", count, "b0ttles of thing on the wall!")