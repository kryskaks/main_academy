from app import app
from flask import render_template, request, redirect, url_for

import funcs


@app.route("/")
def get_payments():
    if request.args:
        return render_template("payments.html", payments=funcs.get_filtered_payments(request.args))
    return render_template("payments.html", payments=funcs.get_all_payments())


@app.route("/new", methods=["GET", "POST"])
def create_payment():
    if request.method == "GET":
        return render_template("new_payment.html",
                               inputs=("name", "created", "amount", "currency"))
    new = funcs.create_new_payment(request.form)
    return redirect(url_for("get_payments", id=new.id))


@app.route("/api/new", methods=["POST"])
def create_api_payment():
    # json request
    return "in create_api_payment"
