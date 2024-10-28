from config import *

from model.data.post import Post

from flask import request, url_for, redirect, render_template
from os import path

@app.route('/main', methods=['GET'])
def getMain():
    return render_template('main.html', lastPost=Post.getLast()) 


@app.route('/newPost', methods=['GET'])
@login_required
def newPostPage():
    return render_template('newPost.html', lastPost=Post.getLast()) 

# @app.route('/post', methods=['GET'])
# def getPsot():
#     return render_template('post.html') 

@app.route('/news', methods=['GET'])
def getNews():
    return render_template('news.html', lastPost=Post.getLast(), posts = list(Post.getLastList())) 

@app.route('/post', methods=['GET'])
def getPost():
    id = int(request.args['id'])
    return render_template('post.html', lastPost=Post.getLast(), post = Post.getByID(id)) 