# -*- coding=utf-8 -*-
from service.optometry_service import get_factory_info


def test_factory_mfr_not_exists():
    # 视光厂商获取（厂商不存在）
    get_factory_info('123456789', exp_http_status=500, exp_status='0099',
                     exp_message=u'class java.lang.NullPointerException')
