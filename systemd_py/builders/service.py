"""
# Service Builder
"""

from typing import Optional
from typing import List

from ._builder import _Builder
from ..core.models import Service
from ..core.types import TypeType, RestartType


class ServiceBuilder(_Builder):
    __slots__ = (
        '_type',
        '_remain_after_exit',
        '_pid_file',
        '_bus_name',
        '_notify_access',
        '_exec_start',
        '_exec_start_pre',
        '_exec_start_post',
        '_exec_reload',
        '_exec_stop',
        '_exec_stop_post',
        '_restart_sec',
        '_restart',
        '_timeout_sec'
    )

    @property
    def allowed_none_fields(self) -> List[str]:
        return [
            '_pid_file', '_bus_name', '_notify_access', '_exec_start_pre',
            '_exec_start_post', '_exec_reload', '_exec_stop_post'
        ]

    def __init__(self):
        self._type: Optional[TypeType] = None
        self._remain_after_exit: Optional[bool] = None
        self._pid_file: Optional[str] = None
        self._bus_name: Optional[str] = None
        self._notify_access: Optional[str] = None
        self._exec_start: Optional[List[str]] = None
        self._exec_start_pre: Optional[List[str]] = None
        self._exec_start_post: Optional[List[str]] = None
        self._exec_reload: Optional[List[str]] = None
        self._exec_stop: Optional[List[str]] = None
        self._exec_stop_post: Optional[List[str]] = None
        self._restart_sec: Optional[int] = None
        self._restart: Optional[RestartType] = None
        self._timeout_sec: Optional[int] = None

    def build(self) -> Service:
        self._check()
        return Service(
            type=self._type,
            remain_after_exit=self._remain_after_exit,
            pid_file=self._pid_file,
            bus_name=self._bus_name,
            notify_access=self._notify_access,
            exec_start=self._exec_start,
            exec_start_pre=self._exec_start_pre,
            exec_start_post=self._exec_start_post,
            exec_reload=self._exec_reload,
            exec_stop=self._exec_stop,
            exec_stop_post=self._exec_stop_post,
            restart_sec=self._restart_sec,
            restart=self._restart,
            timeout_sec=self._timeout_sec
        )

    def with_type(self, type: TypeType) -> 'ServiceBuilder':
        self._type = type
        return self

    def with_remain_after_exit(self, remain_after_exit: bool) -> 'ServiceBuilder':
        self._remain_after_exit = remain_after_exit
        return self

    def with_pid_file(self, pid_file: str) -> 'ServiceBuilder':
        self._pid_file = pid_file
        return self

    def with_bus_name(self, bus_name: str) -> 'ServiceBuilder':
        self._bus_name = bus_name
        return self

    def with_notify_access(self, notify_access: str) -> 'ServiceBuilder':
        self._notify_access = notify_access
        return self

    def with_exec_start(self, exec_start: List[str]) -> 'ServiceBuilder':
        self._exec_start = exec_start
        return self

    def with_exec_start_pre(self, exec_start_pre: List[str]) -> 'ServiceBuilder':
        self._exec_start_pre = exec_start_pre
        return self

    def with_exec_start_post(self, exec_start_post: List[str]) -> 'ServiceBuilder':
        self._exec_start_post = exec_start_post
        return self

    def with_exec_reload(self, exec_reload: List[str]) -> 'ServiceBuilder':
        self._exec_reload = exec_reload
        return self

    def with_exec_stop(self, exec_stop: List[str]) -> 'ServiceBuilder':
        self._exec_stop = exec_stop
        return self

    def with_exec_stop_post(self, exec_stop_post: List[str]) -> 'ServiceBuilder':
        self._exec_stop_post = exec_stop_post
        return self

    def with_restart_sec(self, restart_sec: int) -> 'ServiceBuilder':
        self._restart_sec = restart_sec
        return self

    def with_restart(self, restart: RestartType) -> 'ServiceBuilder':
        self._restart = restart
        return self

    def with_timeout_sec(self, timeout_sec: int) -> 'ServiceBuilder':
        self._timeout_sec = timeout_sec
        return self
