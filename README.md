# reply-timer

Created as a Joke. But maybe someone has a use for it :)

Please don't assume that this software is safe to use :)

This a a small python script spinning up an Website on port 8000, which display a reminder that a message has not been answered since a certain date.

## Installation:

### Manual (not recommended):

    git clone https://github.com/kurzschlussidi/reminder.git
    cd reminder
    pip install flask
    python app.py

Use as is, or point your reverse proxy towards the ip:port of this instance.

### Docker (recommended):

    docker run -d -p 80:8000 -v '/mnt/user/appdata/reminder':'/reminder/data':'rw' kurzschlussidi/reply-timer

Use as is, or point your reverse proxy towards the ip:port of this instance.

## Usage:

Open the Website and generate a link which you can send to the receiver
    
