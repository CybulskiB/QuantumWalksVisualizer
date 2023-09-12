
def zero_pagg(data,begin,end,diff):
    new_data = {}  
    for key, value in data.items():
        shortened_key = int(key[1:],2) 
        if shortened_key in new_data:
            new_data[shortened_key] += value  
        else:
            new_data[shortened_key] = value
    
    x = []
    y = []
    for pos in range(0,end - diff):
        ys = 0.0
        if pos in new_data:
            ys = new_data[pos]
        y.append(ys)
        x.append(pos + diff)
    return dict(zip(x,y))