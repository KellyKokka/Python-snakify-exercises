def shortest_continuous_segment(s):
    '''implement the function'''
    i = s[0]
    n = 0
    
    while n<len(s):
        if s[n] != i: break
        n += 1

    #after execution of the above, i will be the number forming the first continuous segment
    #and n will be the length of the first continuous segment
    
    done_until = n
    #the variable done_until records until which position we scanned s so far
    
    while done_until < len(s):
        cur_i = s[done_until]
        cur_n = 0
        while cur_n+done_until < len(s):
            if s[cur_n+done_until]!=cur_i: break 
            cur_n +=1
        #after execution of the above in the inner loop,
        #cur_i will be the number forming the next segment
        #and cur_n will be the length of the next segment
        done_until+=cur_n   #this updates until where we scanned s so far 
        if cur_n < n: n,i = cur_n, cur_i
        if cur_n == n and cur_i > i: i = cur_i
        #the two lines above possibly update (i,n) so that
        #i is the number forming the shortest segment so far and
        #n is the length of this shortest so far segment
        
    return (i,n)

