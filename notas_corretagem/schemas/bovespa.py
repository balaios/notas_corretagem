from ..extensions import ma
from ..models.bovespa import FolhaBovespa, NotaBovespa, OperacaoBovespa


class NotaBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaBovespa


class FolhaBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FolhaBovespa


class OperacaoBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OperacaoBovespa
