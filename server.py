# -*- coding : utf=8 -*-
import io
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import copy
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as Datasets
import matplotlib.pyplot as plt

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('ch_project_web_editing.html')

@app.route("/", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        x = request.files['fin-image']
        return render_template('ch_project_web_editing.html', result=20)

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == '__main__':
    app.run(host=host_addr, port=port_num, debug=True)
