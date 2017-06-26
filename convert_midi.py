import os
import sys
from midi_tools import read_midi


def convert_dir(MIDI_DIR, mode):
    chords = []
    for DIR, _, FILES in os.walk(MIDI_DIR):
        for f in FILES:
            if f.endswith(('.mid', '.midi')):
                try:
                    new_chords = read_midi(os.path.join(DIR, f), mode) # mode is 'chord' or 'notes'
                except:
                    print('problem reading file')

                # if there are new chords, append them
                if new_chords:
                    chords += new_chords

    with open('data_as_words', 'w') as f:
        f.write(' '.join(chords))

if __name__ == "__main__":
    convert_dir(sys.argv[1], sys.argv[2])
