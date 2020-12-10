small exercice for upstride interview

Last answers 
If the backend is slow to process response (ex. add a function call with a sleep time of two minutes into the back <put> endpoint). How do you speed up the response to the user while still processing the response?
  >>i have added a session to handle asynchronous request, to let server process request and handle state. I'd suggest to use redis or any pub sub if the process is to be long enough, and mqrk every process with an uuid
  
 Idempotency is important in web applications, given that a request could be repeated by the network toward the frontend or the backend. How could you improve the application in order to guarantee that a request is only executed once?
  >>UUIDs would mark uniquely every process. In conjuction with a redis, we would know for sure a process/request is not repeated
 
 A service in production has security leaks. What are the immediate patches you could apply to the service configuration to block standard cyber attacks (DDOS, brute forcing ..)?
  >>Do not expose backend services nor db to exterior, adding firewall policies (and check if load balancer scale correctly etc.), only authorized users can perfom actions or trigger processes with the app, use sercurity certificates
 
