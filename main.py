from __future__ import print_function

import os
import time

import redis
from bluelens_log import Logging
from bluelens_k8s.pod import Pod


REDIS_TICKER_KEY = os.environ['TICKER_KEY']
REDIS_TICKER_VALUE = os.environ['TICKER_VALUE']

SPAWN_ID = os.environ['SPAWN_ID']
RELEASE_MODE = os.environ['RELEASE_MODE']
REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

rconn = redis.StrictRedis(REDIS_SERVER, port=6379, password=REDIS_PASSWORD)

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-ticker')

class Ticker(Pod):
  def __init__(self):
    super().__init__(REDIS_SERVER, REDIS_PASSWORD, rconn, log)

  def run(self):
    while True:
      time.sleep(REDIS_TICKER_VALUE)
      rconn.lpush(REDIS_TICKER_KEY, '@')

if __name__ == '__main__':
  log.info('Start bl-ticker:1')

  try:
    ticker = Ticker()
    ticker.run()
  except Exception as e:
    log.error(str(e))
