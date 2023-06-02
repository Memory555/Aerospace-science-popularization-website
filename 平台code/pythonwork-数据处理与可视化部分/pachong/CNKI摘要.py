import os
import re
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import xlrd
from tqdm import tqdm

# 存放搜索的关键字
global search

# 判断是否为中文摘要
def Chinese(web):
    try:
        web.find_element_by_xpath('//*[@id="ChDivSummary"]')
        return True
    except:
        return False

# 判断是否存在下一页
def Next_page(web):
    try:
        web.find_element_by_xpath('//*[@id="PageNext"]')
        return True
    except:
        return False

# 判断是否为英文摘要
def English(web):
    try:
        web.find_element_by_xpath('//*[@id="doc-summary-content-text"]')
        return True
    except:
        return False

# 判断是否打开了子网页
def is_childpage(web):
    try:
        web.switch_to.window(web.window_handles[1])
        return True
    except:
        return False

# 爬取数据
def spider(web):
    # key_search = input('请输入索引关键字：')
    # 获取所有关键词，存放到medical_list中
    medical_list = get_data()
    # 已抓取过的关键词存放到列表have_search_list = []
    have_search_list = []
    # 用一个变量来标明第一次搜索和后面几次搜索
    count_mark = 0
    for key_search in medical_list:
        # 给全局变量赋值
        global search
        search= key_search
        # 如果已经抓取过，则跳过，进行下一个
        if key_search in have_search_list:
            continue
        else:
            have_search_list.append(key_search)
            # 每个关键词创建一个文件夹
            file_path = './Abstract/'+key_search
            if not os.path.exists(file_path):
                os.mkdir(file_path)

        if count_mark == 0:
            web.find_element_by_xpath('//*[@id="txt_SearchText"]').send_keys(key_search, Keys.ENTER)
            count_mark += 1
        else:
            web.find_element_by_xpath('//*[@id="txt_search"]').clear()
            web.find_element_by_xpath('//*[@id="txt_search"]').send_keys(key_search,Keys.ENTER)
        # input('筛选是否完成：')
        # 筛选年份
        time.sleep(3)
        Choose_year(web)
        time.sleep(8)
        # while循环实现翻页
        page_count = 0
        while True:
            try:
                time.sleep(2)
                # 获取论文列表
                page_count += 1
                tr_list = web.find_elements_by_xpath('//*[@id="gridTable"]/table/tbody/tr')
                print(f'{key_search} : 正在读取第{page_count}页!')
                for tr in tqdm(tr_list):
                    time.sleep(1)
                    # 点击论文链接
                    tr.find_element_by_xpath('./td[@class="name"]/a').click()
                    # 切换到新窗口
                    if is_childpage(web) == True:
                        web.switch_to.window(web.window_handles[1])
                    else:
                        print('*'*100)
                        print('未打开新窗口')
                        time.sleep(50)
                        continue
                    time.sleep(4)
                    # 中文期刊
                    if Chinese(web) == True:
                        # 抓取标题
                        title = web.find_element_by_xpath('/html/body/div[@class="wrapper"]/div[@class="main"]/div[@class="container"]/div[@class="doc"]/div[@class="doc-top"]/div[@class="brief"]/div[@class="wx-tit"]/h1').text
                        # 抓取摘要
                        abstract = web.find_element_by_xpath('//*[@id="ChDivSummary"]').text
                    # 英文期刊
                    elif English(web) == True:
                        # 抓取标题
                        title = web.find_element_by_xpath('//*[@id="doc-title"]').text
                        # 抓取摘要
                        abstract = web.find_element_by_xpath('//*[@id="doc-summary-content-text"]').text
                    else:
                        title = "标题不存在！"
                        abstract = '摘要不存在！'

                    # 如果标题中存在/则用汉字替换
                    r = r"[.!+-=——,$%^，,。？?、~@#￥%……&*《》<>「」{}【】()/\\\[\]'\"]"
                    title_copy = re.sub(r, ' ', title)
                    # title_copy = re.sub(r'/','斜杠',title)


                    # 写入摘要
                    try:
                        with open(file_path + '/{0}.txt'.format(title_copy), 'w',encoding='utf-8') as f:
                            f.write(title)
                            f.write('\n')
                            f.write(abstract)
                        if is_childpage(web) == True:
                            # 关闭子网页
                            web.close()
                            # 切换到原网页
                            web.switch_to.window(web.window_handles[0])
                        else:
                            web.switch_to.window(web.window_handles[0])
                    except:
                        print('文件名称Invalid !')
                        if is_childpage(web) == True:
                            # 关闭子网页
                            web.close()
                            # 切换到原网页
                            web.switch_to.window(web.window_handles[0])
                        else:
                            web.switch_to.window(web.window_handles[0])
                if Next_page(web) == True:
                    # web.find_element_by_xpath('//*[@id="PageNext"]').click()
                    web.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
                else:
                    break
                time.sleep(3)
            except:
                print('定位失败！当前在第{}页！'.format(page_count))
                # 跳回第一个页面
                if is_childpage(web) == True:
                    web.switch_to.window(web.window_handles[1])
                    web.close()
                    web.switch_to.window(web.window_handles[0])
                else:
                    web.switch_to.window(web.window_handles[0])
                # 点击下一页
                if Next_page(web) == True:
                    # web.find_element_by_xpath('//*[@id="PageNext"]').click()
                    web.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
                    time.sleep(5)
                else:
                    break
        print('关键词：',key_search,'Successful!')

