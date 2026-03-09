"""
Encrypt/decrypt strings using Python standard library only.
Uses a key from environment variable SECRET_KEY (or a default for dev).

# Encrypt
python -m src.util.secrets --key "my-secret-key" --encrypt "hello world"
python -m src.util.secrets -k "my-secret-key" -e "hello world"

# Decrypt
python -m src.util.secrets --key "my-secret-key" --decrypt "base64_ciphertext_here"
python -m src.util.secrets -k "my-secret-key" -d "base64_ciphertext_here"
"""

import argparse
import base64
import hashlib
import os
import sys


def _get_key(key_override: str | None = None) -> bytes:
    raw = key_override or os.environ.get("SECRET_KEY", "default-dev-key-do-not-use-in-production")
    return hashlib.sha256(raw.encode()).digest()


def _xor_bytes(data: bytes, key: bytes) -> bytes:
    key_len = len(key)
    return bytes(b ^ key[i % key_len] for i, b in enumerate(data))


def encrypt(cleartext: str, key: str | None = None) -> str:
    """Encrypt a string; returns base64-encoded ciphertext."""
    key_bytes = _get_key(key)
    data = cleartext.encode("utf-8")
    encrypted = _xor_bytes(data, key_bytes)
    return base64.urlsafe_b64encode(encrypted).decode("ascii")


def decrypt(encrypted: str, key: str | None = None) -> str:
    """Decrypt a string from base64-encoded ciphertext."""
    key_bytes = _get_key(key)
    data = base64.urlsafe_b64decode(encrypted.encode("ascii"))
    decrypted = _xor_bytes(data, key_bytes)
    return decrypted.decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a value using SECRET_KEY.")
    parser.add_argument(
        "--key",
        "-k",
        required=True,
        help="SECRET_KEY value used for encryption/decryption",
    )
    parser.add_argument(
        "--encrypt",
        "-e",
        action="store_true",
        help="Encrypt the value",
    )
    parser.add_argument(
        "--decrypt",
        "-d",
        action="store_true",
        help="Decrypt the value",
    )
    parser.add_argument(
        "value",
        help="Value to encrypt or decrypt",
    )
    args = parser.parse_args()

    if args.encrypt == args.decrypt:
        parser.error("Exactly one of --encrypt or --decrypt is required")

    try:
        if args.encrypt:
            print(encrypt(args.value, key=args.key))
        else:
            print(decrypt(args.value, key=args.key))
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
