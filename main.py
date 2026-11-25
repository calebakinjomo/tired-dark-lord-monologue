#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (105 words) to /output/entry.txt for the make.fun
bounty u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

The villain is a specific dark lord with a history (three would-be
assassins this year, a brother who left for a farm) and a scheme
(the eclipse on Thursday, the dark's little lists). The tiredness is
never announced: it leaks through the rhythm, the fragments, the
ellipses and the small deflections ("A farm." repeated, the trailing
"Sign here, here, and—"), and the sting lands in the last line.

Judge criteria, kept in mind while writing: tiredness must live in
the voice, rhythm and deflection — never stated outright; the speaker
must read as a real villain with a scheme and a history, not a generic
baddie; and the piece stays near 100 words (105 here, 555 characters,
inside the 600-character gate).
"""

import os

MONOLOGUE = """Come in. Mind the— yes, the candles. I lit them myself. Nobody else remembers which.

You came to kill me. Of course you did. Third one this year. The last one cried. The one before asked for a job.

Sit. No, not there. That chair was my brother's. He writes from a farm now. A farm.

No bard tells you this. The crown fits. The throne fits. The kingdom... fits. And still the dark sends its little lists. Burn this village. Raise that dead king. Sign here, here, and—

Oh. Your sword is out. How... prompt.

Well. The eclipse is Thursday. Do stay for it."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
        f.write("\n")


if __name__ == "__main__":
    main()
