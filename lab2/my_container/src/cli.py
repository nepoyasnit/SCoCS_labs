class CLI:
    _commands: dict[str, callable]
    is_work = True

    def __init__(self):
        self._commands = {}

    @staticmethod
    def parse_username():
        username = input('Enter your name: ')
        return username

    def append_command(self, command: str, function: callable):
        self._commands[command] = function

    def parse_command(self):
        user_input = input('Enter command: ').split(maxsplit=1)

        if not user_input:
            print('Empty input!')
            return

        command = user_input[0]
        arguments = user_input[1] if len(user_input) > 1 else None

        function_from_command = self._commands.get(command)

        if not function_from_command:
            print('Unknown command!')
            return
        function_from_command(arguments)
