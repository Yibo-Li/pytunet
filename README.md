# TUNET

TUNET is a python tool to login and logout Tsinghua University Network (tunet).

To use this do as below:

```python
# install from pip
pip install tunet

# import tunet package
import tunet

# set login/logout options
options = {
    'name': 'user_name',    # required, 'user_name' and 'user_name@tsinghua' are for access public internet and tunet, respectively
    'pwd': 'user_password', # required, password for tunet account 'user_name'
    'ip': '192.168.1.1'     # optional, the ip you want to authenticate, and default is the client ip
}

# do login
tunet.login(options['name'], options['pwd'], options['ip'])
# Login is successful.

# do logout
tunet.logout(options['name'], options['ip'])
# Logout is successful.
```
