import os


counter = 0
print("If you want all the excel file, for example write .xlsx")
this_dir = os.getcwd()
for r, d, f in os.walk(r"D:\Users\Student\Desktop\big"): # change the hard drive, if you want
    print(f'r: {r}')
    print(f'f: {f}')
    print(f'd: {d}')