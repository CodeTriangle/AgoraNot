import random
import re

def cmd_help(*args):
    return "I'm not sure what I am, but I'm not AgoraBot."

def cmd_rng(*args):
    low = 1
    high = 0
    if len(args) == 1:
        high = int(args[0])
    elif len(args) == 2:
        low  = int(args[0])
        high = int(args[1])
    elif len(args) < 1:
        return "I need at least one argument."
    else:
        return "Two arguments at most, please."

    rnd = random.randint(low, high)
    return f"Your random number between **{low}** and **{high}** is **{rnd}**."

def cmd_roll(*args):
    history = []
    total = 0
    for r in args:
        if r[0] in ["+", "-"]:
            if r.isnumeric() and (i := int(r)) > 0:
                total += i
                history.append(i)
            else:
                return f"**{r}** is not a valid integer format!"
        elif m := re.fullmatch(r"(\d+)?d(\d+)", r):
            numdice = 1
            sides = 0
            g1 = m.group(1)
            g2 = m.group(2)
            if g1:
                if (i := int(g1)) > 0:
                    numdice = i
                else:
                    return f"**{g1}** is not a valid dice number specifier!"

            if (i := int(g2)) > 0:
                sides = i
            else:
                return f"**{g2}** is not a valid number of sides for a die!"

            for d in range(numdice):
                rnd = random.randint(1, sides)
                total += rnd
                history.append(rnd)

        else:
            return f"Invalid specifier: **{r}**"

    histstr = ", ".join([f"**{i}**" for i in history])
    return f"Total: **{total}**\n[{histstr}]"
