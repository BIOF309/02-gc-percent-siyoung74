# 02-gc-percent-siyoung74

# This sequence is the first 100 nucleotides of the Influenza H1N1 Virus segment 8
#flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'
seq_raw = input("Please enter sequence into GC calculator: ")
print("The sequence you enter is: " + seq_raw)
seq = seq_raw.upper()
print(seq)
#seq=input("input your seq ")
total=len(seq)
g=seq.count("G")
c=seq.count("C")
percent=(g+c)/total*100
print("GC %:", percent, "%")
