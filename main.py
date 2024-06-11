import io
import streamlit as st
import qrcode
from PIL import Image

st.title("QR Code Generator")

input_URL = st.text_input("Enter the URL:")

if st.button("Generate QR Code"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(input_URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    st.image(img_bytes, caption="QR Code")

    st.success("QR Code Generated Successfully!")
