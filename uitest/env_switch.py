# -*- coding:utf-8 -*-
from logzero import logger


class EnvOptions(object):
    UAT_TEST = 1        #预发布
    UAT_WENYI = 2
    T27 = 3
    YOT_TEST = 4        #试用环境
    T27_TEST = 5        #测试环境27


# 设置测试环境
ENABLED_ENV = EnvOptions.UAT_TEST

if ENABLED_ENV == EnvOptions.YOT_TEST:
    from env_constants import constants_yot_test as constants
elif ENABLED_ENV == EnvOptions.T27_TEST:
    from env_constants import constants_t27_test as constants
elif ENABLED_ENV == EnvOptions.UAT_TEST:
    from env_constants import constants_uat_test as constants
else:
    logger.debug("Not support for now. please set  env_constants for it!!!")


if __name__ == "__main__":
    print('url', constants.url)
