x, y, w = 0, 1, 2  
while w < 4000000:  
    if w % 2 == 0:  
        x += w 
    y, w = w, y + w  
print(x)  

