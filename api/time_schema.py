from api import ma
from . import time_model
from marshmallow import fields

class TimeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = time_model.Time
        load_instance = True
        fields = ('posicao', 'nome', 'pontos', 'jogos', 'vitorias', 'empates', 'derrotas', 'gols_pro', 'gols_contra', 'saldo_gols')

    posicao = fields.Integer(strict=True)
    nome = fields.String(required=True)
    pontos = fields.String(required=True)
    jogos = fields.String(required=True)
    vitorias = fields.String(required=True)
    empates = fields.String(required=True)
    derrotas = fields.String(required=True)
    gols_pro = fields.String(required=True)
    gols_contra = fields.String(required=True)
    saldo_gols = fields.String(required=True)