from flask_marshmallow.fields import fields

from config import ma
from models.entities import TelemetryData


class TelemetryDataSchema(ma.SQLAlchemyAutoSchema):
    dataId = fields.String(attribute="data_id")

    class Meta:
        model = TelemetryData
        load_instance = True
        exclude = ["data_id"]
