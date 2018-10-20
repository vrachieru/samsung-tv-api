import sys
sys.path.append('../')

from samsungtv import SamsungTV

tv = SamsungTV('192.168.xxx.xxx')
tv.power()