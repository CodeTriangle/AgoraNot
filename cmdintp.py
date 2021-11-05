import func

class CommandInterpreter:
    def __init__(self, commands):
        self.__commands = commands

    def add_command(self, command, func):
        if command not in self.__commands:
            self.__commands[command] = func

    def handle_event(self, event):
        if event["type"] == "message":
            return func.make_response(
                event["message"],
                self.handle_message(event["message"])
            )

    def handle_message(self, msg):
        content = msg["content"]
        if content[0] == "%":
            return self.interpret(*func.split_message(content[1:]))

    def interpret(self, command, *args):
        if cmdfunc := self.__commands.get(command):
            return cmdfunc(*args)
        return None
