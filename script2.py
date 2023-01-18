import os

path = "my-treerd-folder"
print(os.environ["CNVRG_JOB_ID"])
os.mkdir(path)
for i in range(1, 10000):
    with open("output/exp_file_no_{}".format(i), "w") as f:
        f.write("Now the file has more content!")
    f.close()
