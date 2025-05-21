import io
import pytest
from qr_utils import generate_qr

def test_generate_qr_default():
    text = "Hello QR"
    result = generate_qr(text)
    assert isinstance(result, io.BytesIO)
    assert result.getbuffer().nbytes > 0

def test_generate_qr_custom_params():
    text = "Тест цвета"
    bio = generate_qr(
        text,
        fill_color="red",
        back_color="yellow",
        size=400,
        fmt="jpeg"
    )
    assert isinstance(bio, io.BytesIO)
    assert bio.getbuffer().nbytes > 0
    assert bio.name == "qr.jpeg"
