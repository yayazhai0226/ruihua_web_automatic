from base.basetools import BasePage


class Courtyard(BasePage):
    def select_(self, courtyardname=None, status="全部"):
        self.input_(('xpath', '//input[@id="courtyardName"]'), courtyardname)
        self.click_(('xpath', '//span[@class="ui-dropdown-trigger-icon ui-clickable pi pi-chevron-down"]'))
        if status == "全部":
            self.click_(('xpath', '//span[text()="全部"]'))
        elif status == "禁用":
            self.click_(('xpath', '//span[text()="禁用"]'))
        elif status == "启用":
            self.click_(('xpath', '//span[text()="启用"]'))
        else:
            print('输入的状态不存在')
        self.click_(('xpath', '//span[text()="查询列表"]'))

    def add_(self, name, abbrname, code, courtid='test_id', location=('四川省', '成都市', '锦江区'), highercourt="无", courtaddr="成都市天府新区", GNSS="test_gnss", note="test_note"):
        self.click_(('xpath', '//span[text()="新增"]'))  # 点击新增按钮
        self.input_(('xpath', '//input[@id="courtyardName"][contains(@formcontrolname,"courtyardName")]'), name)  # 名称
        self.input_(('xpath', '//input[@id="courtyardAliasName"]'), abbrname)  # 简称
        self.input_(('xpath', '//input[@id="courtyardCode"]'), code)  # code
        self.input_(('xpath', '//input[@id="hisCode"]'), courtid)  # id
        self.locate_s(('xpath', '//span[@class="ui-dropdown-trigger-icon ui-clickable pi pi-chevron-down"]'))[1].click()  # 位置信息_省
        self.click_(('xpath', '//span[text()=\"{a}\"]'.format(a=location[0])))  # 位置信息_省
        self.locate_s(('xpath', '//span[@class="ui-dropdown-trigger-icon ui-clickable pi pi-chevron-down"]'))[2].click()  # 位置信息_市
        self.click_(('xpath', '//span[text()=\"{a}\"]'.format(a=location[1])))  # 位置信息_市
        self.locate_s(('xpath', '//span[@class="ui-dropdown-trigger-icon ui-clickable pi pi-chevron-down"]'))[3].click()  # 位置信息_区
        self.click_(('xpath', '//span[text()=\"{a}\"]'.format(a=location[2])))  # 位置信息_区
        self.click_(('xpath', '//div[@class="tree-input"]'))  # 上级院区
        self.click_(('xpath', '//span[@class="ng-star-inserted"][contains(text(),\"{a}\")]'.format(a=highercourt)))  # 上级院区
        self.input_(('xpath', '//input[@id="address"]'), courtaddr)  # 院区地址
        self.input_(('xpath', '//input[@id="gnss"]'), GNSS)  # GNSS
        self.input_(('xpath', '//textarea[@id="description"]'), note)  # 备注
        self.click_(('xpath', '//span[text()="保存"]'))  # 保存
        self.click_(('xpath', '//span[@class="ui-button-text ui-clickable"][contains(text(),"确定")]'))  # 确定

    def downloaddemo_(self):
        self.click_(('xpath', '//span[text()="下载模板"]'))

    def leadingin_(self):
        pass

    def status_(self):
        self.click_(('xpath', '//td[contains(text(),\"{a}\")]/../td/p-inputswitch/div/span'.format(a="test_name")))

    def lookup_(self):
        self.click_(('xpath',
                     "// td[contains(text(), \"{a}\")] /../ td / a[contains(text(), \"{b}\")]".format(a="test_",
                                                                                                      b="查看")))
        self.click_(('xpath', '//span[text()="返回"]'))

    def update_(self):
        self.click_(('xpath',
                     "// td[contains(text(), \"{a}\")] /../ td / a[contains(text(), \"{b}\")]".format(a="test_",
                                                                                                      b="更新")))
        self.input_(('xpath', '//textarea[@id="description"]'), "通过update，写入备注")
        self.click_(('xpath', '//span[text()="保存"]'))
        self.click_(('xpath', '//span[text()="确定"]'))

    def delete_(self):
        self.click_(('xpath', "// td[contains(text(), \"{a}\")] /../ td / a[contains(text(), \"{b}\")]".format(a="test_", b="删除")))
        self.click_(('xpath', '//span[@class="ui-button-text ui-clickable"][contains(text(),"确定")]'))
        self.click_(('xpath', '//span[@class="ui-button-text ui-clickable"][contains(text(),"确定")]'))
