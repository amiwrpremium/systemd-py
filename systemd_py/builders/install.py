"""
# Install Builder
"""

from typing import Optional
from typing import List

from ._builder import _Builder
from ..core.models import Install


class InstallBuilder(_Builder):
    __slots__ = (
        '_wanted_by',
        '_required_by',
        '_alias',
        '_also',
        '_default_instance',
    )

    @property
    def allowed_none_fields(self) -> List[str]:
        return [
            'wanted_by', 'required_by', 'alias', 'also', 'default_instance'
        ]

    def build(self) -> Install:
        self._check()
        return Install(
            wanted_by=self._wanted_by,
            required_by=self._required_by,
            alias=self._alias,
            also=self._also,
            default_instance=self._default_instance
        )

    def __init__(self):
        self._wanted_by: Optional[List[str]] = None
        self._required_by: Optional[List[str]] = None
        self._alias: Optional[List[str]] = None
        self._also: Optional[List[str]] = None
        self._default_instance: Optional[str] = None

    def with_wanted_by(self, wanted_by: List[str]) -> 'InstallBuilder':
        self._wanted_by = wanted_by
        return self

    def with_required_by(self, required_by: List[str]) -> 'InstallBuilder':
        self._required_by = required_by
        return self

    def with_alias(self, alias: List[str]) -> 'InstallBuilder':
        self._alias = alias
        return self

    def with_also(self, also: List[str]) -> 'InstallBuilder':
        self._also = also
        return self

    def with_default_instance(self, default_instance: str) -> 'InstallBuilder':
        self._default_instance = default_instance
        return self
