import cv2

def read_qr_code(image_path):
    detector = cv2.QRCodeDetector()
    img = cv2.imread(image_path)
    data, _, _ = detector.detectAndDecode(img)
    return data

def load_trusted_data(file_path='trusted_data.txt'):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f.readlines())

def check_if_valid(data, trusted_list):
    if data in trusted_list:
        print(f"✅ VALID QR Code: {data}")
    elif data == "":
        print("⚠️ QR Code could not be read or is empty.")
    else:
        print(f"❌ FAKE QR Code: {data}")

if __name__ == "__main__":
    image_file = input("Enter the QR image filename (e.g., myqr.png): ")
    trusted_data = load_trusted_data()
    qr_data = read_qr_code(image_file)
    check_if_valid(qr_data, trusted_data)
