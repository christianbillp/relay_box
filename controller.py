import paramiko

class Controller():

    client = paramiko.SSHClient()

    def __init__(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname='10.42.1.250',
                       port=22,
                       username='pi',
                       password='raspberry')
    
    def activate(self, channel):
        stdin, stdout, stderr = self.client.exec_command('/usr/bin/python3 /home/pi/relay_box/relay.py a {}'.format(channel))
    
    def deactivate(self, channel):
        stdin, stdout, stderr = self.client.exec_command('/usr/bin/python3 /home/pi/relay_box/relay.py d {}'.format(channel))

if __name__ == '__main__':
    co = Controller()
    co.deactivate(1)
