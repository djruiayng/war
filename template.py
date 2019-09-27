from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
import sys
import logging
import json
import requests

class LiffErrorCode(object):
    INVALID_REQUEST = 1
    UNAUTHORIZED = 2
    CONSENT_REQUIRED = 3
    VERSION_UPDATE_REQUIRED = 4
    SERVER_ERROR = 100

    _VALUES_TO_NAMES = {
        1: "INVALID_REQUEST",
        2: "UNAUTHORIZED",
        3: "CONSENT_REQUIRED",
        4: "VERSION_UPDATE_REQUIRED",
        100: "SERVER_ERROR",
    }

    _NAMES_TO_VALUES = {
        "INVALID_REQUEST": 1,
        "UNAUTHORIZED": 2,
        "CONSENT_REQUIRED": 3,
        "VERSION_UPDATE_REQUIRED": 4,
        "SERVER_ERROR": 100,
    }


class LiffFeatureType(object):
    GEOLOCATION = 1
    ADVERTISING_ID = 2
    BLUETOOTH_LE = 3

    _VALUES_TO_NAMES = {
        1: "GEOLOCATION",
        2: "ADVERTISING_ID",
        3: "BLUETOOTH_LE",
    }

    _NAMES_TO_VALUES = {
        "GEOLOCATION": 1,
        "ADVERTISING_ID": 2,
        "BLUETOOTH_LE": 3,
    }

