from enum import Enum
from typing import List, Union, Optional, Dict
from pydantic import BaseModel
from pydantic import Field
from pydantic.main import ModelMetaclass  # noqa

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

    @staticmethod
    def load_from_string(text: str, model: ModelMetaclass = None) -> 'Section':
        """
        Load Section from string

        :param text: Service text to load
        :type text: str

        :param model: Model to load
        :type model: ModelMetaclass

        :return: Section
        :rtype: Section

        :raise SystemdPyError: If text is not valid
        """

        if not text.strip().startswith('['):
            raise SystemdPyError(f'Invalid section: {text}')

        section_name = text.split('[')[1].split(']')[0]

        text = text.strip()
        text = text[text.find('['):]
        text = text[text.find(']')+1:]
        text = text.strip()

        if not text:
            raise SystemdPyError(f'Invalid section: {text}')

        props = {
            'extra': {}
        }

        if model is None:
            import importlib
            try:
                model = getattr(importlib.import_module('systemd_py.core.models'), section_name)
            except AttributeError as e:
                raise SystemdPyError(f'Invalid section: {text}') from e

        for line in text.splitlines():
            if not line.strip().startswith('#'):
                k, v = line.split('=', 1)
                k = ''.join(['_' + i.lower() if i.isupper() else i for i in k]).lstrip('_')
                v = v.strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                if v.startswith("'") and v.endswith("'"):
                    v = v[1:-1]
                if v.startswith('[') and v.endswith(']'):
                    v = v[1:-1].split()
                if v.lower() == 'true':
                    v = True
                elif v.lower() == 'false':
                    v = False
                elif v.isdigit():
                    v = int(v)
                elif v.replace('.', '', 1).isdigit():
                    v = float(v)

                if k in model.__fields__:
                    props[k] = v
                else:
                    props['extra'].update({k: v})

        return model(**props)

    def __str__(self):
        if all(getattr(self, s) is None for s in self.__fields__):
            raise SystemdPyError(f'{self.__class__.__name__} is empty')

        text = ""
        dict_ = self.dict(by_alias=True, exclude_none=True)
        extra = dict_.pop('Extra', None)

        for k, v in dict_.copy().items():
            if v in (None, '', [], (), {}, ..., Ellipsis):
                dict_.pop(k)
                continue
            dict_[k] = self._to_str(v)

        text += "\n".join([f'{k}={v!r}' for k, v in dict_.items()])

        if extra:
            for k, v in extra.items():
                text += f'\n{k}={v}'

        text = text.strip()

        if text and not text.isspace():
            return f'[{self.__class__.__name__}]\n{text}'

        return ''

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Section):
            if other.__str__().strip().isspace() or other.__str__() == '':
                return self
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
