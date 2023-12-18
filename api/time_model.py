from api import db

class Time(db.Model):
    __tablename__= "time"
    posicao = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    pontos = db.Column(db.String(2), nullable=False)
    jogos = db.Column(db.String(2), nullable=False)
    vitorias = db.Column(db.String(2), nullable=False)
    empates = db.Column(db.String(2), nullable=False)
    derrotas = db.Column(db.String(2), nullable=False)
    gols_pro = db.Column(db.String(2), nullable=False)
    gols_contra = db.Column(db.String(2), nullable=False)
    saldo_gols = db.Column(db.String(3), nullable=False)
