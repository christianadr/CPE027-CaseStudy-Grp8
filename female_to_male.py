import argparse
import os
from pedalboard.io import AudioFile
from pedalboard import Pedalboard, PitchShift, LowpassFilter

def to_male(input, pitch, frequency):
    chunk_size = 500_000
    out_filename = str(input).split('\\')[-1]
    out_filepath = os.path.join("converted", out_filename)

    female_to_male = Pedalboard([
        PitchShift(semitones=float(pitch)),
        LowpassFilter(cutoff_frequency_hz=float(frequency))
    ])

    with AudioFile(input) as f: # Reads the audio file
        with AudioFile(out_filepath, "w", f.samplerate) as o: # Allows AudioFile to output file
            while f.tell() < f.frames:
                # Read frames based on chunk size
                audio = f.read(chunk_size)[0] # only reads the left channel

                # Edit audio
                out_audio = female_to_male(audio, f.samplerate)

                # Write the results in out.mp3
                o.write(out_audio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input audio file path. Use '\\' as separator.")
    parser.add_argument("--pitch", default=-3.7, help="Input semitones for changing pitch. (Default = -3.7)")
    parser.add_argument("--lfilter", default=900, help="Input the cut off frequency for low pass filter. (Default = 900Hz)")
    args = parser.parse_args()

    to_male(args.input_file, args.pitch, args.lfilter)
