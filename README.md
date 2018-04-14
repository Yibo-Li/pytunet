# TUNET

TUNET is a python tool to login and logout Tsinghua University Network (tunet).

To use this do as below:

```python
import tunet

// do login
options = {
    'name': 'user_name',
    'pwd': 'user_password'
}
tunet.login(options['name'], options['pwd'])
// Login is successful.

// do logout
tunet.logout()
// Logout is successful.
```
