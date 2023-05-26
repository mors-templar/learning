main_list = ["ASD" , "MNB" , "aer", "mfj", "NOP", "ZKL", "ndp", "zdf"]
AtoM = []
NtoZ = []
for index in range(len(main_list)):
    in_str = main_list[index]
    ch = in_str[:1]
    ch = ch.upper()
    if 'M' >= ch >= 'A':
        AtoM.append(in_str)
    else:
        NtoZ.append(in_str)


print(AtoM)
print(NtoZ)