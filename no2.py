import base64
import hashlib
import os

def generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang):
    # Hash the data
    data = f"{nomor_pengiriman}-{tanggal_kirim}-{kode_cabang}".encode()
    hash_data = hashlib.sha1(data).digest()

    # Generate the encryption key
    key = os.urandom(32)

    # Encrypt the data
    cipher = aes_ocb.new(key, hash_data)
    encrypted_data = cipher.encrypt(data)

    # Encode the encrypted data to base64
    encoded_data = base64.b64encode(encrypted_data).decode()

    return encoded_data


def main():
    # Get the data
    nomor_pengiriman = input("Masukkan Nomor Pengiriman: ")
    tanggal_kirim = input("Masukkan Tanggal Kirim: ")
    kode_cabang = input("Masukkan Kode Cabang Distributor: ")

    # Generate the barcode
    barcode = generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang)

    # Print the barcode
    print(barcode)


if __name__ == "__main__":
    main()
