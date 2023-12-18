from . import time_model
from api import db

def incluir_time(time):
    time_bd = time_model.Time(posicao=time.posicao, nome=time.nome, pontos=time.pontos, jogos=time.jogos, vitorias=time.vitorias, empates=time.empates, derrotas=time.derrotas, gols_pro=time.gols_pro, gols_contra=time.gols_contra, saldo_gols=time.saldo_gols)
    db.session.add(time_bd)
    db.session.commit()
    return time_bd

def listar_times():
    times = time_model.Time.query.all()
    return times

def listar_time_nome(nome):
    time = time_model.Time.query.filter_by(nome=nome).first()
    return time

def listar_posicao(posicao):
    time = time_model.Time.query.filter_by(posicao=posicao).first()
    return time

def atualizar_time(anterior, novo):
    anterior.posicao = novo.posicao
    anterior.nome = novo.nome
    anterior.pontos = novo.pontos
    anterior.jogos = novo.jogos
    anterior.vitorias = novo.vitorias
    anterior.empates = novo.empates
    anterior.derrotas = novo.derrotas
    anterior.gols_pro = novo.gols_pro
    anterior.gols_contra = novo.gols_contra
    anterior.saldo_gols = novo.saldo_gols
    db.session.commit()
