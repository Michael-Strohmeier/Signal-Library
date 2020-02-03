import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment


# Returns sampling frequency and signal data
def freq_signal(path: str):
    sampling_frequency, signal_data = wavfile.read(path)

    return sampling_frequency, signal_data


# Labeled spectrogram
def spectrogram(path: str):
    sampling_frequency, signal_data = wavfile.read(path)

    plt.specgram(signal_data, Fs=sampling_frequency)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.show()


# Saves spectrogram with no padding or axis labels
def save_spectrogram_image_only(file_out_path: str, sampling_frequency: np.ndarray, signal_data: np.ndarray):
    plt.axis('off')
    plt.specgram(signal_data, Fs=sampling_frequency)
    plt.savefig(file_out_path, bbox_inches='tight', pad_inches=0)


# splits signal data into some specified (sample_length) number of samples
def signal_to_samples_of_n_length(sample_length: int, wav: np.ndarray):
    split_wav = []
    num_samples = int(len(wav) / sample_length)
    for n in range(num_samples):
        split_wav.append(wav[n * sample_length: (n + 1) * sample_length])

    return split_wav


# Converts numpy array to .wav
def np_to_wav(np_wav: np.ndarray, sampling_frequency: int, output_file_name: str):
    wavfile.write(output_file_name, sampling_frequency, np_wav)

    return AudioSegment.from_wav(output_file_name)


if __name__ == '__main__':
    print('Hello World')
