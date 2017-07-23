# -*- coding: utf-8 -*-
picnicItems = {'apples': 5, 'cups': 2}
print 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
print 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# print 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
picnicItems.setdefault('eggs', 0)
picnicItems.setdefault('eggs', 9) # setdefault方法在字典中不存在该项时默认设置，若存在该项则不变
print picnicItems