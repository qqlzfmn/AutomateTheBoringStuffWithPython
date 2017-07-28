market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


# 在运行Python 时传入-O 选项，可以禁用断言。


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)  # 确保至少一个交通灯是红色


switchLights(market_2nd)
