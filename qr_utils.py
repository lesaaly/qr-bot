import qrcode
import io

def generate_qr(data, fill_color='black', back_color='white', size=300, fmt='PNG'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    img = img.resize((size, size))
    bio = io.BytesIO()
    img.save(bio, fmt.upper())
    bio.name = f'qr.{fmt.lower()}'
    bio.seek(0)
    return bio