class LiffErrorConsentRequired(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'consentUrl', 'UTF8', None, ),  # 2
    )
    
    def __init__(self, channelId=None, consentUrl=None,):
        self.channelId = channelId
        self.consentUrl = consentUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.consentUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffErrorConsentRequired')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.consentUrl is not None:
            oprot.writeFieldBegin('consentUrl', TType.STRING, 2)
            oprot.writeString(self.consentUrl.encode('utf-8') if sys.version_info[0] == 2 else self.consentUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffErrorPayload(object):
    
    thrift_spec = (
        None,  # 0
        None,  # 1
        None,  # 2
        (3, TType.STRUCT, 'consentRequired', [LiffErrorConsentRequired, None], None, ),  # 3
    )
    
    def __init__(self, consentRequired=None,):
        self.consentRequired = consentRequired

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 3:
                if ftype == TType.STRUCT:
                    self.consentRequired = LiffErrorConsentRequired()
                    self.consentRequired.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffErrorPayload')
        if self.consentRequired is not None:
            oprot.writeFieldBegin('consentRequired', TType.STRUCT, 3)
            self.consentRequired.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffException(TException):
    
    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'code', None, None, ),  # 1
        (2, TType.STRING, 'message', 'UTF8', None, ),  # 2
        (3, TType.STRUCT, 'payload', [LiffErrorPayload, None], None, ),  # 3
    )

    def __init__(self, code=None, message=None, payload=None,):
        self.code = code
        self.message = message
        self.payload = payload

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.payload = LiffErrorPayload()
                    self.payload.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffException')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 2)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        if self.payload is not None:
            oprot.writeFieldBegin('payload', TType.STRUCT, 3)
            self.payload.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffChatContext(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'chatMid', 'UTF8', None, ),  # 1
    )

    def __init__(self, chatMid=None,):
        self.chatMid = chatMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.chatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffChatContext')
        if self.chatMid is not None:
            oprot.writeFieldBegin('chatMid', TType.STRING, 1)
            oprot.writeString(self.chatMid.encode('utf-8') if sys.version_info[0] == 2 else self.chatMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
        
class LiffNoneContext(object):

    thrift_spec = ()
    
    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffNoneContext')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffSquareChatContext(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'squareChatMid', 'UTF8', None, ),  # 1
    )
    
    def __init__(self, squareChatMid=None,):
        self.squareChatMid = squareChatMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.squareChatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffSquareChatContext')
        if self.squareChatMid is not None:
            oprot.writeFieldBegin('squareChatMid', TType.STRING, 1)
            oprot.writeString(self.squareChatMid.encode('utf-8') if sys.version_info[0] == 2 else self.squareChatMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffContext(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'none', [LiffNoneContext, None], None, ),  # 1
        (2, TType.STRUCT, 'chat', [LiffChatContext, None], None, ),  # 2
        (3, TType.STRUCT, 'squareChat', [LiffSquareChatContext, None], None, ),  # 3
    )

    def __init__(self, none=None, chat=None, squareChat=None,):
        self.none = none
        self.chat = chat
        self.squareChat = squareChat

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.none = LiffNoneContext()
                    self.none.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.chat = LiffChatContext()
                    self.chat.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.squareChat = LiffSquareChatContext()
                    self.squareChat.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffContext')
        if self.none is not None:
            oprot.writeFieldBegin('none', TType.STRUCT, 1)
            self.none.write(oprot)
            oprot.writeFieldEnd()
        if self.chat is not None:
            oprot.writeFieldBegin('chat', TType.STRUCT, 2)
            self.chat.write(oprot)
            oprot.writeFieldEnd()
        if self.squareChat is not None:
            oprot.writeFieldBegin('squareChat', TType.STRUCT, 3)
            self.squareChat.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffView(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'type', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'url', 'UTF8', None, ),  # 2
        None,  # 3
        (4, TType.I32, 'titleTextColor', None, None, ),  # 4
        (5, TType.I32, 'titleBackgroundColor', None, None, ),  # 5
        (6, TType.STRING, 'titleIconUrl', 'UTF8', None, ),  # 6
        (7, TType.I32, 'titleSubtextColor', None, None, ),  # 7
        (8, TType.I32, 'titleButtonColor', None, None, ),  # 8
        (9, TType.I32, 'progressBarColor', None, None, ),  # 9
        (10, TType.I32, 'progressBackgroundColor', None, None, ),  # 10
        (11, TType.BOOL, 'trustedDomain', None, None, ),  # 11
    )
    
    def __init__(self, type=None, url=None, trustedDomain=None, titleIconUrl=None, titleTextColor=None, titleSubtextColor=None, titleButtonColor=None, titleBackgroundColor=None, progressBarColor=None, progressBackgroundColor=None,):
        self.type = type
        self.url = url
        self.trustedDomain = trustedDomain
        self.titleIconUrl = titleIconUrl
        self.titleTextColor = titleTextColor
        self.titleSubtextColor = titleSubtextColor
        self.titleButtonColor = titleButtonColor
        self.titleBackgroundColor = titleBackgroundColor
        self.progressBarColor = progressBarColor
        self.progressBackgroundColor = progressBackgroundColor

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.type = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.url = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.BOOL:
                    self.trustedDomain = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.titleIconUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.titleTextColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.titleSubtextColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.titleButtonColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.titleBackgroundColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.progressBarColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.progressBackgroundColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffView')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.STRING, 1)
            oprot.writeString(self.type.encode('utf-8') if sys.version_info[0] == 2 else self.type)
            oprot.writeFieldEnd()
        if self.url is not None:
            oprot.writeFieldBegin('url', TType.STRING, 2)
            oprot.writeString(self.url.encode('utf-8') if sys.version_info[0] == 2 else self.url)
            oprot.writeFieldEnd()
        if self.titleTextColor is not None:
            oprot.writeFieldBegin('titleTextColor', TType.I32, 4)
            oprot.writeI32(self.titleTextColor)
            oprot.writeFieldEnd()
        if self.titleBackgroundColor is not None:
            oprot.writeFieldBegin('titleBackgroundColor', TType.I32, 5)
            oprot.writeI32(self.titleBackgroundColor)
            oprot.writeFieldEnd()
        if self.titleIconUrl is not None:
            oprot.writeFieldBegin('titleIconUrl', TType.STRING, 6)
            oprot.writeString(self.titleIconUrl.encode('utf-8') if sys.version_info[0] == 2 else self.titleIconUrl)
            oprot.writeFieldEnd()
        if self.titleSubtextColor is not None:
            oprot.writeFieldBegin('titleSubtextColor', TType.I32, 7)
            oprot.writeI32(self.titleSubtextColor)
            oprot.writeFieldEnd()
        if self.titleButtonColor is not None:
            oprot.writeFieldBegin('titleButtonColor', TType.I32, 8)
            oprot.writeI32(self.titleButtonColor)
            oprot.writeFieldEnd()
        if self.progressBarColor is not None:
            oprot.writeFieldBegin('progressBarColor', TType.I32, 9)
            oprot.writeI32(self.progressBarColor)
            oprot.writeFieldEnd()
        if self.progressBackgroundColor is not None:
            oprot.writeFieldBegin('progressBackgroundColor', TType.I32, 10)
            oprot.writeI32(self.progressBackgroundColor)
            oprot.writeFieldEnd()
        if self.trustedDomain is not None:
            oprot.writeFieldBegin('trustedDomain', TType.BOOL, 11)
            oprot.writeBool(self.trustedDomain)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class LiffViewRequest(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'liffId', 'UTF8', None, ),  # 1
        (2, TType.STRUCT, 'context', [LiffContext, None], None, ),  # 2
    )
    
    def __init__(self, liffId=None, context=None,):
        self.liffId = liffId
        self.context = context

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.liffId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.context = LiffContext()
                    self.context.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffViewRequest')
        if self.liffId is not None:
            oprot.writeFieldBegin('liffId', TType.STRING, 1)
            oprot.writeString(self.liffId.encode('utf-8') if sys.version_info[0] == 2 else self.liffId)
            oprot.writeFieldEnd()
        if self.context is not None:
            oprot.writeFieldBegin('context', TType.STRUCT, 2)
            self.context.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()


