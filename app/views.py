from flask import render_template
from . import app

#HOME{{{
@app.route('/')
@app.route('/en')
def home_en():
    return render_template('home_en.html')
@app.route('/cn')
def home_cn():
    return render_template('home_cn.html')
@app.route('/fr')
def home_fr():
    return render_template('home_fr.html')
#}}}
#CLASSES{{{
@app.route('/en/classes')
def classes_en():
    return render_template('classes_en.html')
@app.route('/cn/classes')
def classes_cn():
    return render_template('classes_cn.html')
@app.route('/fr/classes')
def classes_fr():
    return render_template('classes_fr.html')
#}}}
#TRANSLATION{{{
@app.route('/en/translation')
def translation_en():
    return render_template('translation_en.html')
@app.route('/cn/translation')
def translation_cn():
    return render_template('translation_cn.html')
@app.route('/fr/translation')
def translation_fr():
    return render_template('translation_fr.html')
#}}}
#SERVICES{{{
@app.route('/en/services')
def services_en():
    return render_template('services_en.html')
@app.route('/cn/services')
def services_cn():
    return render_template('services_cn.html')
@app.route('/fr/services')
def services_fr():
    return render_template('services_fr.html')
#}}}
#BLOG{{{
@app.route('/en/blog')
def blog_en():
    return render_template('blog/blog_en.html')
@app.route('/cn/blog')
def blog_cn():
    return render_template('blog/blog_cn.html')
@app.route('/fr/blog')
def blog_fr():
    return render_template('blog/blog_fr.html')
@app.route('/fr/blog/vowels')
def vowels():
    return render_template('blog/vowels_fr.html')
#}}}
