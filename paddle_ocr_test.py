import time
import cv2
import pyautogui
from paddleocr import PaddleOCR

ocr=PaddleOCR(use_angle_cls = True,use_gpu= True)

def time_calc(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        f = func(*args, **kargs)
        exec_time = time.time() - start_time
        print("func.name:{}\texec_time:{}".format(func.__name__, exec_time))
        return f

    return wrapper

@time_calc
def get_ocr(key):
    text = ocr.ocr("screenshot.png",cls=True)
    # print(text)
    for i in text[0]:
        # print(i[1][0])
        if key in i[1][0]:
            print(i)
            position = i[0]
            # 顺时针
            (top_left, top_right, bottom_right, bottom_left) = position

            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            print(f'Character "{i[1][0]}" found at: top_left={top_left}, bottom_right={bottom_right}')
            target_x = int((top_left[0] + bottom_right[0]) / 2)
            target_y = int((top_left[1] + bottom_right[1]) / 2)
            # print(target_x, target_y)
            pyautogui.click(target_x, target_y)  # 左击坐标(100,150)
            break



if __name__ == "__main__":
    while  True:
        key_word = input("输入key:")
        get_ocr(key_word)

'''
[[[[21.0, 13.0], [53.0, 13.0], [53.0, 37.0], [21.0, 37.0]], ('9', 0.6127567887306213)], [[[232.0, 11.0], [437.0, 11.0], [437.0, 37.0], [232.0, 37.0]], ('、Paddle OCR使用-搜索', 0.977503776550293)], [[[608.0, 16.0], [773.0, 16.0], [773.0, 34.0], [608.0, 34.0]], ('Python最简单的OCF', 0.9456433057785034)], [[[971.0, 16.0], [1021.0, 16.0], [1021.0, 37.0], [971.0, 37.0]], ('保存py', 0.9205005168914795)], [[[1075.0, 16.0], [1189.0, 16.0], [1189.0, 34.0], [1075.0, 34.0]], ('i的截图-搜索', 0.9068277478218079)], [[[1328.0, 16.0], [1464.0, 16.0], [1464.0, 34.0], [1328.0, 34.0]], ('Python使用pyau', 0.9887786507606506)], [[[1512.0, 16.0], [1581.0, 16.0], [1581.0, 34.0], [1512.0, 34.0]], ('实现截屏', 0.9972867369651794)], [[[1680.0, 16.0], [1755.0, 16.0], [1755.0, 34.0], [1680.0, 34.0]], ('哗哩哗哩', 0.9370088577270508)], [[[96.0, 66.0], [128.0, 66.0], [128.0, 89.0], [96.0, 89.0]], ('C', 0.7492508292198181)], [[[235.0, 61.0], [515.0, 61.0], [515.0, 97.0], [235.0, 97.0]], ('https://www.bilili.com', 0.875352680683136)], [[[2168.0, 71.0], [2187.0, 71.0], [2187.0, 84.0], [2168.0, 84.0]], ('2.', 0.5793014764785767)], [[[19.0, 116.0], [147.0, 116.0], [147.0, 142.0], [19.0, 142.0]], ('机器学习', 0.999909520149231)], [[[147.0, 116.0], [269.0, 116.0], [269.0, 145.0], [147.0, 145.0]], ('网络安全 ', 0.9103788137435913)], [[[272.0, 116.0], [443.0, 116.0], [443.0, 145.0], [272.0, 145.0]], ('网页开发工具', 0.9995900988578796)], [[[445.0, 116.0], [536.0, 116.0], [536.0, 142.0], [445.0, 142.0]], ('算法', 0.9999316930770874)], [[[539.0, 116.0], [659.0, 116.0], [659.0, 142.0], [539.0, 142.0]], ('处理工具', 0.9995684027671814)], [[[672.0, 116.0], [787.0, 116.0], [787.0, 142.0], [672.0, 142.0]], ('常见问题', 0.9998595714569092)], [[[824.0, 116.0], [925.0, 116.0], [925.0, 142.0], [824.0, 142.0]], ('」游戏攻略', 0.8683235049247742)], [[[975.0, 122.0], [1016.0, 115.0], [1020.0, 136.0], [979.0, 143.0]], ('资源', 0.9995943307876587)], [[[1032.0, 116.0], [1152.0, 116.0], [1152.0, 142.0], [1032.0, 142.0]], ('腾讯开悟', 0.999283492565155)], [[[1168.0, 116.0], [1333.0, 116.0], [1333.0, 145.0], [1168.0, 145.0]], ('华为开发者联盟', 0.9995599389076233)], [[[37.0, 187.0], [256.0, 187.0], [256.0, 221.0], [37.0, 221.0]], ('首页番剧直播', 0.9903347492218018)], [[[275.0, 195.0], [336.0, 195.0], [336.0, 213.0], [275.0, 213.0]], ('游戏中', 0.9985396862030029)], [[[1019.0, 192.0], [1099.0, 192.0], [1099.0, 221.0], [1019.0, 221.0]], ('360智脑', 0.9991732835769653)], [[[2381.0, 187.0], [2472.0, 187.0], [2472.0, 224.0], [2381.0, 224.0]], ('投稿', 0.9988285303115845)], [[[2267.0, 213.0], [2344.0, 213.0], [2344.0, 232.0], [2267.0, 232.0]], ('创作中心', 0.9987285137176514)], [[[472.0, 434.0], [523.0, 434.0], [523.0, 463.0], [472.0, 463.0]], ('番剧', 0.9967614412307739)], [[[608.0, 434.0], [661.0, 434.0], [661.0, 463.0], [608.0, 463.0]], ('国创', 0.9999924302101135)], [[[741.0, 434.0], [795.0, 434.0], [795.0, 463.0], [741.0, 463.0]], ('综艺', 0.9997082948684692)], [[[880.0, 434.0], [931.0, 434.0], [931.0, 463.0], [880.0, 463.0]], ('动画', 0.9999037384986877)], [[[1016.0, 434.0], [1064.0, 434.0], [1064.0, 463.0], [1016.0, 463.0]], ('鬼畜', 0.9995203614234924)], [[[1155.0, 434.0], [1200.0, 434.0], [1200.0, 463.0], [1155.0, 463.0]], ('舞蹈', 0.9998300075531006)], [[[1288.0, 434.0], [1339.0, 434.0], [1339.0, 463.0], [1288.0, 463.0]], ('娱乐', 0.9975822567939758)], [[[1421.0, 434.0], [1475.0, 434.0], [1475.0, 463.0], [1421.0, 463.0]], ('科技', 0.9999508261680603)], [[[1560.0, 434.0], [1608.0, 434.0], [1608.0, 463.0], [1560.0, 463.0]], ('美食', 0.9999557733535767)], [[[1693.0, 434.0], [1744.0, 434.0], [1744.0, 463.0], [1693.0, 463.0]], ('汽车', 0.9997131824493408)], [[[1832.0, 434.0], [1883.0, 434.0], [1883.0, 463.0], [1832.0, 463.0]], ('运动', 0.999926745891571)], [[[1984.0, 432.0], [2325.0, 432.0], [2325.0, 466.0], [1984.0, 466.0]], ('目专栏活动社区中心', 0.9733137488365173)], [[[472.0, 492.0], [523.0, 492.0], [523.0, 521.0], [472.0, 521.0]], ('电影', 0.9999405741691589)], [[[597.0, 492.0], [675.0, 492.0], [675.0, 521.0], [597.0, 521.0]], ('电视剧', 0.9999445080757141)], [[[733.0, 492.0], [805.0, 492.0], [805.0, 521.0], [733.0, 521.0]], ('纪录片', 0.9996054768562317)], [[[877.0, 492.0], [933.0, 492.0], [933.0, 521.0], [877.0, 521.0]], ('游戏', 0.9999526739120483)], [[[1016.0, 492.0], [1067.0, 492.0], [1067.0, 521.0], [1016.0, 521.0]], ('音乐', 0.9999704360961914)], [[[1152.0, 492.0], [1203.0, 492.0], [1203.0, 521.0], [1152.0, 521.0]], ('影视', 0.9997687339782715)], [[[1288.0, 492.0], [1339.0, 492.0], [1339.0, 521.0], [1288.0, 521.0]], ('知识', 0.999962329864502)], [[[1421.0, 495.0], [1475.0, 495.0], [1475.0, 524.0], [1421.0, 524.0]], ('资讯', 0.9995858073234558)], [[[1560.0, 492.0], [1611.0, 492.0], [1611.0, 521.0], [1560.0, 521.0]], ('生活', 0.9999721050262451)], [[[1693.0, 492.0], [1744.0, 492.0], [1744.0, 521.0], [1693.0, 521.0]], ('时尚', 0.9999489784240723)], [[[1821.0, 492.0], [1891.0, 492.0], [1891.0, 521.0], [1821.0, 521.0]], ('更多', 0.9999282956123352)], [[[1984.0, 489.0], [2328.0, 489.0], [2328.0, 524.0], [1984.0, 524.0]], ('直播课堂新歌热榜', 0.9993767142295837)], [[[227.0, 500.0], [275.0, 500.0], [275.0, 532.0], [227.0, 532.0]], ('动态', 0.9998061656951904)], [[[333.0, 503.0], [379.0, 503.0], [379.0, 532.0], [333.0, 532.0]], ('热门', 0.9999339580535889)], [[[1536.0, 566.0], [1760.0, 566.0], [1760.0, 629.0], [1536.0, 629.0]], ('我做了一', 0.9550034999847412)], [[[1139.0, 608.0], [1328.0, 608.0], [1328.0, 653.0], [1139.0, 653.0]], ('Spring', 0.9228885173797607)], [[[1309.0, 603.0], [1403.0, 603.0], [1403.0, 653.0], [1309.0, 653.0]], ('JAI', 0.9201827645301819)], [[[1581.0, 642.0], [1813.0, 642.0], [1813.0, 708.0], [1581.0, 708.0]], ('理想中的', 0.9989039897918701)], [[[1168.0, 691.0], [1337.0, 674.0], [1344.0, 740.0], [1175.0, 757.0]], ('真香啊', 0.9568707942962646)], [[[1605.0, 708.0], [1789.0, 708.0], [1789.0, 755.0], [1605.0, 755.0]], ('工具网', 0.8670567870140076)], [[[1080.0, 750.0], [1165.0, 750.0], [1165.0, 779.0], [1080.0, 779.0]], ('2357', 0.9994155764579773)], [[[1176.0, 753.0], [1216.0, 753.0], [1216.0, 771.0], [1176.0, 771.0]], ('B2', 0.6255089640617371)], [[[1408.0, 753.0], [1456.0, 753.0], [1456.0, 774.0], [1408.0, 774.0]], ('03:48', 0.9752591848373413)], [[[1504.0, 747.0], [1664.0, 747.0], [1664.0, 776.0], [1504.0, 776.0]], ('44万551', 0.9940699934959412)], [[[1835.0, 753.0], [1880.0, 753.0], [1880.0, 774.0], [1835.0, 774.0]], ('05:57', 0.9449539184570312)], [[[1933.0, 750.0], [2040.0, 750.0], [2040.0, 776.0], [1933.0, 776.0]], ('216.1万', 0.997793436050415)], [[[1064.0, 800.0], [1247.0, 794.0], [1248.0, 831.0], [1065.0, 837.0]], ('Spring Al 真香啊', 0.9859898090362549)], [[[1491.0, 795.0], [1837.0, 797.0], [1837.0, 834.0], [1491.0, 831.0]], ('【耗时7个月】我做了一个工具网,', 0.9608966708183289)], [[[1917.0, 797.0], [2261.0, 795.0], [2261.0, 831.0], [1918.0, 834.0]], ('当coser拿出假胸 阁下又该如何应', 0.996318519115448)], [[[1499.0, 834.0], [1704.0, 834.0], [1704.0, 866.0], [1499.0, 866.0]], ('每个人都可以用的上', 0.999927818775177)], [[[1923.0, 832.0], [1965.0, 832.0], [1965.0, 863.0], [1923.0, 863.0]], ('对?', 0.7862555980682373)], [[[443.0, 876.0], [568.0, 876.0], [568.0, 916.0], [443.0, 916.0]], ('宣位', 0.6204542517662048)], [[[1069.0, 868.0], [1264.0, 868.0], [1264.0, 897.0], [1069.0, 897.0]], (' Alan聊编程·7-28', 0.9841204881668091)], [[[1499.0, 871.0], [1739.0, 871.0], [1739.0, 897.0], [1499.0, 897.0]], ('4万点赞名字就叫30·7-1', 0.9990513920783997)], [[[1923.0, 868.0], [2069.0, 868.0], [2069.0, 897.0], [1923.0, 897.0]], ('四落九川·8-7', 0.9349367618560791)], [[[237.0, 1050.0], [709.0, 1050.0], [709.0, 1087.0], [237.0, 1087.0]], ('空投节来袭，特种兵速来领取夏日空投!', 0.9896918535232544)], [[[245.0, 1097.0], [448.0, 1097.0], [448.0, 1124.0], [245.0, 1124.0]], ('······.', 0.5885127186775208)], [[[1573.0, 1103.0], [1821.0, 1103.0], [1821.0, 1139.0], [1573.0, 1139.0]], ('公测签到送全英雄', 0.9922804832458496)], [[[1085.0, 1118.0], [1152.0, 1118.0], [1152.0, 1137.0], [1085.0, 1137.0]], ('69.4', 0.9992791414260864)], [[[1933.0, 1116.0], [2045.0, 1116.0], [2045.0, 1142.0], [1933.0, 1142.0]], ('54.8万', 0.9965654611587524)], [[[1067.0, 1168.0], [1360.0, 1168.0], [1360.0, 1195.0], [1067.0, 1195.0]], ('【ai】ai眼中的你们不要再打了', 0.9753141403198242)], [[[1491.0, 1163.0], [1845.0, 1163.0], [1845.0, 1197.0], [1491.0, 1197.0]], ('轻松爽快的竖屏魔法旷野之旅来了!', 0.9761617183685303)], [[[1917.0, 1163.0], [2264.0, 1163.0], [2264.0, 1197.0], [1917.0, 1197.0]], ('认真的吗？院线电影用AI，就这种', 0.9912469387054443)], [[[1923.0, 1200.0], [1987.0, 1200.0], [1987.0, 1229.0], [1923.0, 1229.0]], ('质量？', 0.9417212605476379)], [[[1069.0, 1237.0], [1272.0, 1237.0], [1272.0, 1263.0], [1069.0, 1263.0]], ('回小钻风www·7-23', 0.9404781460762024)], [[[1496.0, 1237.0], [1696.0, 1237.0], [1696.0, 1266.0], [1496.0, 1266.0]], ('广告剑与远征：启程', 0.9994297027587891)], [[[1923.0, 1234.0], [2091.0, 1234.0], [2091.0, 1263.0], [1923.0, 1263.0]], ('四痕继痕迹·8-3', 0.9642047882080078)], [[[261.0, 1371.0], [520.0, 1371.0], [520.0, 1418.0], [261.0, 1418.0]], ('腾讯真是天才！', 0.9840106964111328)], [[[1615.0, 1362.0], [1774.0, 1369.0], [1772.0, 1424.0], [1613.0, 1418.0]], ('男女比例', 0.997657299041748)], [[[1088.0, 1374.0], [1336.0, 1374.0], [1336.0, 1421.0], [1088.0, 1421.0]], ('为什么米虫像是', 0.9964500069618225)], [[[1968.0, 1374.0], [2021.0, 1374.0], [2021.0, 1392.0], [1968.0, 1392.0]], ('赛事', 0.9992223978042603)], [[[853.0, 1389.0], [1000.0, 1389.0], [1000.0, 1468.0], [853.0, 1468.0]], ('陪睡', 0.9978748559951782)], [[[1087.0, 1413.0], [1323.0, 1422.0], [1321.0, 1469.0], [1085.0, 1460.0]], ('凭空长出来的？', 0.9920324087142944)], [[[291.0, 1429.0], [582.0, 1435.0], [581.0, 1490.0], [290.0, 1484.0]], ('在游戏饭圈化时代', 0.9956851005554199)], [[[1613.0, 1421.0], [1773.0, 1421.0], [1773.0, 1489.0], [1613.0, 1489.0]], ('1:40', 0.9596176147460938)], [[[781.0, 1474.0], [920.0, 1474.0], [920.0, 1529.0], [781.0, 1529.0]], ('损款', 0.6284663677215576)], [[[1547.0, 1497.0], [1840.0, 1497.0], [1840.0, 1532.0], [1547.0, 1532.0]], ('相亲市场有多略形？', 0.8000562191009521)], [[[999.0, 1541.0], [1121.0, 1548.0], [1119.0, 1585.0], [997.0, 1578.0]], ('Q搜索', 0.907643735408783)], [[[1565.0, 1550.0], [1592.0, 1550.0], [1592.0, 1579.0], [1565.0, 1579.0]], ('PC', 0.7175765037536621)], [[[2451.0, 1542.0], [2499.0, 1542.0], [2499.0, 1561.0], [2451.0, 1561.0]], ('17:13', 0.970749020576477)], [[[2240.0, 1553.0], [2272.0, 1553.0], [2272.0, 1574.0], [2240.0, 1574.0]], ('中', 0.9989645481109619)], [[[2408.0, 1561.0], [2501.0, 1561.0], [2501.0, 1587.0], [2408.0, 1587.0]], ('2024/8/10', 0.9983475208282471)]]

'''