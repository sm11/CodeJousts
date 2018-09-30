def campusCup(emails):
    dict_ = {}
    for e in emails:
        val = e.split('@')[-1]
        if val in dict_:
            dict_[val][0] += 1
            dict_[val][1] += 20
        else:
            dict_[val] = [1, 20]

        
    mem = {}
    for k, v in dict_.items():
        if v[1] < 100:
            mem[k] = 0
        if v[1] >= 100:
            mem[k] = 3
        if v[1] >= 200:
            mem[k] += 8
        if v[1] >= 300:
            mem[k] += 15
        if v[1] >= 500:
            mem[k] += 25

    return [k for k,v in sorted(mem.items(), key=lambda kv: (-kv[1], kv[0]))]

        
            

