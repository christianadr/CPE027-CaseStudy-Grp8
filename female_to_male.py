import argparse
from pedalboard.io import AudioFile
from pedalboard import Pedalboard, PitchShift, LowpassFilter

def to_male(input):
    chunk_size = 500_000
    out_filename = f"[converted]{input}"

    female_to_male = Pedalboard([
        PitchShift(semitones=-3.7),
        LowpassFilter(cutoff_frequency_hz=900)
    ])

    with AudioFile(input) as f: # Reads the audio file
        with AudioFile(out_filename, "w", f.samplerate) as o: # Allows AudioFile to output file
            while f.tell() < f.frames:
                # Read frames based on chunk size
                audio = f.read(chunk_size)[0] # only reads the left channel

                # Edit audio
                out_audio = female_to_male(audio, f.samplerate)

                # Write the results in out.mp3
                o.write(out_audio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input audio file path")
    args = parser.parse_args()

    to_male(args.input_file)
