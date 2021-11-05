import zulip
import func
import command
from cmdintp import CommandInterpreter

ci = CommandInterpreter({
    "help": command.cmd_help,
    "rng": command.cmd_rng,
    "roll": command.cmd_roll,
})

client = zulip.Client(config_file="zuliprc")

client.call_on_each_event(
    lambda e: client.send_message(ci.handle_event(e)),
    event_types=["message"],
    all_public_streams=True,
)
