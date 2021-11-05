def split_message(msg):
    result = []
    while True:
        msg = msg.lstrip()

        if len(msg) == 0: break

        sep = ' '
        if msg[0] in ['"', "'"]:
            sep = msg[0]
            msg = msg[1:]

        out = msg.split(sep, 1)
        result.append(out[0])
        if len(out) > 1:
            msg = out[1]
        else:
            break

    return result


def make_response(msg, content):
    result = {
        "content": content,
        "type": msg["type"],
    }
    
    if msg["type"] == "stream":
        result["topic"] = msg["subject"]
        result["to"] = [msg["stream_id"]]
    else:
        result["to"] = list([r["id"] for r in msg["display_recipient"]])

    return result
