mylist = [23,19,39,14,95,49,29]
def swap(indeks,a,b):
   indeks[a],indeks[b]=indeks[b],indeks[a]
   
def sorting(mylist):
    
   change = True
   lap = 0
   while lap < len(mylist)-1 and change:
       change = False
       IndeksMinimal = lap
       IndeksMeningkat = IndeksMinimal + 1
       while IndeksMeningkat < len(mylist):
           if mylist[IndeksMinimal] > mylist[IndeksMeningkat]:
               IndeksMinimal = IndeksMeningkat
           IndeksMeningkat += 1
       if IndeksMinimal != lap:
           swap(mylist,IndeksMinimal,lap)
           change = True
       print(mylist)  
       if not change:
           print("output = %s" %str(mylist))
       lap += 1
print('source list')
print(mylist)
print("proses sorting")
sorting(mylist)