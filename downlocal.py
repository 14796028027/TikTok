import you_get
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import xlsxwriter as xw
# os.system("you-get https://v26-web.douyinvod.com/058dad814658a03318bcfa8420c6cc2c/64587bc9/video/tos/cn/tos-cn-ve-15c001-alinc2/ocpPnbRaADDDI1b3qgkgeBweQM9mADWIhA1UB6/?a=6383&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1005&bt=1005&cs=2&ds=3&ft=GN7rKGVVywSyRKJ80mo~ySqTeaApVxkP6vrK5c14mto0g3&mime_type=video_mp4&qs=15&rc=NTQ0Mzg0ZjZnODVkMzozNEBpM3U1cDs6ZnA5ajMzNGkzM0A2YV5hYV5fNTMxMy0xMC0yYSNmai1ucjRnaHNgLS1kLTBzcw%3D%3D&l=20230508113256F6837DA05371F867701E&btag=e00028000")


def drivers(url):
    driver = Chrome()
    driver.get(url)
    time.sleep(5)
    return  driver

# 写入excel
def xw_toExcel(fileName,dataDict):  # xlsxwriter库储存数据到excel
    fileName = f"{fileName}.xlsx"  # 工作簿名字
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    col = ord('A')  # 定义要开始的列

    # names 为一个姓名列表：["李四", "张三"]
    # age 为一个年龄列表:[18, 19]
    datalist = list(dataDict.keys())
    for i in range(len(dataDict.keys())):
        worksheet1.write_column(chr(col + i) + "2",dataDict[datalist[i]] )

    workbook.close()



# 加载次数
def pages(number):
    nums = 0
    while nums < number :
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        nums += 1
        time.sleep(5)

# 爬虫
def pares(driver):
    dataDict = {}
    name_users = []
    contents = []
    dianzans = []
    comments = []
    transmits = []
    times = []
    name_user = driver.find_elements(by=By.XPATH,
                                     value='//*[@id="douyin-right-container"]//li/div/div/div[1]/div/div/div[1]/a/p/span/span/span/span/span/span')
    content = driver.find_elements(by=By.XPATH,
                                   value='//*[@id="douyin-right-container"]//li/div/div/div[2]/div/span/span/span[1]/span/span/span')
    dianzan = driver.find_elements(by=By.XPATH,
                                   value='//*[@id="douyin-right-container"]/div[2]/div/div[2]/div[1]/ul/li/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]')
    comment = driver.find_elements(by=By.XPATH,
                                   value='//*[@id="douyin-right-container"]/div/div/div/div/ul/li/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]')
    transmit = driver.find_elements(by=By.XPATH,
                                    value='//*[@id="douyin-right-container"]/div/div/div/div/ul/li/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]')

    time = driver.find_elements(by=By.XPATH,
                                    value='//*[@id="douyin-right-container"]/div/div/div/div/ul/li/div/div/div[1]/div/div/div[1]/p')

    for item in name_user:
        name_users.append(item.text)
    dataDict["博主"] = name_users
    for item in time:
        times.append(item.text)
    dataDict["时间"] = times
    for item in content:
        contents.append(item.text)
    dataDict["内容"] = contents
    for item in dianzan:
        dianzans.append(item.text)
    dataDict["点赞"] = dianzans
    for item in comment:
        comments.append(item.text)
    dataDict["评论"] = comments
    for item in transmit:
        transmits.append(item.text)
    dataDict["转发"] = transmits

    return dataDict





if __name__ == "__main__":

    url = "https://www.douyin.com/search/%E6%B2%99%E6%9F%9A%E5%AD%90?source=search_history&aid=1d57d4f2-3865-4427-a60c-f40cc7131b65&enter_from=recommend&focus_method=&gid=7216717874029727035"
    urls = 'https://www.douyin.com/search/%E6%9F%9A%E5%AD%90?aid=17ab787d-da72-4546-9c41-1259185196c2&publish_time=0&sort_type=0&source=normal_search&type=general'
    urlss= 'https://www.douyin.com/search/%E6%9F%9A%E5%AD%90?publish_time=182&sort_type=0&source=tab_search&type=general'
    driver = drivers(urlss)
    pages(5)
    dataDict = pares(driver)
    xw_toExcel("沙田柚",dataDict)