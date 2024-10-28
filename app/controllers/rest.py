from config import *
from flask import request, url_for, redirect, send_file
from flask_cors import cross_origin

from model.data.image import *
from model.data.post import *
from model.tools.FileUtil import *

from werkzeug.wsgi import wrap_file
import cv2
import numpy as np

@cross_origin
@login_required
@app.route('/savePost', methods=['GET', 'POST', 'OPTIONS'])
def savePost(): 
    title = request.form.get('title')
    info = request.form.get('text')
    if title and info:
        post=Post(request.form.get('title'), request.form.get('text'))
        post.save()
        
        for file in request.files:
            img = cv2.imdecode(np.fromstring(request.files[file].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            bData = FileUtil.convertImageToBytes(img)
            Image(data=bData, post=post).save()
    
        return 'ok'
    return 'Не заполнены поля', 200