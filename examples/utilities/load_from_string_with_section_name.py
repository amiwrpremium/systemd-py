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


if __name__ == "__main__":
    main()
