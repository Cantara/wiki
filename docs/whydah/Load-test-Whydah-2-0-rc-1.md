# Load test Whydah 2.0-rc-1

### Background

We want to ensure the robustness and scaleabillity of all stable Whydah releases

### Test set-up

Version tested:  
- **Whydah 2.0<sub>~rc</sub><sub>1**  25.9</sub><sub>2014  12:00</sub>~15:00 GST+1

**Whydah configuration:**
- Amazon AWS EC2 cloud deployment (region=us<sub>~east</sub>~1)
    - Amazon Elastic Load Balancer in front of the 10 front-servers running amazon linux - latest version
    - Front-servers: 10 T2 micro servers running SSOLoginWebApp, SecurityTokenService(hazelcast clustered) and TestWebApp with apache proxypass to localhost
    - Backend-server: one of the 10 front servers are also running UAWA and UIB with embedded ApacheDS and HSQLDB (not optimal, as of memory contraints on T2 micro instances)
- Detailed configuration descriptions
    - [SSOLoginWebApp HA configuration (AWS ELB and Apache front)](SSOLoginWebApp<sub>~HA</sub><sub>configuration</sub><sub>AWS</sub><sub>ELB</sub><sub>and</sub>~Apache-front.md)
    - [SecurityTokenService HA configuration (AWS EC2 Hazelcast)](SecurityTokenService<sub>~HA</sub><sub>configuration</sub><sub>AWS</sub>~EC2-Hazelcast.md)

**Load-test configuration:**
- Simple loader.io setup
    - Testing two requests in sequence
        - LOGON:  /sso/action (Params:  redirectURI, name and password)
        - Pick up existing session:  /tokenservice/user/xxx/get_usertoken_by_usertokenid  (Params: usertokenid (from cookie), apptoken (hardcoded), apptokenid (hardcoded)
    - Manual creation of application session and user session, sessiondata inserted into test
- Load (1)
    - 1000 clients / test
    - Duration: 1 min
- Load (2)
    - 250 clients / second
    - Duration: 1 min

**Results:**
- average response time: 67 ms / 72 ms
- average error rate: 0.0 % / 0.0 %
- Successful responses: 2000 / 20.000
- Received†	2.06 MB / 21.12 MB
- Sent	1.39 MB / 13.81 MB

**Comments:**
- No undesired behavior observed in logs, server<sub>~monitoring or elb</sub>~monitoring
- Manual test simultaneously did work as usual
- Running the test several times result in similar results
- Test was done with extensive logging (level: TRACE) less aggressive logging should increase performance

**Reflections:**
- By running different loads, we see that a T2 microserver can handle about 200 logon/pick up session request a second. The heavy operation is logon, as it has to go all the way to UIB(singleton). On higher load, the response<sub>~time increases (for 500 reqs/s it is 2</sub>~3 s).
- A more realistic test<sub>~suite, say 50/1 pickup session/logon should handle 300</sub>~400 request/second on T2 micro servers
- 90% of the Whydah operations scales almost linearly, the exception beeing the few operations which hit the UIB instance.
