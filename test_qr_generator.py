import unittest
from modules.qr_generator import QRGenerator

class TestQRGenerator(unittest.TestCase):
    def test_generate_qr(self):
        qr_generator = QRGenerator("output")
        file_path = qr_generator.generate_qr("https://example.com", "test")
        self.assertTrue(file_path.endswith(".png"))

if __name__ == "__main__":
    unittest.main()
