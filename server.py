# -*- coding : utf=8 -*-
import io
from flask import Flask, jsonify, render_template, request
import torch
import torch.nn as nn
import torch.optim as optim

app = Flask(__name__)

PATH = "./model/fin_classification_model.pt"

torch.save(net.state_dict(), PATH)
model = Net()
model.load_state_dict(torch.load(PATH))
model.eval()

@app.route("/predict", method=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('ch_project_web.html')
#    if request.method == 'POST':


host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == '__main__':
    app.run(host=host_addr, port=port_num, debug=True)
