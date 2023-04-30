from gql.transport.exceptions import TransportQueryError
import typing


class UserIsPrivate(TransportQueryError):
    
    def __init__(self, msg: typing.Optional[str] = None, query_id: typing.Optional[int] = None, errors:  typing.Optional[typing.List[typing.Any]] = None, data: typing.Optional[typing.Any] = None, extensions: typing.Optional[typing.Any] = None):
        default_msg = "The user's Eva profile is set to private! It must be public."
        super().__init__(msg or default_msg, query_id, errors, data, extensions)


class UserNotFound(TransportQueryError):
    
    def __init__(self, msg: typing.Optional[str] = None, query_id: typing.Optional[int] = None, errors:  typing.Optional[typing.List[typing.Any]] = None, data: typing.Optional[typing.Any] = None, extensions: typing.Optional[typing.Any] = None):
        default_msg = "Player Eva doesn't exist."
        super().__init__(msg or default_msg, query_id, errors, data, extensions)
