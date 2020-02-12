import time

from bert_base.client import BertClient
with BertClient(show_server_config=False, check_version=False, check_length=False, mode='NER') as bc:

    start_t = time.perf_counter()
    str = ' 民航总医院医疗保险专用处方,朝羽区红庙北里81-1-201,姓名:牛艳利,性别:女,金果饮,病情及诊断:,1.上呼吸道感染;2.,口服,气管支气管炎;3.咽,连花清瘟颗粒,炎.,口服,2018年11月23日,呼吸内科,病情及诊断:'
    rst = bc.encode([str, str])
    print('rst:', rst)
    print(time.perf_counter() - start_t)