#encoding=utf-8
with open(r"/home/yxran/下载/shuwa/python/作业/太空旅客.txt", 'r') as readFile:
  list={} #初始化字典
  import re
  txt = readFile.read() #read() 每次读取整个文件，通常用于将文件内容放到一个字符串变量中
def operator(string):
    with open(string, 'r') as readFile:
        for line in readFile.readlines():# 不加s，就会只读第一行；内存不够时才用readline
            line = line.strip('\n') #去掉行之间的转义字符
            get = re.findall(line, txt)
            num = len(get)
            list[line] = num  #
    with open('/home/yxran/下载/shuwa/结果.txt','a') as writeFile: #用'w'的话之前的会被清除
        for line in list:
                writeFile.write(line)
                writeFile.write(':')
                writeFile.write(str(list[line]))# num是int型，但是存入的是字符
                writeFile.write('\n')
        list.clear()  # 如果不加这个，在执行正派的时候，之前的反派也会再过一次
operator("/home/yxran/下载/shuwa/python/作业/词典/角色/反派.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/角色/角色.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/角色/角色中的其他.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/角色/男主角.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/角色/女主角.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/角色/配角.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/剧情/发展.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/剧情/结局.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/剧情/剧情.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/剧情/开头.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/剧情/泪点.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/剧情/笑点.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/视听/动作.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/视听/画面.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/视听/镜头.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/视听/视听.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/视听/视听效果中的其他.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/视听/音乐.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/制作/编剧.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/制作/出品公司.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/制作/导演.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/制作/选景.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/制作/制作.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/主题/主题.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/主题/风格.txt")
operator("/home/yxran/下载/shuwa/python/作业/词典/主题/题材内容.txt")