# 筛选中文、年份
def Choose_year(web):
    count = 0
    while True:
        try:
            time.sleep(10)
            # 点击中文
            web.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div/a[1]').click()
            time.sleep(8)
            web.find_element_by_xpath('//*[@id="divGroup"]/dl[3]/dt/i[1]').click()
            time.sleep(8)
            web.find_element_by_xpath('//*[@id="divGroup"]/dl[3]/dt/i[2]').click()
            time.sleep(8)
            web.find_element_by_xpath('//*[@id="txtStartYear"]').send_keys(2011)
            time.sleep(3)
            web.find_element_by_xpath('//*[@id="txtEndYear"]').send_keys(2021)
            time.sleep(3)
            web.find_element_by_xpath('//*[@id="btnFilterYear"]').click()
            break
        except:
            web.refresh()
            # 重新输入
            web.find_element_by_xpath('//*[@id="txt_search"]').clear()
            time.sleep(2)
            web.find_element_by_xpath('//*[@id="txt_search"]').send_keys(search, Keys.ENTER)
            count += 1
            if count > 15:
                time.sleep(120)
            if count > 21:
                break


# 从本地csv文件中读取关键词
def get_data():
    # 创建一个列表存放关键词
    medical = []
    # 打开文件
    # work_book = xlrd.open_workbook('./data.xls')
    # # 打开表
    # sheet = work_book.sheet_by_name('Sheet')
    # # 读取excel
    # for i in range(sheet.nrows):
    #     cell = sheet.row_values(i)
    #     medical.append(cell[3])

    data = pd.read_csv('./data.csv',encoding='ANSI')
    medical = list(data['关键词'])
    print(medical)
    print('关键词读取完成！')
    return medical


if __name__ == '__main__':
    if not os.path.exists('./Abstract'):
        os.mkdir('./Abstract')

    opt = Options()
    opt.add_experimental_option('excludeSwitches',['enable-automation'])
    opt.add_argument('--headless')
    opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
    url = 'https://www.cnki.net/?pageId=77825&wfwfid=145305&websiteId=58201'
    web = Chrome(options=opt)
    web.get(url)
    # while True:
    spider(web)
        # choice = input('是否搜索下一个关键字（是/否）：')
        # if choice == '否':
        #     break