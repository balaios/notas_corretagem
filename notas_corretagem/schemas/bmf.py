from ..extensions import ma
from ..models.bmf import Folhasbmf, Notasbmf, Operaçõesbmf


class NotasbmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notasbmf
        

class FolhasbmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Folhasbmf


class OperaçõesbmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Operaçõesbmf
        