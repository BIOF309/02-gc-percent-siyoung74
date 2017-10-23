# 02-gc-percent-siyoung74
seq=input("input your seq ")
total=len(seq)
g=seq.count("g")
c=seq.count("c")
percent=(g+c)/total*100
print("GC %:", percent, "%")
