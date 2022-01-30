import asyncio
import logging

import grpc
import api_pb2_grpc
import api_servicer
import cameras


async def serve() -> None:
    server = grpc.aio.server()
    cameras_list = cameras.Cameras()
    api_pb2_grpc.add_APIServicer_to_server(api_servicer.APIServicer(cameras_list=cameras_list), server)
    listen_address = "[::]:50051"
    server.add_insecure_port(listen_address)
    logging.info("Starting server on %s", listen_address)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
