#
# Copyright (c) 2018 Bobby Noelte
#
# SPDX-License-Identifier: Apache-2.0
#



import logging

# globals
logger = logging.getLogger('DTS')

def log_init():
    # create logger
    ##logger = logging.getLogger('simple_example')
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    logging.warning('this is warning')
    logging.info('this is info')

    logger.setLevel(logging.DEBUG)
    logger.debug('debug message')
    logger.info('info message')
    logger.error('error message')
    logger.critical('critical message22')

