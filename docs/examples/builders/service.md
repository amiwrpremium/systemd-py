# Service Builder Example

This example shows how to use the `ServiceBuilder` to create unit file `[Service]` section.

```python title="service_builder.py" linenums="1"
from systemd_py import ServiceBuilder


def main():
    builder = ServiceBuilder()
    builder.with_type("simple")
    builder.with_exec_start(["/usr/bin/python3", "-m", "http.server", "8000"])
    builder.with_exec_stop(["/usr/bin/kill", "$MAINPID"])
    builder.with_restart("on-failure")

    section = builder.build()

    print(section)


if __name__ == "__main__":
    main()
```

```bash title="output" linenums="1"
[Service]
Type='simple'
ExecStart='/usr/bin/python3 -m http.server 8000'
ExecStop='/usr/bin/kill $MAINPID'
Restart='on-failure'
```