import unittest
import tempfile
import os
import subprocess
import mido
from src.converters.note_mappings import NOTE_MAPPINGS
from src.converters.midi_converter import MidiConverter


class TestMidiIntegration(unittest.TestCase):
    def test_main_program_conversion(self):
        # Create a temporary input MIDI file.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_in:
            input_filename = temp_in.name

        # Create a temporary output MIDI file.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_out:
            output_filename = temp_out.name

        try:
            # Build a minimal MIDI file using mido.
            mid = mido.MidiFile()
            track = mido.MidiTrack()
            mid.tracks.append(track)
            track.append(mido.Message('note_on', note=36, velocity=100, time=0))
            mid.save(input_filename)

            # Call your main program using subprocess.
            result = subprocess.run(
                ["python", "convert_midi.py", input_filename, output_filename],
                capture_output=True,
                text=True
            )
            # Ensure the program exited successfully.
            self.assertEqual(result.returncode, 0, msg=f"Program error: {result.stderr}")

            # Load the output MIDI file with mido.
            mid_converted = mido.MidiFile(output_filename)
            converted_note_names = []
            for track in mid_converted.tracks:
                for msg in track:
                    if msg.type == 'note_on':
                        # Use our custom helper function to convert the note number to a note name.
                        converted_note_names.append(MidiConverter().midi_note_to_name(msg.note))

            # Verify that the conversion was applied.
            self.assertIn("C0", converted_note_names, 
                          msg="Expected converted note 'C1' not found in output file.")

        finally:
            # Cleanup temporary files.
            os.remove(input_filename)
            os.remove(output_filename)

    def test_full_midi_conversion_preserves_non_note_data(self):
        """
        This test builds a comprehensive MIDI file that includes meta messages,
        note_on/note_off messages (some that are mapped and some that are not),
        then runs the conversion. It then compares the original and converted files
        message-by-message. All properties must match exactly except for note values
        on note messages that are converted.
        """
        # Create temporary input and output MIDI files.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_in:
            input_filename = temp_in.name
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_out:
            output_filename = temp_out.name

        try:
            # Build a comprehensive MIDI file using mido.
            mid = mido.MidiFile()
            track = mido.MidiTrack()
            mid.tracks.append(track)

            # Add a meta message (e.g., track name).
            track.append(mido.MetaMessage('track_name', name='Test Track', time=0))
            # Add a tempo meta message.
            track.append(mido.MetaMessage('set_tempo', tempo=500000, time=0))

            # Add a note_on and note_off message for a note that should be mapped.
            # For example, note 36 (which our helper converts to "C1").
            track.append(mido.Message('note_on', note=36, velocity=100, time=0))
            track.append(mido.Message('note_off', note=36, velocity=64, time=100))

            # Add a note_on and note_off message for a note that is not mapped.
            # For example, note 30 (assuming "30" is not in the mapping).
            track.append(mido.Message('note_on', note=30, velocity=110, time=50))
            track.append(mido.Message('note_off', note=30, velocity=64, time=100))

            mid.save(input_filename)

            # Run the main program via subprocess.
            result = subprocess.run(
                ["python", "convert_midi.py", input_filename, output_filename],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0, msg=f"Program error: {result.stderr}")

            # Load both the original and converted MIDI files.
            original_mid = mido.MidiFile(input_filename)
            converted_mid = mido.MidiFile(output_filename)

            # Assert that the number of tracks is the same.
            self.assertEqual(len(original_mid.tracks), len(converted_mid.tracks),
                             msg="Number of tracks differ between original and converted files.")

            # Iterate over tracks and messages.
            for orig_track, conv_track in zip(original_mid.tracks, converted_mid.tracks):
                self.assertEqual(len(orig_track), len(conv_track),
                                 msg="Number of messages in a track differ between original and converted files.")
                for orig_msg, conv_msg in zip(orig_track, conv_track):
                    if orig_msg.is_meta:
                        # For meta messages, the entire message should be identical.
                        self.assertEqual(orig_msg.dict(), conv_msg.dict(),
                                         msg="Meta messages differ between original and converted files.")
                    elif orig_msg.type in ['note_on', 'note_off']:
                        # For note messages, everything must be the same except the note value.
                        # Determine the expected note:
                        # Convert the original note number to a note name.
                        orig_note_name = MidiConverter().midi_note_to_name(orig_msg.note)
                        # Check if this note is mapped.
                        if orig_note_name in NOTE_MAPPINGS:
                            expected_note_name = NOTE_MAPPINGS[orig_note_name]
                        else:
                            expected_note_name = orig_note_name
                        # Convert the expected note name back to a MIDI note number.
                        expected_note_number = MidiConverter().note_name_to_int(expected_note_name)

                        # Assert that the converted message has the expected note number.
                        self.assertEqual(conv_msg.note, expected_note_number,
                                         msg=f"Expected note {expected_note_number} for original note {orig_msg.note} "
                                             f"({orig_note_name} -> {expected_note_name}), but got {conv_msg.note}.")
                        # Also ensure that velocity and time remain unchanged.
                        self.assertEqual(orig_msg.velocity, conv_msg.velocity,
                                         msg="Velocity differs between original and converted note messages.")
                        self.assertEqual(orig_msg.time, conv_msg.time,
                                         msg="Time delta differs between original and converted note messages.")
                        # And that the type is the same.
                        self.assertEqual(orig_msg.type, conv_msg.type,
                                         msg="Message type differs between original and converted note messages.")
                    else:
                        # For any other message types, compare their dictionaries.
                        self.assertEqual(orig_msg.dict(), conv_msg.dict(),
                                         msg="A non-note message differs between original and converted files.")

        finally:
            # Cleanup temporary files.
            os.remove(input_filename)
            os.remove(output_filename)

    def test_real_midi_file(self):
        """
        This test uses a real MIDI file from the workspace, runs the conversion,
        and compares the output file with the original file to ensure they are the same
        except for the mapped notes.
        """
        input_filename = 'tests/resources/drums_test.mid'
        output_filename = 'tests/resources/converted_midi_file.mid'

        try:
            # Run the main program via subprocess.
            result = subprocess.run(
                ["python", "convert_midi.py", input_filename, output_filename],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0, msg=f"Program error: {result.stderr}")

            # Load both the original and converted MIDI files.
            original_mid = mido.MidiFile(input_filename)
            converted_mid = mido.MidiFile(output_filename)

            # Assert that the number of tracks is the same.
            self.assertEqual(len(original_mid.tracks), len(converted_mid.tracks),
                             msg="Number of tracks differ between original and converted files.")

            # Iterate over tracks and messages.
            for orig_track, conv_track in zip(original_mid.tracks, converted_mid.tracks):
                self.assertEqual(len(orig_track), len(conv_track),
                                 msg="Number of messages in a track differ between original and converted files.")
                for orig_msg, conv_msg in zip(orig_track, conv_track):
                    if orig_msg.is_meta:
                        # For meta messages, the entire message should be identical.
                        self.assertEqual(orig_msg.dict(), conv_msg.dict(),
                                         msg="Meta messages differ between original and converted files.")
                    elif orig_msg.type in ['note_on', 'note_off']:
                        # For note messages, everything must be the same except the note value.
                        # Determine the expected note:
                        # Convert the original note number to a note name.
                        orig_note_name = MidiConverter().midi_note_to_name(orig_msg.note)
                        # Check if this note is mapped.
                        if orig_note_name in NOTE_MAPPINGS:
                            expected_note_name = NOTE_MAPPINGS[orig_note_name]
                        else:
                            expected_note_name = orig_note_name
                        # Convert the expected note name back to a MIDI note number.
                        expected_note_number = MidiConverter().note_name_to_int(expected_note_name)

                        # Assert that the converted message has the expected note number.
                        self.assertEqual(conv_msg.note, expected_note_number,
                                         msg=f"Expected note {expected_note_number} for original note {orig_msg.note} "
                                             f"({orig_note_name} -> {expected_note_name}), but got {conv_msg.note}.")
                        # Also ensure that velocity and time remain unchanged.
                        self.assertEqual(orig_msg.velocity, conv_msg.velocity,
                                         msg="Velocity differs between original and converted note messages.")
                        self.assertEqual(orig_msg.time, conv_msg.time,
                                         msg="Time delta differs between original and converted note messages.")
                        # And that the type is the same.
                        self.assertEqual(orig_msg.type, conv_msg.type,
                                         msg="Message type differs between original and converted note messages.")
                    else:
                        # For any other message types, compare their dictionaries.
                        self.assertEqual(orig_msg.dict(), conv_msg.dict(),
                                         msg="A non-note message differs between original and converted files.")

        finally:
            # Cleanup temporary files.
            if os.path.exists(output_filename):
                os.remove(output_filename)
    def test_midi_file_length_preserved(self):
        """
        This test verifies that the overall duration (sum of delta times)
        in each track of the MIDI file is preserved after conversion.
        It creates an input file with multiple tracks and known delta times,
        runs the conversion via the main program, and then checks that the
        sum of the 'time' fields in each track is the same in the output file.
        """
        # Create temporary input and output MIDI files.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_in:
            input_filename = temp_in.name
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_out:
            output_filename = temp_out.name

        try:
            # Build a MIDI file with two tracks, each with several messages with non-zero times.
            mid = mido.MidiFile()
            for _ in range(2):
                track = mido.MidiTrack()
                # Add a few messages with delta times.
                track.append(mido.Message('note_on', note=36, velocity=100, time=10))
                track.append(mido.Message('note_off', note=36, velocity=64, time=20))
                track.append(mido.Message('note_on', note=30, velocity=110, time=30))
                track.append(mido.Message('note_off', note=30, velocity=64, time=40))
                mid.tracks.append(track)
            mid.save(input_filename)

            # Run the main program using subprocess.
            result = subprocess.run(
                ["python", "convert_midi.py", input_filename, output_filename],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0, msg=f"Program error: {result.stderr}")

            # Load both the original and converted MIDI files.
            original_mid = mido.MidiFile(input_filename)
            converted_mid = mido.MidiFile(output_filename)

            # Check that the number of tracks is the same.
            self.assertEqual(len(original_mid.tracks), len(converted_mid.tracks),
                             msg="Number of tracks differ between original and converted files.")

            # For each track, compute the total delta time and compare.
            for i, (orig_track, conv_track) in enumerate(zip(original_mid.tracks, converted_mid.tracks)):
                orig_total_time = sum(msg.time for msg in orig_track)
                conv_total_time = sum(msg.time for msg in conv_track)
                self.assertEqual(orig_total_time, conv_total_time,
                                 msg=(f"Track {i} length differs: original total time {orig_total_time}, "
                                      f"converted total time {conv_total_time}"))
        finally:
            # Cleanup temporary files.
            os.remove(input_filename)
            os.remove(output_filename)

if __name__ == '__main__':
    unittest.main()
