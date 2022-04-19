from ..extensions import ma
from ..models.bmf import FolhasBmf, NotasBmf, OperaçõesBmf


class NotasBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotasBmf
        

class FolhasBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FolhasBmf


class OperaçõesBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OperaçõesBmf
        