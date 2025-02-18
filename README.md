# Potential Fishstick

This repository serves as a collection of random coding ideas and experiments. It contains various scripts and programs that explore different concepts, algorithms, and functionalities. Below are descriptions of some of the files currently in the repository.

## Files

### 1. `Recover.c`
`Recover.c` is a program that recovers JPEG files from a forensic image. It scans through a raw data file, identifies the beginning of JPEG files based on specific byte patterns, and writes each recovered file to disk with a sequential filename (e.g., "001.jpg", "002.jpg"). The program is useful for data recovery and digital forensics.

### 2. `Bricks.py`
`Bricks.py` is a simple Python script that prints a pyramid of bricks. The user is prompted to enter the height of the pyramid (between 1 and 8), and the program prints a left-aligned pyramid of the specified height using the `#` character. The script includes error handling to ensure valid input and demonstrates basic control flow and string manipulation in Python.

### 3. `volume.c`
`volume.c` is a C program that modifies the volume of an audio file. It takes an input WAV file, scales the audio samples by a given factor, and writes the modified audio to a new output WAV file. The program reads the header of the WAV file to preserve the format and processes each audio sample to apply the volume change. It is useful for audio processing tasks.

## Usage
- **Recover.c**: Compile and run the program, providing a forensic image file as input to recover any embedded JPEG files.
- **Bricks.py**: Run the script and follow the prompt to input the desired height of the pyramid.
- **volume.c**: Compile and run the program with the input WAV file, output WAV file, and volume scaling factor as arguments to modify the volume of the audio.

## License
This repository does not currently specify a license. Please contact the repository owner for information regarding usage and contributions.

## Contributions
Feel free to contribute by adding more random code snippets or enhancing the existing ones. This repository is a playground for experimenting with different ideas, so creativity is encouraged!

---

This repository is a place for experimenting, learning, and having fun with code. The contents may range from simple scripts to more complex programs, and they are not always production-ready. Enjoy exploring the ideas and feel free to reach out with any questions or suggestions!
