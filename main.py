#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt. Pure standard library,
deterministic: the same text is produced on every run.
"""

import os

MONOLOGUE = (
    "You want the speech. Fine. Stand there, by the \u2014 no, not the tapestry, "
    "it sheds. Right. I took this crown off a dead king's head at Greyford, "
    "and I have worn it through nine winters of petitions and one determined "
    "badger. My mirror drinks one dream from every "
    "village each month. That is the law. That\u2014 hm. The tea is cold "
    "again. Tell the rebellion I will crush it on Thursday, after the census, "
    "and someone oil this hinge. It squeaks like a\u2014 like a\u2014 The "
    "headsman comes at dawn. No \u2014 after breakfast. I want a front seat."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
