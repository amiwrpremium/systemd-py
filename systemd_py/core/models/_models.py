from enum import Enum
from typing import List, Union, Optional, Dict
from pydantic import BaseModel
from pydantic import Field

from ...exceptions import SystemdPyError


class Section(BaseModel):
    """
    Systemd Section
    """

    extra: Optional[Dict[str, str]] = Field(
        None,
        title="Extra",
        description="Extra directives"
    )

    def _to_str(self, value: Union[str, List, int, float, bool]) -> str:
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return " ".join(value)
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, (int, float)):
            return str(value)
        elif value is None:
            raise SystemdPyError(f'{self.__class__.__name__} value cannot be None')
        elif isinstance(value, dict):
            raise SystemdPyError(f'{self.__class__.__name__} does not support dict')
        if isinstance(value, Enum):
            return str(value.value)
        else:
            return str(value)

    def __str__(self):
        if all(getattr(self, s) is None for s in self.__fields__):
            raise SystemdPyError(f'{self.__class__.__name__} is empty')

        text = f'[{self.__class__.__name__}]\n'
        dict_ = self.dict(by_alias=True, exclude_none=True)

        extra = dict_.pop('Extra', None)
        for k, v in dict_.items():
            dict_[k] = self._to_str(v)

        text += "\n".join([f'{k}={v!r}' for k, v in dict_.items()])

        if extra:
            for k, v in extra.items():
                text += f'\n{k}={v}'

        return text

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Section):
            return self.__str__() + "\n\n" + other.__str__()
        return TypeError(f'unsupported operand type(s) for +: {self.__class__.__name__} and {other.__class__.__name__}')

    def __radd__(self, other):
        return self.__add__(other)

    class Config:
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            """
            Convert to CamelCase

            Args:
                string (str, required): String to convert

            Returns:
                str: CamelCase string
            """

            return ''.join(word.capitalize() for word in string.split('_'))
