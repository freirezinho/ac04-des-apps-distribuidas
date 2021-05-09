from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.model.tables import Student

@app.route("/")
def index():
    students = Student.query.all()
    return render_template(
        "index.html",
        students=students
        )

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        student = Student(request.form['nome'],
                          request.form['email'],
                          request.form['numero'],
                          request.form['cep'],
                          request.form['logradouro'],
                          request.form['complemento']
                          )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")

@app.route("/edit/<int:ra>", methods=['GET', 'POST'])
def edit(ra):
    student = Student.query.get(ra)
    if request.method == 'POST':
        student.ra = request.form['ra']
        student.nomeAluno = request.form['nome']
        student.emailAluno = request.form['email']
        student.numero = request.form['numero']
        student.cep = request.form['cep']
        student.logradouro = request.form['logradouro']
        student.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", student = student)   
 
@app.route("/delete/<int:ra>")
def delete(ra):
    student = Student.query.get(ra)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))