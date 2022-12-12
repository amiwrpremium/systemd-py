# Systemd Utilities

This example shows how to use the `systemd_py.core.models.Section` to load a systemd section


```python title="load_from_string.py" linenums="1"
from systemd_py.core.models import Section


def main():
    text = """
    [Service]
    Type='simple'
    ExecStart='adsas'
    User='root'
    """

    section = Section.load_from_string(text)
    print(section)
    print(type(section))


if __name__ == "__main__":
    main()
```

```python title="load_from_string_with_model.py" linenums="1"
from systemd_py.core.models import Section
from systemd_py.core.models import Service


def main():
    text = """
    [Service]
    Type='simple'
    ExecStart='adsas'
    User='root'
    """

    section = Section.load_from_string(text, model=Service)
    print(section)
    print(type(section))


if __name__ == "__main__":
    main()
```

```python title="load_from_string_with_section_name.py" linenums="1"
from systemd_py.core.models import Section


def main():
    text = """
    [Service]
    Type='simple'
    ExecStart='adsas'
    User='root'
    """

    section = Section.load_from_string(text, model="Service")
    print(section)
    print(type(section))


if __name__ == "__main__":
    main()
```

```bash title="output" linenums="1"
[Service]
Type='simple'
ExecStart='adsas'
User='root'
<class 'systemd_py.core.models.service.Service'>
```