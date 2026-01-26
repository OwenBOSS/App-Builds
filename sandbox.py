import re

file = r"\\zfa.com\SR\Projects\2025\25075 Amador Valley High School\3_Calculations\Building N - Practice Gym\Calc Set PDFs\14_Swap1 Rafter near NC-NB.pdf"

ms = re.search(r"swap\d+", file.lower())
swapnum = ms.group(0)

file_name = file.lower().replace(f"{swapnum} ", "").replace(swapnum, "")

print(swapnum)
print(file_name)