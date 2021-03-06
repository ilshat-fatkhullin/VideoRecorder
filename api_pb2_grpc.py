# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2


class APIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCameras = channel.unary_unary(
                '/API/GetCameras',
                request_serializer=api__pb2.Void.SerializeToString,
                response_deserializer=api__pb2.GetCamerasResult.FromString,
                )
        self.SetCameraActiveness = channel.unary_unary(
                '/API/SetCameraActiveness',
                request_serializer=api__pb2.SetCameraActivenessRequest.SerializeToString,
                response_deserializer=api__pb2.ActionReport.FromString,
                )
        self.SubscribeOnCamera = channel.unary_stream(
                '/API/SubscribeOnCamera',
                request_serializer=api__pb2.SubscribeOnCameraRequest.SerializeToString,
                response_deserializer=api__pb2.VideoChunk.FromString,
                )
        self.GetRecords = channel.unary_unary(
                '/API/GetRecords',
                request_serializer=api__pb2.Void.SerializeToString,
                response_deserializer=api__pb2.GetRecordsResponse.FromString,
                )
        self.SubscribeOnRecord = channel.unary_stream(
                '/API/SubscribeOnRecord',
                request_serializer=api__pb2.SubscribeOnRecordRequest.SerializeToString,
                response_deserializer=api__pb2.VideoChunk.FromString,
                )
        self.RemoveRecord = channel.unary_unary(
                '/API/RemoveRecord',
                request_serializer=api__pb2.RemoveRecordRequest.SerializeToString,
                response_deserializer=api__pb2.ActionReport.FromString,
                )


class APIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCameras(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCameraActiveness(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeOnCamera(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeOnRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCameras': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCameras,
                    request_deserializer=api__pb2.Void.FromString,
                    response_serializer=api__pb2.GetCamerasResult.SerializeToString,
            ),
            'SetCameraActiveness': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCameraActiveness,
                    request_deserializer=api__pb2.SetCameraActivenessRequest.FromString,
                    response_serializer=api__pb2.ActionReport.SerializeToString,
            ),
            'SubscribeOnCamera': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeOnCamera,
                    request_deserializer=api__pb2.SubscribeOnCameraRequest.FromString,
                    response_serializer=api__pb2.VideoChunk.SerializeToString,
            ),
            'GetRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecords,
                    request_deserializer=api__pb2.Void.FromString,
                    response_serializer=api__pb2.GetRecordsResponse.SerializeToString,
            ),
            'SubscribeOnRecord': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeOnRecord,
                    request_deserializer=api__pb2.SubscribeOnRecordRequest.FromString,
                    response_serializer=api__pb2.VideoChunk.SerializeToString,
            ),
            'RemoveRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveRecord,
                    request_deserializer=api__pb2.RemoveRecordRequest.FromString,
                    response_serializer=api__pb2.ActionReport.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'API', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class API(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCameras(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/API/GetCameras',
            api__pb2.Void.SerializeToString,
            api__pb2.GetCamerasResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCameraActiveness(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/API/SetCameraActiveness',
            api__pb2.SetCameraActivenessRequest.SerializeToString,
            api__pb2.ActionReport.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeOnCamera(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/API/SubscribeOnCamera',
            api__pb2.SubscribeOnCameraRequest.SerializeToString,
            api__pb2.VideoChunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/API/GetRecords',
            api__pb2.Void.SerializeToString,
            api__pb2.GetRecordsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeOnRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/API/SubscribeOnRecord',
            api__pb2.SubscribeOnRecordRequest.SerializeToString,
            api__pb2.VideoChunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/API/RemoveRecord',
            api__pb2.RemoveRecordRequest.SerializeToString,
            api__pb2.ActionReport.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
