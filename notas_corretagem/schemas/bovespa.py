from ..extensions import ma
from ..models.bovespa import FolhasBovespa, NotasBovespa, OperaçõesBovespa


class NotasBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotasBovespa
        

class FolhasBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FolhasBovespa


class OperaçõesBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OperaçõesBovespa
