import connexion
import json

from models.entities import TelemetryData
from services.services import TelemetryDataService
from schemas.schemas import TelemetryDataSchema
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError

from swagger_server.models.create_telemetry_data_request import CreateTelemetryDataRequest  # noqa: E501
from swagger_server.models.create_telemetry_data_response import CreateTelemetryDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_telemetry_data_response import GetTelemetryDataResponse  # noqa: E501
from swagger_server.models.update_telemetry_data_request import UpdateTelemetryDataRequest  # noqa: E501
from swagger_server.models.list_telemetry_data_response import ListTelemetryDataResponse  # noqa: E501

telemetry_data_service = TelemetryDataService()
telemetry_data_schema = TelemetryDataSchema()


def create_telemetry_data(body):  # noqa: E501
    """Create Telemetry data tracking

    This operation is used to create new a telemetry data tracking. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateTelemetryDataResponse
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateTelemetryDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = TelemetryData(data_id=None, vehicle_id=body.vehicle_id, data_hora=body.data_hora,
                               latitude=body.latitude, longitude=body.longitude, altimeter=body.altimeter,
                               telemetry_value=body.telemetry_value, tipo_sensor=body.tipo_sensor)
        entity = telemetry_data_service.save(entity)
        response = CreateTelemetryDataResponse.from_dict(json.loads(telemetry_data_schema.dumps(entity)))
        response_code = 201

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new TelemetryData", details=str(e))

    return response.to_dict(), response_code


def delete_telemetry_data(data_id):  # noqa: E501
    """Delete Telemetry data tracking

    This operation is used to delete a specific telemetry data. # noqa: E501

    :param data_id: Unique identifier of the Telemetry Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        entity = telemetry_data_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="TelemetryData not found",
                                 details=f"Unable to find data ID {data_id}")
        telemetry_data_service.delete(data_id)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code


def get_telemetry_data(data_id):  # noqa: E501
    """Get a single telemetry Data info

    This operation is used to retrieve the details of a specific telemetry data. # noqa: E501

    :param data_id: Unique identifier of the Telemetry Data in the database
    :type data_id: dict | bytes

    :rtype: GetTelemetryDataResponse
    """
    response = None
    response_code = None
    try:
        entity = telemetry_data_service.fetch_by_id(entity_id=data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="TelemetryData not found",
                                 details=f"Unable to find data ID {data_id}")
        response = GetTelemetryDataResponse.from_dict(json.loads(telemetry_data_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_telemetry_data():  # noqa: E501
    """Retrieve a list of telemetry data sended

    Retrieve a list of telemetry data # noqa: E501


    :rtype: List[GetTelemetryDataResponse]
    """
    entities = telemetry_data_service.fetch_all()

    telemetry_data_response_list = []
    for entity in entities:
        telemetry_data_response_list.append(
            GetTelemetryDataResponse.from_dict(json.loads(telemetry_data_schema.dumps(entity))))

    response = ListTelemetryDataResponse(content=telemetry_data_response_list,
                                         total_results=len(telemetry_data_response_list))
    return response.to_dict(), 200


def update_telemetry_data(body, data_id):  # noqa: E501
    """Update Telemetry data tracking

    This operation is used to update the details of a specific telemetry data. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param data_id: Unique identifier of the Telemetry Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = UpdateTelemetryDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = telemetry_data_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Telemetry Data not found",
                                 details=f"Unable to find data ID {data_id}")

        entity.vehicle_id = body.vehicle_id
        entity.data_hora = body.data_hora
        entity.latitude = body.latitude
        entity.longitude = body.longitude
        entity.altimeter = body.altimeter
        entity.telemetry_value = body.telemetry_value
        entity.tipo_sensor = body.tipo_sensor

        telemetry_data_service.save(entity)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))

    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code
