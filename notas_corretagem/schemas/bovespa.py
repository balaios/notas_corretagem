from ..extensions import ma
from ..models.bovespa import Folhasbovespa, Notasbovespa, Operaçõesbovespa


class NotasbovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notasbovespa
        

class FolhasbovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Folhasbovespa


class OperaçõesbovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Operaçõesbovespa
