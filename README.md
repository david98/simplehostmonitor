# Setup
    
**Python 3.7 is required.**

1. Either `git clone https://github.com/david98/simplehostmonitor.git` or download the whole repository
by clicking on *Clone or download* -> *Download ZIP*
2. Move into the downloaded folder and run `pip install -r requirements.txt`
3. Create a configuration file called `simplehostmonitor.conf` containing:
    
    >[email]  
    mailjet_public_key = YOUR MAILJET PUBLIC KEY  
    mailjet_secret_key = YOUR MAILJET SECRET KEY  
    sender_address = SENDER ADDRESS   
    send_email_to = WHERE YOU WANT TO RECEIVE EMAIL NOTIFICATIONS  
    [monitoring_target]  
    ip_address = THE TARGET'S IP ADDRESS  
    max_rtt = MAXIMUM PING IN MS  
    max_allowed_failures = HOW MANY FAILURES BEFORE TRIGGERING AN ALARM  
    period = HOW MANY MS BETWEEN CHECKS
4. Run `python3.7 simplehostmonitor.py`
5. Log files will be created inside the program's directory.