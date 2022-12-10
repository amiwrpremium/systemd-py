"""
# Unit Builder
"""

from typing import Optional
from typing import List

from ._builder import _Builder
from ..core.models import Unit


class UnitBuilder(_Builder):
    __slots__ = (
        "_description",
        "_documentation",
        "_requires",
        "_wants",
        "_binds_to",
        "_before",
        "_after",
        "_conflicts",
        "_condition",
        "_assert_",
    )

    @property
    def allowed_none_fields(self) -> List[str]:
        return [
            "_documentation", "_requires", "_wants", "_binds_to", "_before",
            "_after", "_conflicts", "_condition", "_assert_",
        ]

    def build(self) -> Unit:
        self._check()
        return Unit(
            description=self._description,
            documentation=self._documentation,
            requires=self._requires,
            wants=self._wants,
            binds_to=self._binds_to,
            before=self._before,
            after=self._after,
            conflicts=self._conflicts,
            condition=self._condition,
            assert_=self._assert_,
        )

    def __init__(self):
        self._description: str = ...
        self._documentation: Optional[str] = ...
        self._requires: Optional[List[str]] = ...
        self._wants: Optional[List[str]] = ...
        self._binds_to: Optional[List[str]] = ...
        self._before: Optional[List[str]] = ...
        self._after: Optional[List[str]] = ...
        self._conflicts: Optional[List[str]] = ...
        self._condition: Optional[str] = ...
        self._assert_: Optional[str] = ...

    def with_description(self, description: str) -> 'UnitBuilder':
        self._description = description
        return self

    def with_documentation(self, documentation: str) -> 'UnitBuilder':
        self._documentation = documentation
        return self

    def with_requires(self, requires: List[str]) -> 'UnitBuilder':
        self._requires = requires
        return self

    def with_wants(self, wants: List[str]) -> 'UnitBuilder':
        self._wants = wants
        return self

    def with_binds_to(self, binds_to: List[str]) -> 'UnitBuilder':
        self._binds_to = binds_to
        return self

    def with_before(self, before: List[str]) -> 'UnitBuilder':
        self._before = before
        return self

    def with_after(self, after: List[str]) -> 'UnitBuilder':
        self._after = after
        return self

    def with_conflicts(self, conflicts: List[str]) -> 'UnitBuilder':
        self._conflicts = conflicts
        return self

    def with_condition(self, condition: str) -> 'UnitBuilder':
        self._condition = condition
        return self

    def with_assert(self, assert_: str) -> 'UnitBuilder':
        self._assert_ = assert_
        return self
