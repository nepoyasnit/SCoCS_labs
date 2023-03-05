from app import App


def main():
    # app = App()
    try:
        App().start_app()
    except KeyboardInterrupt:
        print('\nThe application is stopped. Goodbye!')


if __name__ == '__main__':
    main()
