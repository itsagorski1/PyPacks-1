class Function:
    def __init__(self, name):
        self.name = name
        self.commands = []
    def add_command(self, command_name, command_value):
        commands_dict = { "say": f"say {command_value}" }
        self.commands.append(commands_dict[command_name])
    def attach(self, pypack):
        pypack.functions[self.name] = self.commands