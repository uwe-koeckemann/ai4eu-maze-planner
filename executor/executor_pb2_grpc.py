# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import executor_pb2 as executor__pb2


class AiddlExecutorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.assembleProblem = channel.unary_unary(
                '/AiddlExecutor/assembleProblem',
                request_serializer=executor__pb2.Goal.SerializeToString,
                response_deserializer=executor__pb2.Problem.FromString,
                )
        self.doNextAction = channel.unary_unary(
                '/AiddlExecutor/doNextAction',
                request_serializer=executor__pb2.Empty.SerializeToString,
                response_deserializer=executor__pb2.Action.FromString,
                )
        self.processPlanningResult = channel.unary_unary(
                '/AiddlExecutor/processPlanningResult',
                request_serializer=executor__pb2.Solution.SerializeToString,
                response_deserializer=executor__pb2.Result.FromString,
                )
        self.processActionResult = channel.unary_unary(
                '/AiddlExecutor/processActionResult',
                request_serializer=executor__pb2.Result.SerializeToString,
                response_deserializer=executor__pb2.Empty.FromString,
                )
        self.processState = channel.unary_unary(
                '/AiddlExecutor/processState',
                request_serializer=executor__pb2.State.SerializeToString,
                response_deserializer=executor__pb2.Empty.FromString,
                )


class AiddlExecutorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def assembleProblem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doNextAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def processPlanningResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def processActionResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def processState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AiddlExecutorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'assembleProblem': grpc.unary_unary_rpc_method_handler(
                    servicer.assembleProblem,
                    request_deserializer=executor__pb2.Goal.FromString,
                    response_serializer=executor__pb2.Problem.SerializeToString,
            ),
            'doNextAction': grpc.unary_unary_rpc_method_handler(
                    servicer.doNextAction,
                    request_deserializer=executor__pb2.Empty.FromString,
                    response_serializer=executor__pb2.Action.SerializeToString,
            ),
            'processPlanningResult': grpc.unary_unary_rpc_method_handler(
                    servicer.processPlanningResult,
                    request_deserializer=executor__pb2.Solution.FromString,
                    response_serializer=executor__pb2.Result.SerializeToString,
            ),
            'processActionResult': grpc.unary_unary_rpc_method_handler(
                    servicer.processActionResult,
                    request_deserializer=executor__pb2.Result.FromString,
                    response_serializer=executor__pb2.Empty.SerializeToString,
            ),
            'processState': grpc.unary_unary_rpc_method_handler(
                    servicer.processState,
                    request_deserializer=executor__pb2.State.FromString,
                    response_serializer=executor__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AiddlExecutor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AiddlExecutor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def assembleProblem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlExecutor/assembleProblem',
            executor__pb2.Goal.SerializeToString,
            executor__pb2.Problem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doNextAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlExecutor/doNextAction',
            executor__pb2.Empty.SerializeToString,
            executor__pb2.Action.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def processPlanningResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlExecutor/processPlanningResult',
            executor__pb2.Solution.SerializeToString,
            executor__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def processActionResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlExecutor/processActionResult',
            executor__pb2.Result.SerializeToString,
            executor__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def processState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlExecutor/processState',
            executor__pb2.State.SerializeToString,
            executor__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
