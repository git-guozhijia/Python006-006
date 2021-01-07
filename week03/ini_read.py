import configparser,pathlib
from week01 import logging_t

class read_ini_config():
    def __init__(self):
        self.log = logging_t.log().mylog()
        self.path = str(pathlib.Path(__file__).parent.resolve())
        self.file = f"{self.path}/config_file/config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.file)

    def config_add_section(self, section_name):
        if self.config.has_section(section_name):
            self.log.error(f"添加的section“{section_name}”在文件内已存在")
        else:
            try:
                self.config.add_section(section_name)
            except Exception as err:
                self.log.error(f"add_section func err:{err}")

    def set_section_value(self, section_name, option, value):
        if self.config.has_section(section_name):
            try:
                self.config.set(section_name, option, value)
                with open(self.file, 'w') as configfile:
                    self.config.write(configfile)
            except Exception as err:
                self.log.error(f"set_section_value func err:{err}")
        else:
            self.log.debug(f'当前的section:"{section_name}"不存在')

    def read_config_dict(self, section_name):
        if self.config.has_section(section_name):
            items = self.config.items(section_name)
            return dict(items)
        else:
            self.log.debug('{} not found in {} file'.format(section_name, self.file))

    def get_option_value(self, section_name, option):
        if self.config.has_section(section_name):
            if self.config.has_option(section_name, option):
                option_value = self.config.get(section_name, option)
                return option_value
            else:
                self.log.debug(f'{option} not found in {section_name} section')
        else:
            self.log.debug(f'{section_name} not found in {self.file} file')

if __name__ == '__main__':
    read_ini = read_ini_config()
    print(read_ini.read_config_dict('login'))
    print(read_ini.get_option_value('login', 'username'))
    # read_ini.config_add_section('login')
    # read_ini.set_section_value('login', 'guozhijia', 'niininin')