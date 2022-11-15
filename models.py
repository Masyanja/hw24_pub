from typing import Iterable, Dict, Any

from flask_restx import ValidationError
from marshmallow import fields, Schema, validates_schema

VALID_CMD_PARAMS: Iterable[str] = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex'
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    # перед тем как запустить данные в схему, идет проверка
    # см документация маршмеллоу
    @validates_schema
    # Находятся параметры см выше и еще что-то
    def validate_cmd_params(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd1" contains invalid value')

        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
