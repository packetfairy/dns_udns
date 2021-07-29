certbot DNS Authenticator Plugin for UltraDNS

# set up and use python virtual environment
virtualenv venv
cd venv
. bin/activate

# download and install dependencies into local virtual environment
pip install -r requirements.txt

# enable plugin
pip install -e plugins


Next, edit plugins/dns_udns.py, defining your UDNS portal username
and password on lines 10 and 11. Alternatively, you could define
username and password in a credentials file and then load that file,
but I just didn't care enough, and wanted it to be able to operate
without manual intervention.

Now you can invoke certbot using `-a dns_udns`

You should also reconfigure your cron entry (probably /etc/cron.d/certbot)
so that it uses the virtualenv-installed certbot binary. eg: if you
installed the base and venv as described at /home/user/udns, you would
declare it as /home/user/udns/bin/certbot in cron
