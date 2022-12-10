"""
# Socket Builder
"""

from typing import Optional
from typing import List

from ._builder import _Builder
from ..core.models import Socket


class SocketBuilder(_Builder):
    __slots__ = (
        "_listen_stream",
        "_listen_datagram",
        "_listen_sequential_packet",
        "_listen_fifo",
        "_accept",
        "_socket_user",
        "_socket_group",
        "_socket_mode",
        "_service",
    )

    @property
    def allowed_none_fields(self) -> List[str]:
        return [
            "_listen_stream", "_listen_datagram", "_listen_sequential_packet",
            "_listen_fifo", "_accept", "_socket_user", "_socket_group",
            "_socket_mode", "_service",
        ]

    def build(self) -> Socket:
        self._check()
        return Socket(
            listen_stream=self._listen_stream,
            listen_datagram=self._listen_datagram,
            listen_sequential_packet=self._listen_sequential_packet,
            listen_fifo=self._listen_fifo,
            accept=self._accept,
            socket_user=self._socket_user,
            socket_group=self._socket_group,
            socket_mode=self._socket_mode,
            service=self._service,
        )

    def __init__(self):
        self._listen_stream: Optional[List[str]] = None
        self._listen_datagram: Optional[List[str]] = None
        self._listen_sequential_packet: Optional[List[str]] = None
        self._listen_fifo: Optional[List[str]] = None
        self._accept: Optional[bool] = None
        self._socket_user: Optional[str] = None
        self._socket_group: Optional[str] = None
        self._socket_mode: Optional[str] = None
        self._service: Optional[str] = None

    def with_listen_stream(self, listen_stream: List[str]) -> 'SocketBuilder':
        self._listen_stream = listen_stream
        return self

    def with_listen_datagram(self, listen_datagram: List[str]) -> 'SocketBuilder':
        self._listen_datagram = listen_datagram
        return self

    def with_listen_sequential_packet(self, listen_sequential_packet: List[str]) -> 'SocketBuilder':
        self._listen_sequential_packet = listen_sequential_packet
        return self

    def with_listen_fifo(self, listen_fifo: List[str]) -> 'SocketBuilder':
        self._listen_fifo = listen_fifo
        return self

    def with_accept(self, accept: bool) -> 'SocketBuilder':
        self._accept = accept
        return self

    def with_socket_user(self, socket_user: str) -> 'SocketBuilder':
        self._socket_user = socket_user
        return self

    def with_socket_group(self, socket_group: str) -> 'SocketBuilder':
        self._socket_group = socket_group
        return self

    def with_socket_mode(self, socket_mode: str) -> 'SocketBuilder':
        self._socket_mode = socket_mode
        return self

    def with_service(self, service: str) -> 'SocketBuilder':
        self._service = service
        return self
