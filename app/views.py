from flask import Flask, render_template, request
from flask_cors import CORS
import qrcode
import base64
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from io import BytesIO

app = Flask(__name__)
cors = CORS(app, resources={r"/generate": {"origins": "*"}})


@app.route("/")
def home():
    return render_template("home.html", name="Emre Ateş")


@app.route("/generate", methods=['POST'])
def generate_qr_code():
    data = request.json
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(data["qrData"])
    qr.make(fit=True)
    if data["isTransparent"]:
        img = qr.make_image(fill_color=data["fillColor"])
    else:
        img = qr.make_image(
            fill_color=data["fillColor"], back_color=data["backgroundColor"])

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())

    return img_str.decode()
