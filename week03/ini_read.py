import configparser,pathlib

path = str(pathlib.Path(__file__).parent.resolve())
file = f"{path}/config_file/config.ini"

'''
# config = configparser.ConfigParser()
# file = "config.ini"
# config.read(file)
# # 向ini配置文件内添加section，并设置section的键值对
# config.add_section('login')
# config.set('login', 'username', '1111')
# config.set('login', 'password', '2222')
# with open(file, 'w') as configfile:
#     config.write(configfile)

config = configparser.ConfigParser()
config.read(file)
username = config.get('login', 'username')
password = config.get('login', 'password')
print(username, password)
'''

def read_db_config(file_path, section):
    parser = configparser.ConfigParser()
    parser.read(file_path)
    if parser.has_section(section):
        items = parser.items(section)
        print(items)
    else:
        raise Exception('{} not found in {} file'.format(section, file_path))
    return dict(items)

if __name__ == '__main__':
    print(read_db_config(file, "mysql"))