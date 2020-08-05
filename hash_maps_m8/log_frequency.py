test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
  logFrequency= {}
  
  for log in logs:
    warning, message = log.split(': ')
    issue, subMsg= warning.split(']')
    issue = issue.replace('[','')

    num, test = str(subMsg.split()[0]), ' '.join(subMsg.split()[1:])
    
    if issue not in logFrequency:
      logFrequency.update({issue:{num:{test:{message:1}}}})
    else:
      if message in logFrequency[issue][num][test]:
        logFrequency[issue][num][test][message]+=1
      else:
        logFrequency[issue][num][test].update({message:1})
    
    
    
  return(logFrequency)

    
print(log_stats(test_data))