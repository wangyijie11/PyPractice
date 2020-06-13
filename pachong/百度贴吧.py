import urllib.request
import urllib.error
import re
import ssl


class Tool:
    """处理页面标签类

    Attributes:


    """
    # 去除img标签,7位长空格
    remove_img = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    remove_addr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replace_line = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replace_td = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replace_para = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replace_br = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    remove_extratag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.remove_img, "", x)
        x = re.sub(self.remove_addr, "", x)
        x = re.sub(self.replace_line, "\n", x)
        x = re.sub(self.replace_td, "\t", x)
        x = re.sub(self.replace_para, "\n", x)
        x = re.sub(self.replace_br, "\n", x)
        x = re.sub(self.remove_extratag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class Bdtb:
    """百度贴吧爬虫类

    Attributes:
        baseurl: 帖子地址
        seelz: 是否只看楼主
        tool: html标签提出工具类对象
        file: 全局file变量，文件写入操作对象
        floor: 楼层标号，初始为1
        defaulttitle: 默认标题，如果没有获取到标题则用此默认值
        floortag: 是否写入楼层分割符

    """
    def __init__(self, baseurl, seelz, floortag):
        self.baseurl = baseurl
        self.seeelz = '?see_lz=' + str(seelz)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaulttitle = u"百度贴吧"
        self.floortag = floortag

    # 传入页码，获取该页帖子
    def get_page(self, pagenum):
        try:
            context = ssl._create_unverified_context()
            url = self.baseurl + self.seeelz + '&pn=' + str(pagenum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request, context=context)
            # print(response.read().decode())
            return response.read().decode()

        except urllib.error.URLError as ex:
            print(ex)

    # 获取帖子标题
    def get_title(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            # print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def get_pagenum(self, page):
        pattern = re.compile('<li class="l_reply_num".*?>.*?<span.*?>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            # print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容，传入页面内容
    def get_content(self, page):
        pattern = re.compile('<div id="post_content.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode())
        return contents

    # 文件命名
    def set_file_title(self, title):
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaulttitle + ".txt", "w+")

    # 数据写入文件
    def set_file_data(self, contents):
        for item in contents:
            if self.floortag == '1':
                floorline = "\n" + str(self.floor) + u"----------------------------------------->>\n"
                self.file.write(floorline)
            self.file.write(item.decode())
            self.floor += 1

    # 启动
    def start(self):
        indexpage = self.get_page(1)
        pagenum = self.get_pagenum(indexpage)
        title = self.get_title(indexpage)
        self.set_file_title(title)
        if pagenum == None:
            print("url已失效，请重试")
            return
        try:
            print("该帖子共有" + str(pagenum) + "页")
            for i in range(1, int(pagenum)+1):
                print("正在写入第" + str(i) + "页数据")

                page = self.get_page(i)
                contents = self.get_content(page)
                self.set_file_data(contents)
        except IOError as ex:
            print("文件写入失败，原因" + ex.strerror)
        finally:
            print("文件写入完成")



baseurl = "http://tieba.baidu.com/p/3138733512"
seelz = 1
floortag = "1"
bdtb = Bdtb(baseurl, seelz, floortag)
bdtb.start()
