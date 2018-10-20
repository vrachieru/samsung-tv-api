<p align="center">
    <img src="https://user-images.githubusercontent.com/5860071/47255992-611d9b00-d481-11e8-965d-d9816f254be2.png" width="300px" border="0" />
    <br/>
    <a href="https://github.com/vrachieru/samsung-tv-api/releases/latest">
        <img src="https://img.shields.io/badge/version-1.0.0-brightgreen.svg?style=flat-square" alt="Version">
    </a>
    <a href="https://travis-ci.org/vrachieru/samsung-tv-api">
        <img src="https://img.shields.io/travis/vrachieru/samsung-tv-api.svg?style=flat-square" alt="Version">
    </a>
    <br/>
    Samsung Smart TV API wrapper
</p>

This project is a library for remote controlling Samsung televisions via a TCP/IP connection. 
It currently supports modern (post-2016) TVs with Ethernet or Wi-Fi connectivity.

## Install

```bash
$ pip3 install git+https://github.com/vrachieru/samsung-tv-api.git
```
or
```bash
$ git clone https://github.com/vrachieru/samsung-tv-api.git
$ pip3 install ./samsung-tv-api
```

## Usage

```python
from samsungtv import SamsungTV

tv = SamsungTV('192.168.xxx.xxx')
tv.power() # toggle power
```

## License

MIT