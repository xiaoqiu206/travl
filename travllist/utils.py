# coding=utf-8
'''
Created on 2015年4月22日

@author: Administrator
'''
from django.core.paginator import Paginator


def page(query_set, page_num, wanted_page=1):
    '''
    分页,query_set是没分页的数据,page_num是每页记录数,wanted_page是页数
    '''
    page_maker = Paginator(query_set, page_num)
    re_data = {}
    re_data['page_num'] = page_num
    re_data['total_num'] = page_maker.count  # 总记录数
    re_data['total_pages'] = page_maker.num_pages  # 总页数
    re_data['wanted_page'] = wanted_page

    wanted_page_data = page_maker.page(int(wanted_page))
    re_data['data_list'] = wanted_page_data.object_list
    re_data['page_up'] = wanted_page_data.has_previous()
    re_data['page_down'] = wanted_page_data.has_next()
    re_data['previous_page'] = int(wanted_page) - 1
    re_data['next_page'] = int(wanted_page) + 1

    return re_data

    