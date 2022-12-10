from systemd_py import SocketBuilder


def main():
    builder = SocketBuilder()
    builder.with_listen_stream(["8000"])
    builder.with_accept(True)

    section = builder.build()

    print(section)


if __name__ == "__main__":
    main()