class LiffViewResponse(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'view', [LiffView, None], None, ),  # 1
        (2, TType.STRING, 'contextToken', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'accessToken', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'featureToken', 'UTF8', None, ),  # 4
        (5, TType.LIST, 'features', (TType.I32, None, False), None, ),  # 5
        (6, TType.STRING, 'channelId', 'UTF8', None, ),  # 6
    )
    
    def __init__(self, view=None, contextToken=None, accessToken=None, featureToken=None, features=None, channelId=None,):
        self.view = view
        self.contextToken = contextToken
        self.accessToken = accessToken
        self.featureToken = featureToken
        self.features = features
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.view = LiffView()
                    self.view.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.contextToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.accessToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.featureToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.features = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI32()
                        self.features.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LiffViewResponse')
        if self.view is not None:
            oprot.writeFieldBegin('view', TType.STRUCT, 1)
            self.view.write(oprot)
            oprot.writeFieldEnd()
        if self.contextToken is not None:
            oprot.writeFieldBegin('contextToken', TType.STRING, 2)
            oprot.writeString(self.contextToken.encode('utf-8') if sys.version_info[0] == 2 else self.contextToken)
            oprot.writeFieldEnd()
        if self.accessToken is not None:
            oprot.writeFieldBegin('accessToken', TType.STRING, 3)
            oprot.writeString(self.accessToken.encode('utf-8') if sys.version_info[0] == 2 else self.accessToken)
            oprot.writeFieldEnd()
        if self.featureToken is not None:
            oprot.writeFieldBegin('featureToken', TType.STRING, 4)
            oprot.writeString(self.featureToken.encode('utf-8') if sys.version_info[0] == 2 else self.featureToken)
            oprot.writeFieldEnd()
        if self.features is not None:
            oprot.writeFieldBegin('features', TType.LIST, 5)
            oprot.writeListBegin(TType.I32, len(self.features))
            for iter6 in self.features:
                oprot.writeI32(iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 6)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class issueLiffView_args(object):
    
    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'request', [LiffViewRequest, None], None, ),  # 1
    )

    def __init__(self, request=None,):
        self.request = request

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueLiffView_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 1)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class issueLiffView_result(object):
    
    thrift_spec = (
        (0, TType.STRUCT, 'success', [LiffViewResponse, None], None, ),  # 0
        (1, TType.STRUCT, 'e', [LiffException, None], None, ),  # 1
    )

    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = LiffViewResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = LiffException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

