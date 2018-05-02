import tunet

options = {
    'name': 'user_name',
    'pwd': 'user_password',
    'ip': '192.168.1.1'
}
tunet.login(options['name'], options['pwd'], options['ip'])
