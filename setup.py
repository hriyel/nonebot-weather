import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '1.3'
DESCRIPTION = '一个以nonebot为框架的天气查询插件'
LONG_DESCRIPTION = ''

setup(
    name="nonebot-weather",
    version=VERSION,
    author="hriyel",
    author_email="1249781871@qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/hriyel/nonebot-weather.git",
    packages=find_packages(),
    keywords=['python', 'menu', 'dumb_menu','windows','mac','linux'],
    install_requires=[
    "nonebot2 >= 2.0.0b1",
    "nonebot-adapter-onebot >= 2.0.0b1"
    "aiohttp >= 3.0"
    ]
)
