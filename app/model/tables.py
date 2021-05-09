from app import db

class Student(db.Model):
    __tablename__ = "tbstudents"
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeAluno = db.Column(db.String(60))
    emailAluno = db.Column(db.String(50))
    logradouro = db.Column(db.String(50))
    numero = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    complemento = db.Column(db.String(60))

    def __init__(self, nomeAluno, emailAluno, numero, cep, logradouro, complemento):
        self.nomeAluno = nomeAluno
        self.emailAluno = emailAluno
        self.numero = numero
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento