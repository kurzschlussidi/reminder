# reply-timer

Created for a Joke. But maybe someone has a use for it :)

Please don't assume that this software is safe to use :)

This a a small python script spinning up an Website on port 8000, which display a reminder that a message has not been answered since a certain date.

##Installation:
###Manual (not recommended):
    git clone https://github.com/kurzschlussidi/reminder.git
    cd reminder
    pip install flask
    python app.py
Connect your reverse-proxy to this url and port.
###Docker (recommended):
    docker run -d -p 80:8000 kurzschlussidi/reply-timer
Connect your reverse-proxy to this url and port.
##Usage:
Send the person you want to remind a link with the following syntax:

    yoursubdomain.yourdomain/?date=YYYY-MM-DD-HH-MM&sender=YourName&receiver=ReceiversName

for example:

    reminder.mydomain/?date=2020-11-23-20-22&sender=Markus&receiver=Horst
    