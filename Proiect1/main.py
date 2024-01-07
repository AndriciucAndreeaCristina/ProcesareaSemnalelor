# Import the necessary libraries
from time import time
import numpy as np
from PIL.Image import Image
from scipy import misc
from scipy.fftpack import dct, idct
from collections import defaultdict
import heapq

# Define the DCT and IDCT functions
def dctn(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idctn(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

# Define the block size and the quantization matrix
block_size = 8
Q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]]

# Define the EOP symbol
EOP = (0, 0)

# Define the function to pad the image
def pad_image(X):
    height, width = X.shape
    new_height = (height + block_size - 1) // block_size * block_size
    new_width = (width + block_size - 1) // block_size * block_size
    padded_image = np.zeros((new_height, new_width))
    padded_image[:height, :width] = X
    return padded_image

# Define the function to perform the zigzag scan
def zigzag(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    solution = [[] for i in range(n + m - 1)]
    for i in range(n):
        for j in range(m):
            sum = i + j
            if sum % 2 == 0:
                solution[sum].insert(0, matrix[i][j])
            else:
                solution[sum].append(matrix[i][j])
    res = []
    for i in solution:
        for j in i:
            if j == -0.0:
                j = 0.0
            res.append(j)
    return res

# Define the function to perform the run-length encoding
def run_length_encoding(zigzag):
    rle = []
    count = 0
    for i in range(len(zigzag)):
        if zigzag[i] == 0:
            count += 1
        else:
            rle.append((count, zigzag[i]))
            count = 0
    # Add the EOP symbol at the end
    rle.append(EOP)
    return rle

# Define the function to generate the frequency dictionary
def generate_frequency_dict(rle_data):
    frequency_dict = defaultdict(int)
    for block_rle in rle_data:
        for pair in block_rle:
            frequency_dict[pair] += 1
    for block_rle in rle_data:
        for pair in block_rle:
            frequency_dict[pair] = frequency_dict[pair] / len(rle_data)
    return frequency_dict

# Define the function to generate the Huffman codes
def generate_huffman_codes(freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))

# Define the function to perform the Huffman encoding
def huffman_encoding(data, codes):
    encoded_data = ''.join(codes[symbol] for symbol in data)
    return encoded_data

# Define the function to perform the Huffman decoding
def huffman_decode(encoded_string, codes):
    decoded_data = []
    current_code = ''
    # Reverse the codes dictionary to map codes to symbols
    reversed_codes = {code: symbol for symbol, code in codes.items()}
    for bit in encoded_string:
        current_code += bit
        # Check if the current code is a valid Huffman code
        if current_code in reversed_codes:
            # Get the symbol corresponding to the code
            symbol = reversed_codes[current_code]
            # Check if the symbol is the EOP symbol
            if symbol == EOP:
                # Break the loop
                break
            # Append the symbol to the decoded data
            decoded_data.append(symbol)
            # Reset the current code
            current_code = ''
    return decoded_data

# Define the function to perform the run-length decoding
def run_length_decoding(rle_data):
    decoded_data = []
    for block_rle in rle_data:
        decoded_block = []
        # Inițializăm un contor pentru numărul de zerouri
        zero_count = 0
        # Parcurgem valorile întregi din block_rle
        for value in block_rle:
            # Dacă valoarea este 0, incrementăm contorul
            if value == 0:
                zero_count += 1
            # Altfel, adăugăm contorul și valoarea la blocul decodat
            else:
                for i in range(zero_count):
                    decoded_block.append(0)
                decoded_block.append(value)
                # Resetăm contorul
                zero_count = 0
        # Adăugăm blocul decodat la datele decodate
        decoded_data.append(decoded_block)
    return decoded_data

# Load the image and convert it to grayscale
X = misc.ascent()
X = X.astype(np.float32)
X = X - 128
# Pad the image
X = pad_image(X)
height, width = X.shape
# Initialize the lists to store the zigzag and RLE vectors
Y_zigzag = []
Y_rle = []
# Initialize the arrays to store the DCT and IDCT coefficients
X_dct = np.zeros((height, width))
X_idct = np.zeros((height, width))
# Initialize the counters to store the number of non-zero coefficients
y_nnz = 0
y_jpeg_nnz = 0

# Loop over the blocks of the image
for i in range(0, height, block_size):
    for j in range(0, width, block_size):
        # Get the current block
        x = X[i:i + block_size, j:j + block_size]
        # Apply the DCT
        y = dctn(x)
        # Count the number of non-zero coefficients
        y_nnz += np.count_nonzero(y)
        # Apply the quantization
        y = Q_jpeg * np.round(y / Q_jpeg)
        # Count the number of non-zero coefficients after quantization
        y_jpeg_nnz += np.count_nonzero(y)
        # Perform the zigzag scan
        y_zigzag = zigzag(y)
        # Perform the run-length encoding
        y_rle = run_length_encoding(y_zigzag)
        # Append the RLE vector to the list
        Y_rle.append(y_rle)
        # Apply the IDCT
        x_idct = idctn(y)
        # Store the DCT and IDCT coefficients in the arrays
        X_dct[i:i + block_size, j:j + block_size] = y
        X_idct[i:i + block_size, j:j + block_size] = x_idct

