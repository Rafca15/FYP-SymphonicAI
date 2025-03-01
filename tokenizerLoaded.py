from miditok import *
from pathlib import *

tokenizer = REMI(params = Path("tokens.json"))

print(tokenizer)

midiraw = ["California_Dreamin.mid", "LakhMidiDataset\The_Things_We_Do_for_Love.mid"]

# tokentest = tokenizer.midi_to_tokens(midiraw[0])
tokentest = tokenizer.encode(midiraw[1])
decodedtest= tokenizer.decode(tokentest)

print(tokentest)
print("==========")
print(decodedtest)

generated_midi = tokenizer(tokentest)
print(generated_midi)

generated_midi.dump_midi(Path("The_Things_We_Do_for_Love_Decoded.mid"))