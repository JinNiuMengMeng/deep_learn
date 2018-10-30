# encoding: utf-8
# import pymysql.cursors
import numpy as np
import pandas as pd

import matplotlib as mpl
# matplotlib.use('agg')
import matplotlib.pyplot as plt

mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False
# 连接数据库
# connect = pymysql.Connect(host="localhost", port=3306, user='root', passwd='12345678', db='icar_active', charset='utf8')
# # 获取游标
# cursor = connect.cursor()
# #打印数据
# lis=[]
# for x in range(0,16):
#     cursor.execute("select count(*) from usr_active_log where act_type=%s",x)
#     lis.append(list(cursor.fetchall())[0][0])
# #     print (lis[x])
# # print (lis)

# cursor.close()
# connect.close()

labels = ['无', '一秀', '二举', '四进', '四进带一秀', '四进带二举', '三红', '对堂', '状元', '五子', '五子带四', '五红', '黑六勃', '遍地锦', '红六勃', '状元插金花']
fracs = [90988, 110016, 58375, 7585, 3809, 511, 15915, 4537, 2213, 726, 173, 203, 21, 5, 8, 91]
explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1]  # 0.1 凸出这部分，
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
# autopct ，show percet
plt.pie(x=fracs, explode=explode, labels=labels, autopct='%3.1f %%', shadow=True, labeldistance=1.1, startangle=90,
        pctdistance=0.6)
'''
labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
shadow，饼是否有阴影
startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
pctdistance，百分比的text离圆心的距离
patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
'''

plt.show()
