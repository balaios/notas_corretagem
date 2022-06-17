from ..extensions import ma
from ..models.bovespa import NotaBovespa, OperacaoBovespa


class NotaBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaBovespa


class OperacaoBovespaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OperacaoBovespa
