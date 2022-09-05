# -*- coding: utf-8 -*-
from toExcel import createtrExcel



i=[ [1,1,1,1],  ['芙蓉巷石锅川菜（百脑汇店）', '天河区天河路岗顶百脑汇A座6楼（地铁岗顶站C1出口直上6楼）', '020-29873568', 'https://img.meituan.net/msmerchant/1eecfcf9d683493318adaedfd3edb330297819.jpg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/4b329946170df53d920f4f5e89c1c8684237984.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/8064b7c25a0dc6661e42757d7ff2e55769961.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/c20bae549b8f0e919a4b19b1ebe5ea8b95062.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/a8df4b0b1dd4bed4b48ae8b4d2748f1f116437.jpg@92w_50h_1e_1c'],
   ['元握寿司（石基店）', '番禺区石基镇岐山南路商业街49号', '18820771184', 'https://p1.meituan.net/mogu/fb8c5a59e5813bafc9c2f1b5ea1112d762407.jpg@380w_214h_1e_1c', 'https://p0.meituan.net/deal/d5cc8b21eedab3d8fa6012751e477d0e445902.jpg@92w_50h_1e_1c', 'https://p0.meituan.net/deal/f8fbcfff72b4667cbf8ba6f1eac77ffa510828.jpg@92w_50h_1e_1c', 'https://p0.meituan.net/shaitu/7692e20dac43ad378cc5a974edfd5bee91694.jpg@92w_50h_1e_1c', 'https://p1.meituan.net/shaitu/67d55d608d8b14b6037bb26107cc195499180.jpg@92w_50h_1e_1c'],
   ['吾虎将·现炒快餐（番禺店）', '番禺区番禺大道北节能科技园科技发展大厦一层103单元', '020-39122969/13682215285', 'https://p0.meituan.net/bbia/9a2c052f14c1284ec2f9caa3f941c5381482655.jpg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/380ee5023ff5bf5d12cc096422c0d81d659293.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/9a2c052f14c1284ec2f9caa3f941c5381482655.jpg@92w_50h_1e_1c', 'https://p0.meituan.net/poiskudish/fb040a5250a21537ad4b643d6c75273e1529195.png@92w_50h_1e_1c', 'https://p0.meituan.net/poiskudish/51460236a2a5f4a6d0afb1d67efe8bda1516976.png@92w_50h_1e_1c'],
   ['蜜雪冰城（华师店）', '天河区五山路122号106', '17620132205', 'https://p1.meituan.net/biztone/2e5610e337d0a30c2ecf9cf00aa0f266162461.jpg@380w_214h_1e_1c', 'https://p1.meituan.net/deal/c723986faed6706580cc5298b97f1c0874207.jpg@92w_50h_1e_1c', 'https://p1.meituan.net/poiskudish/593f6d4a99399c411e297395163b51571778374.png@92w_50h_1e_1c'],
   ['兰桂坊（沙面分店）', '荔湾区沙面南街自编7号（翠州园内）', '020-81217012/020-81217063', 'https://p0.meituan.net/biztone/627424_1625329208903.jpeg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/7507a7ebe622bd38d9e72cdcc29bc74b1300888.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/1d560824324fe8055600d0f7defad3dc1970089.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/fa19f8d048ffc6cc37438662ab02d1c51348165.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/f9bb75b6f7f966f1246939693671739f1195852.jpg@92w_50h_1e_1c'],
   ['韩香阁', '番禺区荔新大道6号', '13144428808', 'https://img.meituan.net/searchscenerec/a80cd16e29c1b49bf419716fd1d81d0f144865.jpg@380w_214h_1e_1c', 'https://p1.meituan.net/deal/349f6d79bd8e0617fd0dce00b76e6dea389273.jpg@92w_50h_1e_1c', 'https://p1.meituan.net/deal/dcf4d728a7ee0e83132816472b6f8cc0935809.jpg@92w_50h_1e_1c', 'https://p0.meituan.net/deal/18aeaf26388e2e018a2f1c0e9032c3a8398883.jpg@92w_50h_1e_1c', 'https://p1.meituan.net/shaitu/4854a7d4b0ab27584e659cb678f88b92152834.jpg@92w_50h_1e_1c'],
   ['大鸽饭（棠下旗舰店）', '天河区棠下涌西路69号天辉大厦1楼', '020-85205090/020-85554651', 'https://img.meituan.net/msmerchant/75ab206bf3024455d26a0e5732f994ba594907.jpg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/fc6e0da3e625eac064e804d6ebbdfd0a802331.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/69b4a503b9784979a1795aac573d049386400.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/6fd99e732c6d77aacbc87d084dc291da81339.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/e9eb2f692c0578054834b61782e97e4396270.jpg@92w_50h_1e_1c'],
   ['韩舍·雪花冰&炸鸡', '花都区龙珠路33号17商铺', '15915938580', 'https://p0.meituan.net/bbia/5c9510d3ab52a0aa78c42c6d6f1d0d248377716.jpg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/091893f998ef89f8db7ac3284bfb0f69911574.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/818bfd9ab88506b42f0ff3472621cfc9757624.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/49a6fa4d4c2bc994d83dde693759d0ad808423.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/016e8bf920990e4259f66573c0a39dc4743384.jpg@92w_50h_1e_1c'],
   ['呼伦贝尔烤羊（南田店）1', '海珠区南田路葵苑酒家旁', '13826270670/15113891222', 'https://p1.meituan.net/biztone/4295474_1621565181978.jpeg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/4ca522b6e7a5869c282466c3b76c67f63676122.png@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/fd5bb520618471babfd35dcf57604772217676.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/5db76624b3e07c6756ee20be380877001459513.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/cc37cc2f7701e544868b1ff36ecef3bb4669085.png@92w_50h_1e_1c']]

