# Socket Builder Example

This example shows how to use the `SocketBuilder` to create unit file `[Socket]` section.

```python title="socket_builder.py" linenums="1"
from systemd_py import SocketBuilder


def main():
    builder = SocketBuilder()
    builder.with_listen_stream(["8000"])
    builder.with_accept(True)

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