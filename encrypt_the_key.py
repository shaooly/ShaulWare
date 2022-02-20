import os


counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = input("What are you looking for?:> ")
this_dir = os.getcwd()
for r, d, f in os.walk(r"C:\Users\shaoo\PycharmProjects\ShaulWare\venv\hello"): # change the hard drive, if you want
    for file in f:
        filepath = os.path.join(r, file)
        print(filepath)
print(f"trovati {counter} files.")