def server_time_check(task_config, task_times):
  num_tasks, time = map(int, task_config.split())
  tasks = list(map(int, task_times.split()))
  count = 0
  sum = 0
  for x in tasks:
    count+=x
    if count > time:
      return(sum)
    sum+=1
    
   
  

## Please do not change the code below this line
## These lines are how the tests interact with the code
if __name__ == "__main__":
  task_config = input("Please input the number of tasks, and the maximum total execution time:")
  task_times = input("Please input the execution times of each task, seperated with a space:")
  
  print(server_time_check(task_config, task_times))
