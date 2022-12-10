from systemd_py import InstallBuilder


def main():
    builder = InstallBuilder()
    builder.with_wanted_by(["multi-user.target"])
    builder.with_required_by(["graphical.target"])
    builder.with_alias(["my-alias.service"])

    section = builder.build()

    print(section)


if __name__ == "__main__":
    main()
