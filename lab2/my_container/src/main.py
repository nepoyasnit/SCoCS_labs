from cli import CLI


def main():
    app = CLI()
    # try:
    app.start_app()
    # except KeyboardInterrupt:
    #     print('/nThe application is stopped. Goodbye!')


if __name__ == '__main__':
    main()
