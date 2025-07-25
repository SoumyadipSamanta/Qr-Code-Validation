import qrcode

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as '{filename}'")

if __name__ == "__main__":
    print("🔹 QR Code Generator")
    user_data = input("Enter the data (URL/Text/ID) to encode: ")
    file_name = input("Enter filename to save (e.g., myqr.png): ")
    generate_qr(user_data, file_name)
