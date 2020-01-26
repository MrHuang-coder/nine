from collections import OrderedDict

vocabulary_meanig = OrderedDict()

vocabulary_meanig['print'] = '将输出打印在屏幕上'
vocabulary_meanig['and'] = '与逻辑关系'
vocabulary_meanig['int'] = '整数类型'
vocabulary_meanig['float'] = '浮点数类型'
vocabulary_meanig['input'] = '通过键盘输入'

for name, meaning in vocabulary_meanig.items():
    print(name.title() + "'s vocabulary meaning is" + meaning.title() + ".")