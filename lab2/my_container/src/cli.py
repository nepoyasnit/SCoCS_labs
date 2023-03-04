class CLI:
    _commands: dict[str, callable]
    is_work = True

    def __init__(self):
        self._commands = {}

    @classmethod
    def parse_command(cls):
        user_input = input('Enter command: ').split(maxsplit=1)

        if not user_input:
            print('Empty input!')
            return

        command = user_input[0]
        arguments = command[1] if len(command) > 1 else None

        function_from_command = cls._commands.get(command)
        if not function_from_command:
            print('Unknown command!')
            return
        function_from_command(arguments)

    @classmethod
    def start_app(cls):
        app = CLI()

        while cls.is_work:
            app.parse_command()

