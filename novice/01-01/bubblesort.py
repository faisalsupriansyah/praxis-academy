def swap(lists,a,x):
    lists[a],lists[x]=lists[x], lists[a]
    
def bubblesorting(listku):
    perubahan = True
    proses = len(listku) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while proses > 1 and perubahan:
        perubahan = False
        x = 1
        while x < proses:
            if listku[x]<listku[x-1]:
                perubahan = True
                swap(listku,x,x-1) 
            x+=1
        print(listku)
        #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
        if not perubahan:
            print("output = %s" %str(listku))
        proses-=1

print("source")
mylist=[15,29,10,50,75,90]
print(mylist)
print(" ")
print("proses")
bubblesorting(mylist)