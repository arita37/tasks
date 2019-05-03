#
"""
python zs3drive/tasks/t_github_test02/main.py

with open(out_file, mode="w") as f :
  for i in range(0, 25)
    f.write(  "{i} \n".format(i=i)   )
    sleep(2)
out_file = "/home/ubuntu/zs3drive/tasks_out/t_github_test02.txt"


"""
import os, sys
from time import sleep

####################################################################################################


task_cpu_required   = 2  #  Nb of CPU required for this task....
taskout_s3_root    =  "/home/ubuntu/zs3drive/tasks_out/" 
taskout_local_root = "/home/ubuntu/tasks_out/" 







####################################################################################################
# print( __file__ )
task_name      =  __file__.split("/")[-2]
taskout_local = taskout_local_root + task_name   
taskout_s3    = taskout_s3_root   + task_name + "/"

if os.path.exists( taskout_local ) :
   print("Task out Local Folder already exist")
else :
   os.system("mkdir " + taskout_local )
####################################################################################################

# print( local_taskout, s3_taskout)


def os_copy_local_to_s3( taskout_local, taskout_s3_root ) :
  
  task_name =  taskout_local.split("/")[-1]
  if not os.path.exists(  taskout_s3_root   ) :
    os.system("mkdir " + taskout_s3_root   )

  if os.path.exists(  taskout_s3_root + "/" + task_name   ) :
    print("Task out s3 Folder already exist, Overwriting", taskout_s3_root + "/" + task_name   )


  cmd =  " cp -r {a}  {b}".format(a=taskout_local, b=taskout_s3_root  )
  msg = os.system(cmd)
  print("Copy success", msg)
 
 




"""





"""
