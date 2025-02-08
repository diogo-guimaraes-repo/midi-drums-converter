from src.converters.midi_converter import MidiConverter

def convert_midi_file(input_path, output_path):
    converter = MidiConverter()
    converter.convert_to_pv(input_path, output_path)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert MIDI file notes.')
    parser.add_argument('input_path', type=str, help='Path to the input MIDI file')
    parser.add_argument('output_path', type=str, help='Path to the output MIDI file')
    args = parser.parse_args()

    convert_midi_file(args.input_path, args.output_path)
    print(f'Converted MIDI file saved to {args.output_path}')