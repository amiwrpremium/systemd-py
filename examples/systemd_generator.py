from systemd_py import Systemd
from systemd_py import InstallBuilder, ServiceBuilder, SocketBuilder, UnitBuilder
from systemd_py import Install, Service, Socket, Unit


def build_install() -> Install:
    builder = InstallBuilder()
    builder.with_wanted_by(["multi-user.target"])
    builder.with_required_by(["graphical.target"])
    builder.with_alias(["my-alias.service"])

    section = builder.build()

    return section


def build_service() -> Service:
    builder = ServiceBuilder()
    builder.with_type("simple")
    builder.with_exec_start(["/usr/bin/python3", "-m", "http.server", "8000"])
    builder.with_exec_stop(["/usr/bin/kill", "$MAINPID"])
    builder.with_restart("on-failure")

    section = builder.build()

    return section


def build_socket() -> Socket:
    builder = SocketBuilder()
    builder.with_listen_stream(["8000"])
    builder.with_accept(True)

    section = builder.build()

    return section


def build_unit() -> Unit:
    builder = UnitBuilder()
    builder.with_description("Example service")
    builder.with_after(["network.target"])
    builder.with_wants(["network.target"])
    builder.with_requires(["network.target"])

    section = builder.build()

    return section


def main():
    install = build_install()
    service = build_service()
    socket = build_socket()
    unit = build_unit()

    systemd = Systemd("my-service", [install, service, socket, unit])
    my_service = systemd.create()

    print(my_service)


if __name__ == "__main__":
    main()
