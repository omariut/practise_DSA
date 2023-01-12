k=[1,2,[3,4],[5,6],7,[8,[9,10],[1,2,4,7,[1,4,5,6],[4,6]]]]
def flat_list(k,d=[]):
    for i in k:
        
        if isinstance(i,int):
            d.append(i)
            
        else:
            flat_list(i,d=d)
            
            
       
    return d

c=flat_list(k)
print(c)
          
