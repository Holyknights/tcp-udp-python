import sys
import time
def process_bar(precent, width=50):
    use_num = int(precent*width)
    space_num = int(width-use_num)
    precent = precent*100
    #   第一个和最后一个一样梯形显示, 中间两个正确,但是在python2中报错
    #
    # print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent))
    # print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent), end='\r')
    print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')
    # print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True)

# for i in range(21):
#     precent = i/20
#     process_bar(precent)
#     time.sleep(0.2)
