import argparse
from PIL import Image
import numpy as np
import os
import sys

def xor_mode(pixels, key):
    return pixels ^ key


def swap_mode(pixels, key, reverse=False):
    h, w, c = pixels.shape
    flat = pixels.reshape(-1, c)

    np.random.seed(key)
    perm = np.random.permutation(len(flat))

    if reverse:
        inv_perm = np.argsort(perm)
        flat = flat ^ key
        flat = flat[inv_perm]
    else:
        flat = flat[perm]
        flat = flat ^ key

    return flat.reshape(h, w, c)


def process_image(input_path, output_path, key, mode):
    if not os.path.exists(input_path):
        print(f"[✗] Input file not found: {input_path}")
        sys.exit(1)

    if not (0 <= key <= 255):
        print("[✗] Key must be between 0 and 255")
        sys.exit(1)

    img = Image.open(input_path).convert("RGB")
    pixels = np.array(img)

    if mode == "xor":
        result = xor_mode(pixels, key)

    elif mode == "swap":
        # Detect decrypt vs encrypt by file name convention
        reverse = "encrypted" in input_path.lower()
        result = swap_mode(pixels, key, reverse=reverse)

    else:
        print("[✗] Invalid mode")
        sys.exit(1)

    Image.fromarray(result.astype(np.uint8)).save(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Image Encryption Tool with XOR and Pixel Swap modes"
    )

    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-k", "--key", required=True, type=int)
    parser.add_argument(
        "--mode",
        required=True,
        choices=["xor", "swap"],
        help="Encryption mode: xor (value-based) or swap (position-based)"
    )

    args = parser.parse_args()

    process_image(args.input, args.output, args.key, args.mode)

    print("[✓] Operation completed")
    print(f"    Mode  : {args.mode}")
    print(f"    Input : {args.input}")
    print(f"    Output: {args.output}")
    print(f"    Key   : {args.key}")


if __name__ == "__main__":
    main()
