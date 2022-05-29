from ..extensions import ma
from ..models.bmf import FolhaBmf, NotaBmf, OperacaoBmf


class NotaBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaBmf


class FolhaBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FolhaBmf


class OperacaoBmfSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OperacaoBmf
