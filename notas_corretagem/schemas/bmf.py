from ..extensions import ma
from ..models.bmf import NotaBmf, OperacaoBmf


class NotaBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaBmf


class OperacaoBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OperacaoBmf
