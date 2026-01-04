from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import Inventory
from extensions import db

inventory_bp = Blueprint('inventory', __name__)

# LIST
@inventory_bp.route('/', methods=['GET'])
@login_required
def list_inventory():
    """
    Tampilkan semua inventory.
    Template: templates/inventory/list.html
    """
    inventories = Inventory.query.order_by(Inventory.id.desc()).all()
    return render_template('inventory/list.html', inventories=inventories)

# ADD
@inventory_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_inventory():
    """
    Form tambah barang. GET -> tampil form. POST -> simpan ke DB.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        stock = request.form.get('stock', type=int)
        price = request.form.get('price', type=float)

        if not name:
            flash("Nama barang wajib diisi.", "warning")
            return redirect(url_for('inventory.add_inventory'))

        item = Inventory(name=name, stock=stock or 0, price=price or 0.0)
        db.session.add(item)
        db.session.commit()
        flash(f"Barang '{name}' berhasil ditambahkan.", "success")
        return redirect(url_for('inventory.list_inventory'))

    return render_template('inventory/add.html')

# EDIT
@inventory_bp.route('/edit/<int:inventory_id>', methods=['GET', 'POST'])
@login_required
def edit_inventory(inventory_id):
    """
    Edit barang berdasarkan ID. GET -> tampil form terisi.
    POST -> update data ke DB.
    """
    item = Inventory.query.get_or_404(inventory_id)

    if request.method == 'POST':
        item.name = request.form.get('name')
        item.stock = request.form.get('stock', type=int)
        item.price = request.form.get('price', type=float)

        db.session.commit()
        flash(f"Barang '{item.name}' berhasil diupdate.", "success")
        return redirect(url_for('inventory.list_inventory'))

    return render_template('inventory/edit.html', item=item)

# DELETE
@inventory_bp.route('/delete/<int:inventory_id>', methods=['GET'])
@login_required
def delete_inventory(inventory_id):
    """
    Hapus barang. Untuk latihan kita terima GET agar link langsung bekerja.
    Di produksi: ganti ke POST dan gunakan CSRF.
    """
    item = Inventory.query.get_or_404(inventory_id)
    name = item.name
    db.session.delete(item)
    db.session.commit()
    flash(f"Barang '{name}' berhasil dihapus.", "success")
    return redirect(url_for('inventory.list_inventory'))

