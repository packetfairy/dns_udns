So, here's what I do to make this work.

First, make sure you have python3 and python virtualenv set up.

From the base of this directory, run the following commands:

# set up and use python virtual environment
virtualenv venv
cd venv
. bin/activate

# download and install dependencies into local virtual environment
pip install -r requirements.txt
pip install -e plugins

# enable plugin
pip install -e plugins


Next, edit plugins/dns_udns.py, defining your UDNS portal username
and password on lines 10 and 11.


Now you can invoke certbot using `-a dns_udns`

You should also reconfigure your cron entry (probably /etc/cron.d/certbot)
so that it uses the virtualenv-installed certbot binary. eg: if you
installed the base and venv as described at /home/user/udns, you would
declare it as /home/user/udns/bin/certbot in cron
