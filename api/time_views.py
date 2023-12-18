from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from api import api
from . import time_schema
from . import time
from . import time_model
from . import time_service
import brasileirao

class TimeList(Resource):
    def get(self):
        times = time_service.listar_times()
        ts = time_schema.TimeSchema(many=True)
        return make_response(ts.jsonify(times), 200)
    
    def post(self):
        ts = time_schema.TimeSchema()

        df = brasileirao.tabela()
        
        for i in range(20):
            posicao = df['POS'][i]
            nome = df['Time'][i]
            pontos = df['PTS'][i]
            jogos = df['J'][i]
            vitorias = df['V'][i]
            empates = df['E'][i]
            derrotas = df['D'][i]
            gols_pro = df['GP'][i]
            gols_contra = df['GC'][i]
            saldo_gols = df['SG'][i]

            novo_time = time.Time(nome, posicao, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols)
            resultado = time_service.incluir_time(novo_time)
            x = ts.jsonify(resultado)

        times = time_service.listar_times()
        ts = time_schema.TimeSchema(many=True)
        return make_response(ts.jsonify(times), 200)

    def put(self):
        # time_bd = time_service.listar_posicao(posicao)
        # if time_bd is None:
        #     return make_response(jsonify("Posição não pertencente à tabela"))
        ts = time_schema.TimeSchema()

        df = brasileirao.tabela()

        for i in range(20):
            posicao = df['POS'][i]
            nome = df['Time'][i]
            pontos = df['PTS'][i]
            jogos = df['J'][i]
            vitorias = df['V'][i]
            empates = df['E'][i]
            derrotas = df['D'][i]
            gols_pro = df['GP'][i]
            gols_contra = df['GC'][i]
            saldo_gols = df['SG'][i]

            time_anterior = time_service.listar_posicao(posicao)
            novo_time = time.Time(nome, posicao, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols)
            time_service.atualizar_time(time_anterior, novo_time)

        tabela_atualizada = time_service.listar_times()
        ts = time_schema.TimeSchema(many=True)
        return make_response(ts.jsonify(tabela_atualizada), 200)

class TimePosicaoDetail(Resource):
    def get(self, posicao):
        time = time_service.listar_posicao(posicao)
        if time is None:
            return make_response(jsonify("Posição não pertencente a tabela"), 404)
        ts = time_schema.TimeSchema()
        return make_response(ts.jsonify(time), 200)
    
class TimeNomeDetail(Resource):
    def get(self, nome):
        time = time_service.listar_time_nome(nome)
        if time is None:
            return make_response(jsonify("Time não pertencente a competição"), 404)
        ts = time_schema.TimeSchema()
        return make_response(ts.jsonify(time), 200)

api.add_resource(TimeList, '/tabela-serie-a')
api.add_resource(TimePosicaoDetail, '/tabela-serie-a/pos/<posicao>')
api.add_resource(TimeNomeDetail, '/tabela-serie-a/time/<nome>')