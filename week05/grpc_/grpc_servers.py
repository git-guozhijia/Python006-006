"""
pip install grpcio  # 该模块是启动grpc服务的项目依赖
pip install grpcio-tools  # gRPC tools 包含protocol buffer 编译器和用于从.proto 文件生成服务端和客户端代码的插件
pip install --upgrade protobuf   # 更新当前安装的protobuf，根据自身的python版本来看，可能会版本较低，编译.proto文件的时候会报错
"""

import grpc
import time
import schema_pb2
import schema_pb2_grpc
from concurrent import futures

# 注意点：
# 1，编写的服务端GatewayService类 ，需要继承schema_pb2_grpc.GatewayServicer类
# 2，编写一个和grpc一样的Call函数
# 3，设置一个参数去接收请求的参数request_iterator
# 4，接收进来的数据都有什么样的参数(req.num)，可以通过.的方式来获取参数
class GatewayService(schema_pb2_grpc.GatewayServicer):
    # 重写父类方法，返回消息（父类的Call方法，是通过编写schema.proto文件，执行命令编译出来的schema_pb2_grpc文件内的Call方法）
    # def Call(self, request_iterator, context):
    #     """Missing associated documentation comment in .proto file."""
    #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    #     context.set_details('Method not implemented!')
    #     raise NotImplementedError('Method not implemented!')

    # request_iterator参数：就是客户端请求Call方法的参数，是一个可迭代对象
    def Call(self, request_iterator, context):
        for req in request_iterator:
            # 返回num=req.num + 1， req.num就是获取request_iterator内包含的num
            yield schema_pb2.Response(num=req.num + 1)
            time.sleep(1)


def main():
    # 创建server线程池，最大是10个线程
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 将GatewayService()加入到server内
    schema_pb2_grpc.add_GatewayServicer_to_server(GatewayService(), server)
    # 添加端口
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop()


if __name__ == '__main__':
    main()