class Product(object):

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'productId', 'UTF8', None, ),  # 1
        (2, TType.I64, 'packageId', None, None, ),  # 2
        (3, TType.I32, 'version', None, None, ),  # 3
        (4, TType.STRING, 'authorName', 'UTF8', None, ),  # 4
        (5, TType.BOOL, 'onSale', None, None, ),  # 5
        (6, TType.I32, 'validDays', None, None, ),  # 6
        (7, TType.I32, 'saleType', None, None, ),  # 7
        (8, TType.STRING, 'copyright', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'title', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'descriptionText', 'UTF8', None, ),  # 10
        (11, TType.I64, 'shopOrderId', None, None, ),  # 11
        (12, TType.STRING, 'fromMid', 'UTF8', None, ),  # 12
        (13, TType.STRING, 'toMid', 'UTF8', None, ),  # 13
        (14, TType.I64, 'validUntil', None, None, ),  # 14
        (15, TType.I32, 'priceTier', None, None, ),  # 15
        (16, TType.STRING, 'price', 'UTF8', None, ),  # 16
        (17, TType.STRING, 'currency', 'UTF8', None, ),  # 17
        (18, TType.STRING, 'currencySymbol', 'UTF8', None, ),  # 18
        (19, TType.I32, 'paymentType', None, None, ),  # 19
        (20, TType.I64, 'createDate', None, None, ),  # 20
        (21, TType.BOOL, 'ownFlag', None, None, ),  # 21
        (22, TType.I32, 'eventType', None, None, ),  # 22
        (23, TType.STRING, 'urlSchema', 'UTF8', None, ),  # 23
        (24, TType.STRING, 'downloadUrl', 'UTF8', None, ),  # 24
        (25, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 25
        (26, TType.I64, 'publishSince', None, None, ),  # 26
        (27, TType.BOOL, 'newFlag', None, None, ),  # 27
        (28, TType.BOOL, 'missionFlag', None, None, ),  # 28
    )

    def __init__(self, productId=None, packageId=None, version=None, authorName=None, onSale=None, validDays=None, saleType=None, copyright=None, title=None, descriptionText=None, shopOrderId=None, fromMid=None, toMid=None, validUntil=None, priceTier=None, price=None, currency=None, currencySymbol=None, paymentType=None, createDate=None, ownFlag=None, eventType=None, urlSchema=None, downloadUrl=None, buddyMid=None, publishSince=None, newFlag=None, missionFlag=None,):
        self.productId = productId
        self.packageId = packageId
        self.version = version
        self.authorName = authorName
        self.onSale = onSale
        self.validDays = validDays
        self.saleType = saleType
        self.copyright = copyright
        self.title = title
        self.descriptionText = descriptionText
        self.shopOrderId = shopOrderId
        self.fromMid = fromMid
        self.toMid = toMid
        self.validUntil = validUntil
        self.priceTier = priceTier
        self.price = price
        self.currency = currency
        self.currencySymbol = currencySymbol
        self.paymentType = paymentType
        self.createDate = createDate
        self.ownFlag = ownFlag
        self.eventType = eventType
        self.urlSchema = urlSchema
        self.downloadUrl = downloadUrl
        self.buddyMid = buddyMid
        self.publishSince = publishSince
        self.newFlag = newFlag
        self.missionFlag = missionFlag

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.authorName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.onSale = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.validDays = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.saleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.copyright = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.descriptionText = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.shopOrderId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.fromMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.toMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.validUntil = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.priceTier = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRING:
                    self.price = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.currency = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRING:
                    self.currencySymbol = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I32:
                    self.paymentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I64:
                    self.createDate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.BOOL:
                    self.ownFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.I32:
                    self.eventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRING:
                    self.urlSchema = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRING:
                    self.downloadUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.STRING:
                    self.buddyMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.I64:
                    self.publishSince = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.BOOL:
                    self.newFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.BOOL:
                    self.missionFlag = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Product')
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 1)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 2)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I32, 3)
            oprot.writeI32(self.version)
            oprot.writeFieldEnd()
        if self.authorName is not None:
            oprot.writeFieldBegin('authorName', TType.STRING, 4)
            oprot.writeString(self.authorName.encode('utf-8') if sys.version_info[0] == 2 else self.authorName)
            oprot.writeFieldEnd()
        if self.onSale is not None:
            oprot.writeFieldBegin('onSale', TType.BOOL, 5)
            oprot.writeBool(self.onSale)
            oprot.writeFieldEnd()
        if self.validDays is not None:
            oprot.writeFieldBegin('validDays', TType.I32, 6)
            oprot.writeI32(self.validDays)
            oprot.writeFieldEnd()
        if self.saleType is not None:
            oprot.writeFieldBegin('saleType', TType.I32, 7)
            oprot.writeI32(self.saleType)
            oprot.writeFieldEnd()
        if self.copyright is not None:
            oprot.writeFieldBegin('copyright', TType.STRING, 8)
            oprot.writeString(self.copyright.encode('utf-8') if sys.version_info[0] == 2 else self.copyright)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 9)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.descriptionText is not None:
            oprot.writeFieldBegin('descriptionText', TType.STRING, 10)
            oprot.writeString(self.descriptionText.encode('utf-8') if sys.version_info[0] == 2 else self.descriptionText)
            oprot.writeFieldEnd()
        if self.shopOrderId is not None:
            oprot.writeFieldBegin('shopOrderId', TType.I64, 11)
            oprot.writeI64(self.shopOrderId)
            oprot.writeFieldEnd()
        if self.fromMid is not None:
            oprot.writeFieldBegin('fromMid', TType.STRING, 12)
            oprot.writeString(self.fromMid.encode('utf-8') if sys.version_info[0] == 2 else self.fromMid)
            oprot.writeFieldEnd()
        if self.toMid is not None:
            oprot.writeFieldBegin('toMid', TType.STRING, 13)
            oprot.writeString(self.toMid.encode('utf-8') if sys.version_info[0] == 2 else self.toMid)
            oprot.writeFieldEnd()
        if self.validUntil is not None:
            oprot.writeFieldBegin('validUntil', TType.I64, 14)
            oprot.writeI64(self.validUntil)
            oprot.writeFieldEnd()
        if self.priceTier is not None:
            oprot.writeFieldBegin('priceTier', TType.I32, 15)
            oprot.writeI32(self.priceTier)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin('price', TType.STRING, 16)
            oprot.writeString(self.price.encode('utf-8') if sys.version_info[0] == 2 else self.price)
            oprot.writeFieldEnd()
        if self.currency is not None:
            oprot.writeFieldBegin('currency', TType.STRING, 17)
            oprot.writeString(self.currency.encode('utf-8') if sys.version_info[0] == 2 else self.currency)
            oprot.writeFieldEnd()
        if self.currencySymbol is not None:
            oprot.writeFieldBegin('currencySymbol', TType.STRING, 18)
            oprot.writeString(self.currencySymbol.encode('utf-8') if sys.version_info[0] == 2 else self.currencySymbol)
            oprot.writeFieldEnd()
        if self.paymentType is not None:
            oprot.writeFieldBegin('paymentType', TType.I32, 19)
            oprot.writeI32(self.paymentType)
            oprot.writeFieldEnd()
        if self.createDate is not None:
            oprot.writeFieldBegin('createDate', TType.I64, 20)
            oprot.writeI64(self.createDate)
            oprot.writeFieldEnd()
        if self.ownFlag is not None:
            oprot.writeFieldBegin('ownFlag', TType.BOOL, 21)
            oprot.writeBool(self.ownFlag)
            oprot.writeFieldEnd()
        if self.eventType is not None:
            oprot.writeFieldBegin('eventType', TType.I32, 22)
            oprot.writeI32(self.eventType)
            oprot.writeFieldEnd()
        if self.urlSchema is not None:
            oprot.writeFieldBegin('urlSchema', TType.STRING, 23)
            oprot.writeString(self.urlSchema.encode('utf-8') if sys.version_info[0] == 2 else self.urlSchema)
            oprot.writeFieldEnd()
        if self.downloadUrl is not None:
            oprot.writeFieldBegin('downloadUrl', TType.STRING, 24)
            oprot.writeString(self.downloadUrl.encode('utf-8') if sys.version_info[0] == 2 else self.downloadUrl)
            oprot.writeFieldEnd()
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 25)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        if self.publishSince is not None:
            oprot.writeFieldBegin('publishSince', TType.I64, 26)
            oprot.writeI64(self.publishSince)
            oprot.writeFieldEnd()
        if self.newFlag is not None:
            oprot.writeFieldBegin('newFlag', TType.BOOL, 27)
            oprot.writeBool(self.newFlag)
            oprot.writeFieldEnd()
        if self.missionFlag is not None:
            oprot.writeFieldBegin('missionFlag', TType.BOOL, 28)
            oprot.writeBool(self.missionFlag)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()
        
