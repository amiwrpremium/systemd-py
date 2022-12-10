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
