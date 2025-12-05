import os
import csv

working_dir = r"C:\Users\r-kajihara\Documents\Python\Versatilel_VirEnv\test"
file_name = "01.brs"
each_file = os.path.join(working_dir, file_name) 
save_file = os.path.join(working_dir, "01save.brs") 
with open(each_file, "r", encoding="SHIFT-JIS") as file_data:
#    r1 = file_data.read()
#    r2 = file_data.readline()
    r3 = file_data.readlines()

data_length = int(r3[174])

new_data = r3[175:176+data_length:10]
new_all_data = r3[:175]+new_data
print(new_data[:10])
print(new_all_data)

with open(save_file, mode="w", encoding="SHIFT-JIS") as save_data:
    save_data.writelines(new_all_data)
