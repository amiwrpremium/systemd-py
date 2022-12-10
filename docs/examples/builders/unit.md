# Unit Builder Example

This example shows how to use the `UnitBuilder` to create unit file `[Unit]` section.

```python title="unit_builder.py" linenums="1"
from systemd_py import UnitBuilder


def main():
    builder = UnitBuilder()
    builder.with_description("Example service")
    builder.with_after(["network.target"])
    builder.with_wants(["network.target"])
    builder.with_requires(["network.target"])

    section = builder.build()

    print(section)


if __name__ == "__main__":
    main()
```

```bash title="output" linenums="1"
[Unit]
Description='Example service'
Requires='network.target'
Wants='network.target'
After='network.target'
```