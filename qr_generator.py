import qrcode
from PIL import Image

class QRGenerator:
    def __init__(self, save_path: str):
        self.save_path = save_path

    def generate_qr(self, link: str, filename: str):
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            file_path = f"{self.save_path}/{filename}.png"
            img.save(file_path)
            return file_path
        except Exception as e:
            raise RuntimeError(f"Error generating QR Code: {e}")