class getProduct_args(object):

    thrift_spec = (
        None,  # 0
        None,  # 1
        (2, TType.I64, 'packageID', None, None, ),  # 2
        (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
    )

    def __init__(self, packageID=None, language=None, country=None,):
        self.packageID = packageID
        self.language = language
        self.country = country

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.packageID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProduct_args')
        if self.packageID is not None:
            oprot.writeFieldBegin('packageID', TType.I64, 2)
            oprot.writeI64(self.packageID)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class getProduct_result(object):

    thrift_spec = (
        (0, TType.STRUCT, 'success', [Product, None], None, ),  # 0
        (1, TType.STRUCT, 'e', [LiffException, None], None, ),  # 1
    )

    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Product()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = LiffException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProduct_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

class Client(object):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot

    def issueLiffView(self, request):
        self._oprot.writeMessageBegin('issueLiffView', TMessageType.CALL, 0)
        issueLiffView_args(request = request).write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
        return self.recv_issueLiffView()

    def recv_issueLiffView(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueLiffView_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueLiffView failed: unknown result")

    def getProduct(self, packageID, language, country):
        self._oprot.writeMessageBegin('getProduct', TMessageType.CALL, 0)
        getProduct_args(packageID = packageID, language = language, country = country).write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()
        return self.recv_getProduct()

    def recv_getProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProduct failed: unknown result")

class Template(object):
    def __init__(self, token = "", appName = '', header = {}):
        self.appName = appName
        self.token = token
        if header != {}: self.header = header
        else: self.header = self.getHeader()
        self.liff = self.login()
        self.shop = self.shop()
    def getHeader(self):
        Headers={'User-Agent': 'Line/8.11.0', 'X-Line-Application': self.appName, 'X-Line-Access': self.token, 'X-Line-Carrier': '51089, 1-0' }
        return Headers
    def login(self):
        transport = THttpClient.THttpClient('https://gwx.line.naver.jp/LIFF1') 
        transport.setCustomHeaders(self.header)
        liff = Client(TCompactProtocol.TCompactProtocol(transport)) 
        transport.open()
        return liff
    def shop(self):
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/SHOP4') 
        transport.setCustomHeaders(self.header)
        shop = Client(TCompactProtocol.TCompactProtocol(transport)) 
        transport.open()
        return shop
    def sendFlex(self, to, data):
        az = LiffChatContext(to)
        ax = LiffContext(chat=az)
        lf = LiffViewRequest('1602687308-GXq4Vvk9', ax)
        token = self.liff.issueLiffView(lf)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
