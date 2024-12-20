from flask import Flask, render_template, request, redirect, url_for
from models import db, Material, Partner
import webbrowser
import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    materials = Material.query.all()
    return render_template('materials.html', materials=materials)

@app.route('/add', methods=['GET', 'POST'])
def add_material():
    if request.method == 'POST':
        name = request.form['name']
        material_type = request.form['type']
        quantity = request.form['quantity']
        min_quantity = request.form['min_quantity']
        price = request.form['price']
        
        new_material = Material(name=name, type=material_type, quantity=quantity, min_quantity=min_quantity, price=price)
        db.session.add(new_material)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_material.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_material(id):
    material = Material.query.get_or_404(id)
    if request.method == 'POST':
        material.name = request.form['name']
        material.type = request.form['type']
        material.quantity = request.form['quantity']
        material.min_quantity = request.form['min_quantity']
        material.price = request.form['price']
        
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit_material.html', material=material)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_material(id):
    material = Material.query.get_or_404(id)
    db.session.delete(material)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/partners')
def index_partners():
    partners = Partner.query.all()
    return render_template('partners.html', partners=partners)

@app.route('/partners/add', methods=['GET', 'POST'])
def add_partner():
    if request.method == 'POST':
        name = request.form['name']
        contact_info = request.form['contact_info']
        
        new_partner = Partner(name=name, contact_info=contact_info)
        db.session.add(new_partner)
        db.session.commit()
        return redirect(url_for('index_partners'))
    
    return render_template('add_partner.html')

@app.route('/partners/edit/<int:id>', methods=['GET', 'POST'])
def edit_partner(id):
    partner = Partner.query.get_or_404(id)
    if request.method == 'POST':
        partner.name = request.form['name']
        partner.contact_info = request.form['contact_info']
        
        db.session.commit()
        return redirect(url_for('index_partners'))
    
    return render_template('edit_partner.html', partner=partner)

@app.route('/partners/delete/<int:id>', methods=['POST'])
def delete_partner(id):
    partner = Partner.query.get_or_404(id)
    db.session.delete(partner)
    db.session.commit()
    return redirect(url_for('index_partners'))

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)