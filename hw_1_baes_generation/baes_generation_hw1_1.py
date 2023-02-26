import pprint
import random

# возможные элементы стиля
styles = {
    'прическа':[
        'нет волос',
        'длинные в пучок',
        'длинные волнистые',
        'длинные прямые',
        'короткая волнистые',
        'короткая прямые',
        'короткая курчавые'
    ],
    'цвет волос':[
        'черный',
        'блонд',
        'каштановый',
        'пастельный розовый',
        'рыжий',
        'серебристо серый',
    ],
    'аксесуар':[
        'нет очков',
        'круглые очки',
        'солнцезащитные очки',
    ],
    'одежда':[
        'худи',
        'комбинезон',
        'футболка с круглым вырезом',
        'футболка с V-вырезом',
    ],
    'цвет одежды':[
        'черный',
        'синий',
        'серый',
        'зеленый',
        'оранжевый',
        'розовый',
        'красный',
        'белый'
    ],
}
# количество элементов стиля в наблюдаемых данных
styles_count = {
    'прическа':[
        7,
        0,
        1,
        23,
        1,
        11,
        7
    ],
    'цвет волос':[
        7,
        6,
        2,
        3,
        8,
        24,
    ],
    'аксесуар':[
        11,
        22,
        17,
    ],
    'одежда':[
        7,
        18,
        19,
        6,
    ],
    'цвет одежды':[
        4,
        5,
        6,
        8,
        6,
        8,
        7,
        6
    ],
}


"""print(styles_count.keys())
for k in styles_count.keys():
    summ = 0
    for s in styles_count[k]:
         summ += s
    print(k, summ)"""

num = 0
prev_sum = 0
for k, v in styles_count.items():
    summ = sum(v)
    print(k, summ)
    if num >= 1: # проверка входных данных
        if prev_sum != summ:
            print('проверьте данные, ошибка в параметре', k)
            print('дальнейшие цифры некорректны')
            break
    num += 1       
    prev_sum = summ   
    
        
    
p={}
for k in styles:
    p[k] = []
    for n, i_style in enumerate(styles[k]):
        p_n = (styles_count[k][n] +1) / ((sum(styles_count[k]) + len(styles_count[k])))
        p[k].append(p_n)
pprint.pprint(p)

feature = 'аксесуар'
result_style = {}
for feature in styles:
    p_acc = p[feature]
    acc = styles[feature]
    result_style[feature] = random.choices(acc, p_acc)[0]
if result_style['прическа']  == 'нет волос':
    result_style.pop('цвет волос')
print(result_style)

for i in p:
    print(i, sum(p[i]))