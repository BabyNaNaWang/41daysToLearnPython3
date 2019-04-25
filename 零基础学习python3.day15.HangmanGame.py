import random
# 创建一个hangman的函数用于保存用于保存游戏
# 该方法接受word参数：
'''def hangman(word):
    # 定义一个变量保存出错次数
    wrong = 0
    # 定义stages列表，含组成人上吊需要的字符串
    stages = ['',
            '_____________         ',
            '|                     ',
            '|            |        ',
            '|            0        ',
            '|           /|\       ',
            '|           / \       ',
            '|                     '
    ]
    # 将传入的参数转换成列表，并赋值给rletter变量
    rletters = list(word)
    # 根据传入变量的长度，定义一个含与长度数字对应的下换线的列表
    # 并赋值给board
    board = ['_']*len(word)
    # 定义一个win变量判断游戏的输赢
    # 默认值为false
    win = False

    print('welcome to Hangman')
    # 定义游戏循环的条件，即：当游戏猜错数量小于参数长度时执行
    while wrong < len(stages) - 1:
        print('\n')
        # 键盘获取用户输入的内容
        msg = 'guess a letter'
        # 将用户输入的内容保存在变量char中
        char = input(msg)
        # 如果输入的内容在rletter列表中
        if char in rletters:
            # 查找输入内容所在索引
            cind = rletters.index(char)
            # 将下换线替换为输入内容
            board[cind] = char
            # 将字符库中已经找到的字符替换为$,
            # 否则永远在替换对应字符第一个索引
            rletters[cind] = '$'
        # 如果猜错了，猜错书加1
        else:
            wrong += 1
        # 将下划线打印
        print(' '.join(board))

        # 如果board列表中没有'_'则玩家赢，游戏结束
        if '_' not in board:
            print(' you win')
            # 打印board中的字母
            print(' '.join(board))
            print(board)
            win = True
            break
    # 如果输赢标记为False
    if not win:
        # 换行打印图案
        print('\n'.join(stages[0:wrong]))
        # 打印正确答案
        print('U lose! It wwas {}'.format(word))

hangman('class')'''
# 创建一个phrase的函数用于保存用于保存游戏
# 该方法接受word参数：
def phrase(word):
    
    # 定义一个变量保存出错次数
    wrongTims = 0
    
    # 定义一个判定输赢的标记
    winFlag = False
    
    # 定义stages列表，含组成人上吊需要的字符串
    stages = ['',
            '_____________         ',
            '|                     ',
            '|            |        ',
            '|            0        ',
            '|           /|\       ',
            '|           / \       ',
            '|                     ',
            '|                     '
    ]

    # 将传入的参数转换成列表，并赋值给rletter变量
    rletters = list(word)
    
    # 根据传入变量的长度，定义一个含与长度数字对应下换线个数的列表
    # 并赋值给board
    board = ['_']*len(word)

    # 游戏开场白
    print('欢迎来到猜成语游戏，猜错会挂人的哦！')

    # 定义游戏循环的条件，即：当游戏猜错数量小于参数长度时执行
    while wrongTims < len(stages)-1:
        print('\n')
        
        # 提示用户输入内容
        msg = '猜字：'

        # 获取玩家键盘输入内容并保存到变量中
        char = input(msg)

        # 判断用户输入内容是否在列表中，如果在则执行：
        if char in rletters:
            
            # 获取玩家输入内容在列表中的索引
            x = rletters.index(char)
            
            # 将列表中的值改为玩家输入内容
            board[x] = char
            
            # 将rletter中对应的字以*代替
            # 避免重复输入以及成语中重复字
            rletters[x] = '*'
        
        # 如果不在列表中则错误次数加1：
        else:
            wrongTims += 1
        
        # 打印猜中及未猜中情况。
        print(' '.join(board))
        
        # 打印与错误进度相匹配的上吊图案
        e = wrongTims + 1
        print('\n'.join(stages[0:e+1]))
        
        # board列表中不含下划线则玩家胜利，游戏结束
        if '_' not in board:
            print('真棒')
            print(' '.join(word))
            winFlag = True
            break
    # 循环结束后如果winFlag标记仍为
    if not winFlag:
        print('\n'.join(stages[0:wrongTims]))
        print('猜错啦，成语是{}'.format(word))

phraseLsit = ['行尸走肉','金蝉脱壳','百里挑一','背水一战','霸王别姬','海阔天空','情非得已']
word = random.choice(phraseLsit)
phrase(word)