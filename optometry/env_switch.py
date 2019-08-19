# -*- coding:utf-8 -*-
from logzero import logger


class EnvOptions(object):
    UAT_TEST = 1
    UAT_WENYI = 2
    T27 = 3
    YOT_TEST = 4
    T27_TEST = 5


# 设置测试环境
ENABLED_ENV = EnvOptions.YOT_TEST

if ENABLED_ENV == EnvOptions.YOT_TEST:
    from env_settings import settings_yot_test as settings
    from env_constants import constants_yot_test as constants
elif ENABLED_ENV == EnvOptions.T27_TEST:
    from env_settings import settings_t27_test as settings
    from env_constants import constants_t27_test as constants
elif ENABLED_ENV == EnvOptions.UAT_TEST:
    from env_settings import settings_uat_test as settings
    from env_constants import constants_t27_test as constants
elif ENABLED_ENV == EnvOptions.T27_WENYI:
    from env_settings import settings_t27_wenyi as settings
    from env_constants import constants_t27_wenyi as constants
else:
    logger.debug("Not support for now. please set env_settings and env_constants for it!!!")


if __name__ == "__main__":
    print settings.TENANT_ID
    print constants.DRUG_FACTORYID
