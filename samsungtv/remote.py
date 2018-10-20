import base64
import json
import logging
import time
import websocket

class SamsungTV():

    _URL_FORMAT = 'ws://{host}:{port}/api/v2/channels/samsung.remote.control?name={name}'

    _KEY_INTERVAL = 1.5

    def __init__(self, host, port=8001, name='SamsungTvRemote'):
        self.connection = websocket.create_connection(
            self._URL_FORMAT.format(**{
                'host': host, 
                'port': port, 
                'name': self._serialize_string(name)
            })
        )

        response = json.loads(self.connection.recv())
        if response['event'] != 'ms.channel.connect':
            self.close()
            raise Exception(response)

    def __exit__(self, type, value, traceback):
        self.close()

    def _serialize_string(self, string):
        if isinstance(string, str):
            string = str.encode(string)
        return base64.b64encode(string).decode('utf-8')

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            logging.debug('Connection closed.')

    def send_key(self, key, repeat=1):
        for n in range(repeat):
            payload = json.dumps({
                'method': 'ms.remote.control',
                'params': {
                    'Cmd': 'Click',
                    'DataOfCmd': key,
                    'Option': 'false',
                    'TypeOfRemote': 'SendRemoteKey'
                }
            })

            logging.info('Sending key %s', key)
            self.connection.send(payload)
            time.sleep(self._KEY_INTERVAL)

    # power
    def power(self):
        self.send_key('KEY_POWER')

    # menu
    def home(self):
        self.send_key('KEY_HOME')

    def menu(self):
        self.send_key('KEY_MENU')

    def source(self):
        self.send_key('KEY_SOURCE')

    def guide(self):
        self.send_key('KEY_GUIDE')

    def tools(self):
        self.send_key('KEY_TOOLS')

    def info(self):
        self.send_key('KEY_INFO')

    # navigation
    def up(self, count=1):
        self.send_key('KEY_UP', count)

    def down(self, count=1):
        self.send_key('KEY_DOWN', count)

    def left(self, count=1):
        self.send_key('KEY_LEFT', count)

    def right(self, count=1):
        self.send_key('KEY_RIGHT', count)

    def enter(self, count=1):
        self.send_key('KEY_ENTER', count)

    def back(self, count=1):
        self.send_key('KEY_RETURN', count)

    # channel
    def channel_list(self):
        self.send_key('KEY_CH_LIST')    

    def channel(self, ch):
        for c in str(ch):
            self.digit(c)
        self.enter()

    def digit(self, d):
        self.send_key('KEY_' + d)

    def channel_up(self, count=1):
        self.send_key('KEY_CHUP', count)

    def channel_down(self, count=1):
        self.send_key('KEY_CHDOWN', count)

    # volume
    def volume_up(self, count=1):
        self.send_key('KEY_VOLUP', count)

    def volume_down(self, count=1):
        self.send_key('KEY_VOLDOWN', count)

    def mute(self):
        self.send_key('KEY_MUTE')

    # extra
    def red(self):
        self.send_key('KEY_RED')

    def green(self):
        self.send_key('KEY_GREEN')

    def yellow(self):
        self.send_key('KEY_YELLOW')

    def blue(self):
        self.send_key('KEY_BLUE')