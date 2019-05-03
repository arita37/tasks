

import os, sys
from time import sleep

out_file = "/home/ubuntu/zs3drive/tasks_out/t_github_test02.txt"

with open(out_file, mode="a") as f :
  for i in range(0, 25)
    f.write(  "{i} \n".format(i=i)   )
    sleep(2)