k=[['重庆德庄火锅（新塘大润发店）', '增城市港口大道332号金海岸城市广场4层', '020-32178399', 'https://p1.meituan.net/biztone/1331225832_1621912937044.jpeg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/a2816f2b997d09ce6981a414a16fcecd3929783.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/1a80ed6e65109938627c668aa8b736362377101.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/f7a9879939492992fd07f861747216cc3536816.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/7fb34dd73726491a9597e8f4c5c043ca4153116.jpg@92w_50h_1e_1c'],
   ['醉英雄（国贸店）', '增城市新塘镇东坑三横中路汇创国贸大厦3栋1楼工商银行对面（锦上花、安提、工商银行对面）', '020-26229958', 'https://p0.meituan.net/bbia/328cdf1b62586bde9d566e4f5c549e51116927.jpg@380w_214h_1e_1c', 'https://p0.meituan.net/deal/a31482f47bb069b621fadac0b31c3d12355867.jpg@92w_50h_1e_1c', 'https://p1.meituan.net/deal/84a587d9ab05ef4013ff4197b0cc8a9c604853.jpg@92w_50h_1e_1c', 'https://p1.meituan.net/deal/706e3908910c7b275259e7fbfda4f6c3342646.jpg@92w_50h_1e_1c', 'https://p0.meituan.net/poi/a783df2aeff0c0b8390b23237efc6c54190464.jpg@92w_50h_1e_1c'],
   ['洞庭土鸡馆（奥园广场店）', '番禺区福德路281号奥园广场4层', '020-83563288', 'https://p1.meituan.net/biztone/4365759_1620357182184.jpeg@380w_214h_1e_1c', 'https://img.meituan.net/msmerchant/c83e5af049f6fae8167fb00cc95f0c9d513608.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/144bf8079a0c1a23165f40aceb281286379491.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/e3eb6c9b0cea595c54a45ca263edb058389978.jpg@92w_50h_1e_1c', 'https://img.meituan.net/msmerchant/5420fc45f79f1a1e2d5196c623f593072685831.jpg@92w_50h_1e_1c']]


c=createtrExcel('广州美食','美食',k)
# c.createrWookbook()
# c.addSheet()
c.pandas_insert()
# a=['aa','aaa','aaaa']
# b=['bb','bbb','bbbb']
# print(a+b)

#
# import pandas as pd
# import openpyxl
# # df1 = pd.DataFrame(i)
# # df2 = df1.copy()
# # with pd.ExcelWriter('./美团.xlsx') as writer:
# #    df1.to_excel(writer, sheet_name='美食')
# #    writer.save()
# #    writer.close()
# wb = openpyxl.load_workbook('./美团.xlsx')
# #如果有多个模块可以读写excel文件，这里要指定engine，否则可能会报错
# writer = pd.ExcelWriter('./美团.xlsx',engine='openpyxl')
# #没有下面这个语句的话excel表将完全被覆盖
# writer.book = wb
#
# df = pd.DataFrame(pd.read_excel('美团.xlsx',sheet_name = '美食'))
# #如果有相同名字的工作表，新添加的将命名为Sheet21，如果Sheet21也有了就命名为Sheet22，不会覆盖原来的工作表
# df.to_excel(writer,sheet_name = '美食')
# writer.save()
# writer.close()







# workbook=xlwt.Workbook(encoding='utf-8')
# booksheet=workbook.add_sheet('美食', cell_overwrite_ok=True)
# for
# # oldWb = xlrd.open_workbook("./考勤系统.xlsx")
# # newWb = copy(oldWb)
# # newWs = newWb.get_sheet(2)
# # newWs.write(2, 4, "pass")
# # newWb.save("./考勤系统.xls")

