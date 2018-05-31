from setuptools import setup, find_packages

long_description = """# Jamaddr Python Package

This package Created by Jamison Emilio and packaged by Todd Albiston

## Description:
Python Package adds functions to convert IP address or subnet masks to bits and bit back up IP address.


```python
from jamaddr import JamAddr
ipbits = JamAddr.ip_to_bits("192.168.0.23")
ipbits
```

returns = '11000000101010000000000000010111'

```python
from jamaddr import JamAddr
bitsip = JamAddr.bits_to_ip("11000000101010000000000000010111")
bitsip
```

returns = '192.168.0.23'

#"""

setup(
    name='jamaddr27',
    version='0.2',
    packages=find_packages(),
    url='https://github.com/talbiston/jamaddr27.git',
    license='MIT',
    author='Jamison Emilio & Todd Albiston',
    author_email='foxtrot711@gmail.com',
    description='IP Subnet package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 2 ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
