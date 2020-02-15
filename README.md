# port-monitoring

WHAT IS IT ?


A python script to monitor activity on a given port .
It works on a simple concept of basic socket programing

SETUP ?


set port on which activity to be monitored to port as python port 
change port of process to be monitord to any free port over 1024 which is free.
run the python script 
you will get data being transmitted to and from on console
enjoy !!!!


HOW IT WORKS ??


heres what happens :
  Incomming data belives its talking to say port 80 standard for webserver.
  But infact we are running our socket here which will recv message.
  We then note message.
  we then create a socket connection with the actual process (manually changed to 2222)
  we send the exact message we rercieved on port 80
  and the response we get note it.
  then send  response recieved to original client.
  
  NOTE :
  
  
  this can be used to tamper unencrpted data 
  AND NOT BE USED FOR MALICIOUS PURPOSES.
  
  THIS SCRIPT IS FOR EDUCATIONAL PURPOSE ONLY
