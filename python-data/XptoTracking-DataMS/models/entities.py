from sqlalchemy.orm import relationship

from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class TelemetryData(db.Model):
    __tablename__ = "telemetryData"

    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True))  # , db.ForeignKey("vehicle.vehicle_id")
    data_hora = db.Column(db.DateTime)
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    altimeter = db.Column(db.Integer())
    telemetry_value = db.Column(db.Integer())
    tipo_sensor = db.Column(db.String(255))

    def get_id(self):
        return self.data_id

    def __init__(self, data_id, vehicle_id, data_hora, latitude, longitude, altimeter, telemetry_value, tipo_sensor):
        self.data_id = data_id
        self.vehicle_id = vehicle_id
        self.data_hora = data_hora
        self.latitude = latitude
        self.longitude = longitude
        self.altimeter = altimeter
        self.telemetry_value = telemetry_value
        self.tipo_sensor = tipo_sensor

    def __repr__(self):
        return 'TelemetryData(data_id=%d, vehicle_id=%s, data_hora=%s, latitude=%s, longitude=%s, altimeter=%s, ' \
               'telemetry_value=%s, tipo_sensor=%s)' % (self.data_id, self.vehicle_id, self.data_hora, self.latitude,
                                                        self.longitude, self.altimeter, self.telemetry_value,
                                                        self.tipo_sensor)

    def json(self):
        return {'data_id': self.data_id, 'vehicle_id': self.vehicle_id, 'data_hora': self.data_hora,
                'latitude': self.latitude, 'longitude': self.longitude, 'altimeter': self.altimeter,
                'telemetry_value': self.telemetry_value, 'tipo_sensor': self.tipo_sensor}
