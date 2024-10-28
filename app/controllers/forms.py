from config import *

from model.data.post import Post

from flask import request, url_for, redirect, render_template
from os import path

@cross_origin
@app.route('/search', methods=['GET', 'POST', 'OPTIONS'])
def search():
    rawTargets = request.form.get('targets')
    targets = rawTargets.split(' ')
    result = []
    posts = Post.getLastList()
    for post in posts:
        if min(list(map(lambda x: x.lower() in post.info.lower() or x in post.title.lower(), targets))):
            result.append(post)
    print('search finished')
    return render_template('news.html', lastPost=Post.getLast(), posts=list(result) )
    
            