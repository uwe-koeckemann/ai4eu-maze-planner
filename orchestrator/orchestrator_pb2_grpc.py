# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import orchestrator_pb2 as orchestrator__pb2


class AiddlExecutorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.assembleProblem = channel.unary_unary(
                '/AiddlExecutor/assembleProblem',
                request_serializer=orchestrator__pb2.Goal.SerializeToString,
                response_deserializer=orchestrator__pb2.Problem.FromString,
                )
        self.doNextAction = channel.unary_unary(
                '/AiddlExecutor/doNextAction',
                request_serializer=orchestrator__pb2.Empty.SerializeToString,
                response_deserializer=orchestrator__pb2.Action.FromString,
                )
        self.processPlanningResult = channel.unary_unary(
                '/AiddlExecutor/processPlanningResult',
                request_serializer=orchestrator__pb2.Solution.SerializeToString,
                response_deserializer=orchestrator__pb2.Result.FromString,
                )
        self.processActionResult = channel.unary_unary(
                '/AiddlExecutor/processActionResult',
                request_serializer=orchestrator__pb2.Result.SerializeToString,
                response_deserializer=orchestrator__pb2.Empty.FromString,
                )
        self.processState = channel.unary_unary(
                '/AiddlExecutor/processState',
                request_serializer=orchestrator__pb2.State.SerializeToString,
                response_deserializer=orchestrator__pb2.Empty.FromString,
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
                    request_deserializer=orchestrator__pb2.Goal.FromString,
                    response_serializer=orchestrator__pb2.Problem.SerializeToString,
            ),
            'doNextAction': grpc.unary_unary_rpc_method_handler(
                    servicer.doNextAction,
                    request_deserializer=orchestrator__pb2.Empty.FromString,
                    response_serializer=orchestrator__pb2.Action.SerializeToString,
            ),
            'processPlanningResult': grpc.unary_unary_rpc_method_handler(
                    servicer.processPlanningResult,
                    request_deserializer=orchestrator__pb2.Solution.FromString,
                    response_serializer=orchestrator__pb2.Result.SerializeToString,
            ),
            'processActionResult': grpc.unary_unary_rpc_method_handler(
                    servicer.processActionResult,
                    request_deserializer=orchestrator__pb2.Result.FromString,
                    response_serializer=orchestrator__pb2.Empty.SerializeToString,
            ),
            'processState': grpc.unary_unary_rpc_method_handler(
                    servicer.processState,
                    request_deserializer=orchestrator__pb2.State.FromString,
                    response_serializer=orchestrator__pb2.Empty.SerializeToString,
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
            orchestrator__pb2.Goal.SerializeToString,
            orchestrator__pb2.Problem.FromString,
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
            orchestrator__pb2.Empty.SerializeToString,
            orchestrator__pb2.Action.FromString,
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
            orchestrator__pb2.Solution.SerializeToString,
            orchestrator__pb2.Result.FromString,
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
            orchestrator__pb2.Result.SerializeToString,
            orchestrator__pb2.Empty.FromString,
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
            orchestrator__pb2.State.SerializeToString,
            orchestrator__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MazeGUIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.requestTask = channel.unary_unary(
                '/MazeGUI/requestTask',
                request_serializer=orchestrator__pb2.Empty.SerializeToString,
                response_deserializer=orchestrator__pb2.Goal.FromString,
                )
        self.processTaskResult = channel.unary_unary(
                '/MazeGUI/processTaskResult',
                request_serializer=orchestrator__pb2.Result.SerializeToString,
                response_deserializer=orchestrator__pb2.Empty.FromString,
                )
        self.getState = channel.unary_unary(
                '/MazeGUI/getState',
                request_serializer=orchestrator__pb2.Empty.SerializeToString,
                response_deserializer=orchestrator__pb2.State.FromString,
                )
        self.visualizeState = channel.unary_unary(
                '/MazeGUI/visualizeState',
                request_serializer=orchestrator__pb2.State.SerializeToString,
                response_deserializer=orchestrator__pb2.Empty.FromString,
                )


class MazeGUIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def requestTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def processTaskResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def visualizeState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MazeGUIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'requestTask': grpc.unary_unary_rpc_method_handler(
                    servicer.requestTask,
                    request_deserializer=orchestrator__pb2.Empty.FromString,
                    response_serializer=orchestrator__pb2.Goal.SerializeToString,
            ),
            'processTaskResult': grpc.unary_unary_rpc_method_handler(
                    servicer.processTaskResult,
                    request_deserializer=orchestrator__pb2.Result.FromString,
                    response_serializer=orchestrator__pb2.Empty.SerializeToString,
            ),
            'getState': grpc.unary_unary_rpc_method_handler(
                    servicer.getState,
                    request_deserializer=orchestrator__pb2.Empty.FromString,
                    response_serializer=orchestrator__pb2.State.SerializeToString,
            ),
            'visualizeState': grpc.unary_unary_rpc_method_handler(
                    servicer.visualizeState,
                    request_deserializer=orchestrator__pb2.State.FromString,
                    response_serializer=orchestrator__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MazeGUI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MazeGUI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def requestTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MazeGUI/requestTask',
            orchestrator__pb2.Empty.SerializeToString,
            orchestrator__pb2.Goal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def processTaskResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MazeGUI/processTaskResult',
            orchestrator__pb2.Result.SerializeToString,
            orchestrator__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MazeGUI/getState',
            orchestrator__pb2.Empty.SerializeToString,
            orchestrator__pb2.State.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def visualizeState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MazeGUI/visualizeState',
            orchestrator__pb2.State.SerializeToString,
            orchestrator__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AiddlPlannerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.plan = channel.unary_unary(
                '/AiddlPlanner/plan',
                request_serializer=orchestrator__pb2.Problem.SerializeToString,
                response_deserializer=orchestrator__pb2.Solution.FromString,
                )


class AiddlPlannerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def plan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AiddlPlannerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'plan': grpc.unary_unary_rpc_method_handler(
                    servicer.plan,
                    request_deserializer=orchestrator__pb2.Problem.FromString,
                    response_serializer=orchestrator__pb2.Solution.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AiddlPlanner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AiddlPlanner(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def plan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlPlanner/plan',
            orchestrator__pb2.Problem.SerializeToString,
            orchestrator__pb2.Solution.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AiddlSimulatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.doAction = channel.unary_unary(
                '/AiddlSimulator/doAction',
                request_serializer=orchestrator__pb2.Action.SerializeToString,
                response_deserializer=orchestrator__pb2.Result.FromString,
                )
        self.getState = channel.unary_unary(
                '/AiddlSimulator/getState',
                request_serializer=orchestrator__pb2.Empty.SerializeToString,
                response_deserializer=orchestrator__pb2.State.FromString,
                )
        self.setState = channel.unary_unary(
                '/AiddlSimulator/setState',
                request_serializer=orchestrator__pb2.State.SerializeToString,
                response_deserializer=orchestrator__pb2.Empty.FromString,
                )


class AiddlSimulatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def doAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AiddlSimulatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'doAction': grpc.unary_unary_rpc_method_handler(
                    servicer.doAction,
                    request_deserializer=orchestrator__pb2.Action.FromString,
                    response_serializer=orchestrator__pb2.Result.SerializeToString,
            ),
            'getState': grpc.unary_unary_rpc_method_handler(
                    servicer.getState,
                    request_deserializer=orchestrator__pb2.Empty.FromString,
                    response_serializer=orchestrator__pb2.State.SerializeToString,
            ),
            'setState': grpc.unary_unary_rpc_method_handler(
                    servicer.setState,
                    request_deserializer=orchestrator__pb2.State.FromString,
                    response_serializer=orchestrator__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AiddlSimulator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AiddlSimulator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def doAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlSimulator/doAction',
            orchestrator__pb2.Action.SerializeToString,
            orchestrator__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlSimulator/getState',
            orchestrator__pb2.Empty.SerializeToString,
            orchestrator__pb2.State.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiddlSimulator/setState',
            orchestrator__pb2.State.SerializeToString,
            orchestrator__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
