import os
path = "my-treerd-folder"
print(os.environ['CNVRG_JOB_ID'])
os.chdir('output')
os.mkdir(path)
for i in range (10500):
    with open("output/exp_file_no_{}".format(i), "w") as f:
    f.write(str(i))
    f.close()
