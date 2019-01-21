# Setup
    
**Python 3.7 is required.**

1. Either `git clone https://github.com/david98/simplehostmonitor.git` or download the whole repository
by clicking on *Clone or download* -> *Download ZIP*
2. Move into the downloaded folder and run `pip install -r requirements.txt`
3. Create a configuration file called `simplehostmonitor.conf` containing:
    
    >[email]  
    mode = HTTP || SMTP (HTTP uses mailjet's REST API to bypass any firewall on port 25)  
    mailjet_public_key = YOUR MAILJET PUBLIC KEY  
    mailjet_secret_key = YOUR MAILJET SECRET KEY  
    sender_address = SENDER ADDRESS   
    send_email_to = WHERE YOU WANT TO RECEIVE EMAIL NOTIFICATIONS  
    [monitoring_target]  
    domain_name = TARGET'S DOMAIN NAME   
    *ip_address* = TARGET'S IP ADDRESS (*optional*, but overrides domain_name if present)  
    max_rtt = MAXIMUM PING IN MS  
    max_allowed_failures = HOW MANY FAILURES BEFORE TRIGGERING AN ALARM  
    period = HOW MANY MS BETWEEN CHECKS
4. Run `sudo python3.7 simplehostmonitor.py` on Linux. On Windows, run CMD or Powershell as admin and then run
`python3.7 simplehostmonitor.py`
5. Log files will be created inside the program's directory.