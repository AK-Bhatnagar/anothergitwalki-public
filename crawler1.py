import os
path = "my-treerd-folder"
print(os.environ['CNVRG_JOB_ID'])
os.chdir('output')
for i in range (1, 10000):
    f = open("{}/demofile{}.txt".format(path, i), "a")
    f.write("secondcontent")
    f.close()
