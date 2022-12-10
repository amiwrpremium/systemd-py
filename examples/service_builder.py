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
