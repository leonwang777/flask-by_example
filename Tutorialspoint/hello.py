from flask import Flask

app = Flask(__name__)


@app.route('/blog/<int:postID>')
def ShowBlog(postID):
    return 'Blog number:  %d'  % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision number:  %f'  % revNo

if __name__ == '__main__':
    app.run(debug=True)