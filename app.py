# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from model_file import *
from whale_title import *

model.load_state_dict(torch.load('./model/VGG-whaleFin_ImageClassification_model.pt',map_location ='cpu'))
model.eval()

# Define a flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html", predictions=" ")


@app.route('/uploader', methods = ['POST'])
def upload_file():
    predictions=""
    explain=""
    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static','uploads', secure_filename(f.filename))
        f.save(file_path)

        x = pil_loader(file_path)
        x = transform(x)
        x = x.unsqueeze(0)
        x = x.to(device)
        y_pred, _ = model(x)
        y_prob = F.softmax(y_pred, dim = -1)
        top_pred = y_prob.argmax(1, keepdim = True)
        top_pred = top_pred.cpu()
        classes = ['blue_whale',
                'brydes_whale',
                'cuviers_beaked_whale',
                'false_killer_whale',
                'fin_whale', 'gray_whale',
                'humpback_whale', 'killer_whale',
                'long_finned_pilot_whale',
                'melon_headed_whale',
                'minke_whale',
                'pygmy_killer_whale',
                'sei_whale',
                'short_finned_pilot_whale',
                'southern_right_whale']
        name = name_title(classes[top_pred])        
        explain = switch(classes[top_pred])

    return render_template("index1.html", predictions = name, explain = explain, image_name = classes[top_pred]) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port="4100")
