import grpc
import queue
import schema_pb2
import schema_pb2_grpc

queue = queue.Queue()

def main():
	# channel = grpc.insecure_channel('localhost:50051')
	# stub = schema_pb2_grpc.GatewayStub(channel)
	with grpc.insecure_channel("localhost:50051") as channel:
		stub = schema_pb2_grpc.GatewayStub(channel)
		queue.put(1)
		resp = stub.Call(generate_massage())
		for r in resp:
			num = r.num
			queue.put(num)

def generate_massage():
	while 1:
		num = queue.get()
		print(num)
		yield schema_pb2.Request(num=num)

if __name__ "__main__":
	main()