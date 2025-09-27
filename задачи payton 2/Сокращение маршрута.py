def m(a):
    x = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    y = []
    for direct in a:
        if y and y[-1] == opp[direct]:
            y.pop() 
        else:
            y.append(direct)
        return y
dir = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
n = m(dir)
print(n)
