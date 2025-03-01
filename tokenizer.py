# from miditok import REMI, TokenizerConfig, MusicTokenizer
from miditok import *
import miditoolkit
from pathlib import Path

path = list(Path("LakhMidiDataset").glob('**/*.mid'))

tokenizer = REMI(TokenizerConfig(use_programs=True))
print("=====")
print (tokenizer)
print("======")


tokenizer.train(
    vocab_size=100000,
    model="BPE",
    files_paths=path,
)

print(tokenizer)

tokenizer.save("tokens.json")
 
# newmidi = miditoolkit.MidiFile("LakhMidiDataset\Aint_No_Sunshine.mid")
# print(newmidi)

midiraw = ["California_Dreamin.mid"]

# tokentest = tokenizer.midi_to_tokens(midiraw[0])
tokentest = tokenizer.encode(midiraw[0])
decodedtest= tokenizer.decode(tokentest)

print(tokentest)
print(decodedtest)

tokenizer.save_model("trained_tokenizer_model")


# decodedtest.dump_midi(Path())

