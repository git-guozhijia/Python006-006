from pathlib import Path

# # p = Path('/hidog/text.tar.gz')
# p = Path(__file__).resolve()
# '''
# name 目录的最后一个部分
# suffix 目录中最后一个部分的扩展名
# suffixes 返回多个扩展名列表
# stem 目录最后一个部分，没有后缀
# with_name(name) 替换目录最后一个部分并返回一个新的路径
# with_suffix(suffix) 替换扩展名，返回新的路径，扩展名存在则不变
# '''
# print(f"p.name:{p.name}")
# print(p.suffix)
# print(p.suffixes)
# print(p.stem)
# print(p.with_name('haha.tgz'))
# print(p.with_suffix('.gz'))
# print(p.with_suffix('.gzzz'))
# print(p.cwd())#返回一个表示当前目录的新路径对象
# print(p.home())#返回一个表示当前用户HOME目录的新路径对象
#
# '''
# is_dir() 是否是目录
# is_file() 是否是普通文件
# is_symlink() 是否是软链接
# is_socket() 是否是socket文件
# is_block_device() 是否是块设备
# is_char_device() 是否是字符设备
# is_absolute() 是否是绝对路径
# '''
#
# print(p.resolve())#返回一个新的路径，这个新路径就是当前Path对象的绝对路径，如果是软链接则直接被解析
# print(p.absolute())#也可以获取绝对路径，但是推荐resolve()
#
# print(Path('/c').exists())
# print(Path(p.resolve()).exists())#该路径是否指向现有的目录或文件


with open(Path(__file__).resolve(), 'rb') as f:
    while 1:
        data = f.read(10)
        if not data:
            break
        print(f"data.decode('utf-8') >>> {data}")

# import os
# fp = open(Path(__file__).resolve(), 'rb')
# while 1:
#     data = fp.read(1024)
#     if not data:
#         print('{0} file send over...'.format(os.path.basename(Path(__file__).resolve())))
#         break
#     print(data,'\n')