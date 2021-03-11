import yaml

#文件的读取
class YamlTools(object):
    #文件的读取
    def yaml_read(self, file_path):
        """
        :param file_path: 文件地址
        :return: 返回值文件值
        """
        f = open(file_path, 'r', encoding='utf-8')
        x = yaml.load(f, yaml.FullLoader)
        f.close()
        return x
    #文件的追加写入
    def yaml_a_write(self, file_path, data):
        """
        :param file_path: 文件地址
        :param data: 数据——dict格式
        :return: 无
        """
        f = open(file_path, 'a', encoding='utf-8')
        yaml.dump(data, f, allow_unicode = True)
        f.close()
    #文件的覆盖写入
    def yaml_w_write(self, file_path, data):
        """
        :param file_path: 文件地址
        :param data: 数据——dict格式
        :return: 无
        """
        f = open(file_path, 'w', encoding='utf-8')
        yaml.dump(data, f, allow_unicode = True)
        f.close()
    #文件的更新
    def yaml_update(self, file_path, data):
        """
        :param file_path: 文件地址
        :param data: 数据——dict格式
        :return: 无
        """
        x = self.yaml_read(file_path)
        x.update(data)
        self.yaml_a_write(file_path, x)


if __name__ == "__main__":
    ytool = YamlTools()
    res = ytool.yaml_read('../data/page_url.yaml')
    print(res)
    print(type(res))