from cli import CLI
from controller import ContainerController


class App:
    _all_commands = '''
        # add <key> [key, …] – add one or more elements to the container\n
        # remove <key> – delete key from container\n
        # find <key> [key, …] – check if the element is presented in the container\n
        # list – print all elements of container\n
        # grep <regex> – check the value in the container by regular expression\n
        # save/load – save container to file/load container from file\n
        # switch – switches to another user\n
    '''
    is_work = True

    def show_possible_commands(self, args=''):
        print('Hello! List of all commands: \n', self._all_commands)

    def start_app(self):
        print(f'''Hello! It's CLI program-storage for unique elements! ''')
        self.show_possible_commands()

        controller = ContainerController()
        cli = CLI()

        all_commands = ['add', 'load', 'save', 'find', 'remove', 'grep', 'switch', 'list', 'exit']
        for command in all_commands:
            cli.append_command(command, getattr(controller, command))

        cli.append_command('help', self.show_possible_commands)

        while self.is_work:
            cli.parse_command()