# Generate the frequency dictionary
frequency_dict = generate_frequency_dict(Y_rle)
# Generate the Huffman codes
huffman_codes = generate_huffman_codes(frequency_dict)
# Initialize the encoded string
Y_huffman = ""
# Loop over the RLE vectors
for block_rle in Y_rle:
    # Perform the Huffman encoding
    encoded_block = huffman_encoding(block_rle, huffman_codes)
    # Append the encoded block to the encoded string
    Y_huffman += encoded_block


# Perform the Huffman decoding
Y_rle_decoded = []
for i in range(0, len(Y_huffman), block_size * block_size):
    # Get the encoded string for each block
    encoded_block = Y_huffman[i:i + block_size * block_size]
    # Decode the block using the Huffman codes
    decoded_block = huffman_decode(encoded_block, huffman_codes)
    # Append the decoded block to the list
    Y_rle_decoded.append(decoded_block)

# Perform the run-length decoding
Y_zigzag_decoded = []
for block_rle in Y_rle_decoded:
    # Decode the block using the EOP symbol
    decoded_block = run_length_decoding(block_rle)
    # Append the decoded block to the list
    Y_zigzag_decoded.append(decoded_block)

# Initialize the array to store the IDCT coefficients
X_idct = np.zeros((height, width))


def inverse_zigzag(vector):
    # Verificăm dacă vectorul este vid sau conține numai zerouri
    if len(vector) == 0 or np.count_nonzero(vector) == 0:
        # Returnăm o matrice vidă
        return np.array([])
    # Altfel, continuăm cu algoritmul original
    # Inițializăm matricea ca o matrice pătrată de zerouri
    n = int(np.sqrt(len(vector)))
    matrix = np.zeros((n, n))
    # Inițializăm indicii pentru a parcurge matricea
    i = 0
    j = 0
    # Inițializăm direcția de deplasare
    direction = "up"
    # Parcurgem vectorul
    for value in vector:
        # Adăugăm valoarea la matrice
        matrix[i][j] = value
        # Verificăm direcția de deplasare
        if direction == "up":
            # Dacă suntem pe prima coloană sau pe ultima linie, schimbăm direcția la dreapta
            if i == 0 or j == n - 1:
                direction = "right"
                # Dacă suntem pe ultima linie, ne deplasăm la dreapta
                if j == n - 1:
                    j += 1
                # Altfel, ne deplasăm în diagonală jos-dreapta
                else:
                    i += 1
                    j += 1
            # Altfel, ne deplasăm în diagonală sus-stânga
            else:
                i -= 1
                j -= 1
        elif direction == "down":
            # Dacă suntem pe ultima coloană sau pe prima linie, schimbăm direcția la stânga
            if j == 0 or i == n - 1:
                direction = "left"
                # Dacă suntem pe ultima coloană, ne deplasăm în jos
                if i == n - 1:
                    i += 1
                # Altfel, ne deplasăm în diagonală sus-dreapta
                else:
                    i += 1
                    j -= 1
            # Altfel, ne deplasăm în diagonală jos-stânga
            else:
                i += 1
                j -= 1
        elif direction == "right":
            # Dacă suntem pe ultima coloană, schimbăm direcția la jos
            if j == n - 1:
                direction = "down"
                i += 1
            # Altfel, ne deplasăm la dreapta
            else:
                j += 1
        elif direction == "left":
            # Dacă suntem pe prima coloană, schimbăm direcția la sus
            if j == 0:
                direction = "up"
                i -= 1
            # Altfel, ne deplasăm la stânga
            else:
                j -= 1
    # Returnăm matricea
    return matrix



# Loop over the blocks of the image
for i in range(0, height, block_size):
    for j in range(0, width, block_size):
        # Get the zigzag vector for each block
        y_zigzag = Y_zigzag_decoded[i // block_size * width // block_size + j // block_size]
        # Perform the inverse zigzag scan
        y = inverse_zigzag(y_zigzag)
        # Perform the inverse quantization
        y = y * Q_jpeg
        # Perform the inverse DCT
        x_idct = idctn(y)
        # Store the IDCT coefficients in the array
        X_idct[i:i + block_size, j:j + block_size] = x_idct

# Add 128 to the IDCT coefficients
X_idct = X_idct + 128
# Convert the IDCT coefficients to integers
X_idct = X_idct.astype(np.uint8)
# Save the decoded image
Image.fromarray(X_idct).save("decoded_image.png")
