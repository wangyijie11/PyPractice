#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import logging.config
import yaml

logging.basicConfig(filename='example.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# 通过yaml文件配置logging
f = open('logging.conf.yaml')
dic = yaml.safe_load(f)
f.close()
logging.config.dictConfig(dic)


# 创建logger
logger = logging.getLogger('simpleExample')

# 输出日志
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')