from app import app
from flask import render_template, request, jsonify
from app.cvtools import CvTools
import numpy as np

@app.route("/<name>")
def index(name):
    return f"Bismillah {name}"


@app.route("/set-img")
def set_img():
    return render_template('set-img.html')


@app.route("/api/set-img", methods=['POST'])
def api_set_img():
    print("Proses")
    try:
        # Terima data gambar dari frontend
        img_data = request.get_data()
        img_array = np.frombuffer(img_data, np.uint8)
        # Baca gambar menggunakan OpenCV

        if CvTools().add_dataset('uki',img_array):
            print("Save img")
        else:
            print("Gagal Save")
        # Kirim respons
        response_data = {'status': 'success', 'message': 'Image capture received and processed'}
        return jsonify(response_data)

    except Exception as e:
        # Tangani kesalahan jika terjadi
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data)