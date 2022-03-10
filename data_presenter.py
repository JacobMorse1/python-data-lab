open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     # print(line)


# flavors = []

# for line in open_file:
#    line = line.rstrip("/n").split(",")
#    for value in line:
#        flavors.append(value)
       
# every_third = flavors[2::5]
# print(every_third)


# for line in open_file:
#     line = line.rstrip("/n").split(",")
#     print(float(line[3]) + float(line[4]))

total = 0
for line in open_file:
    line = line.rstrip("/n").split(",")
    total_new = (int(line[3]) * (float(line[4])))
    total += total_new 
    
print(total)    

open_file.close()


    
    

