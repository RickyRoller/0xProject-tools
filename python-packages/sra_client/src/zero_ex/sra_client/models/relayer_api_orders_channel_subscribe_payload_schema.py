# coding: utf-8


import pprint
import re  # noqa: F401

import six


class RelayerApiOrdersChannelSubscribePayloadSchema(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "maker_asset_proxy_id": "str",
        "taker_asset_proxy_id": "str",
        "maker_asset_address": "str",
        "taker_asset_address": "str",
        "maker_asset_data": "str",
        "taker_asset_data": "str",
        "trader_asset_data": "str",
    }

    attribute_map = {
        "maker_asset_proxy_id": "makerAssetProxyId",
        "taker_asset_proxy_id": "takerAssetProxyId",
        "maker_asset_address": "makerAssetAddress",
        "taker_asset_address": "takerAssetAddress",
        "maker_asset_data": "makerAssetData",
        "taker_asset_data": "takerAssetData",
        "trader_asset_data": "traderAssetData",
    }

    def __init__(
        self,
        maker_asset_proxy_id=None,
        taker_asset_proxy_id=None,
        maker_asset_address=None,
        taker_asset_address=None,
        maker_asset_data=None,
        taker_asset_data=None,
        trader_asset_data=None,
    ):  # noqa: E501
        """RelayerApiOrdersChannelSubscribePayloadSchema - a model defined in OpenAPI"""  # noqa: E501

        self._maker_asset_proxy_id = None
        self._taker_asset_proxy_id = None
        self._maker_asset_address = None
        self._taker_asset_address = None
        self._maker_asset_data = None
        self._taker_asset_data = None
        self._trader_asset_data = None
        self.discriminator = None

        if maker_asset_proxy_id is not None:
            self.maker_asset_proxy_id = maker_asset_proxy_id
        if taker_asset_proxy_id is not None:
            self.taker_asset_proxy_id = taker_asset_proxy_id
        if maker_asset_address is not None:
            self.maker_asset_address = maker_asset_address
        if taker_asset_address is not None:
            self.taker_asset_address = taker_asset_address
        if maker_asset_data is not None:
            self.maker_asset_data = maker_asset_data
        if taker_asset_data is not None:
            self.taker_asset_data = taker_asset_data
        if trader_asset_data is not None:
            self.trader_asset_data = trader_asset_data

    @property
    def maker_asset_proxy_id(self):
        """Gets the maker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The maker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._maker_asset_proxy_id

    @maker_asset_proxy_id.setter
    def maker_asset_proxy_id(self, maker_asset_proxy_id):
        """Sets the maker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param maker_asset_proxy_id: The maker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if maker_asset_proxy_id is not None and not re.search(
            r"^0x(([0-9a-f][0-9a-f])+)?$", maker_asset_proxy_id
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `maker_asset_proxy_id`, must be a follow pattern or equal to `/^0x(([0-9a-f][0-9a-f])+)?$/`"
            )  # noqa: E501

        self._maker_asset_proxy_id = maker_asset_proxy_id

    @property
    def taker_asset_proxy_id(self):
        """Gets the taker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The taker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._taker_asset_proxy_id

    @taker_asset_proxy_id.setter
    def taker_asset_proxy_id(self, taker_asset_proxy_id):
        """Sets the taker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param taker_asset_proxy_id: The taker_asset_proxy_id of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if taker_asset_proxy_id is not None and not re.search(
            r"^0x(([0-9a-f][0-9a-f])+)?$", taker_asset_proxy_id
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `taker_asset_proxy_id`, must be a follow pattern or equal to `/^0x(([0-9a-f][0-9a-f])+)?$/`"
            )  # noqa: E501

        self._taker_asset_proxy_id = taker_asset_proxy_id

    @property
    def maker_asset_address(self):
        """Gets the maker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The maker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._maker_asset_address

    @maker_asset_address.setter
    def maker_asset_address(self, maker_asset_address):
        """Sets the maker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param maker_asset_address: The maker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if maker_asset_address is not None and not re.search(
            r"^0x[0-9a-f]{40}$", maker_asset_address
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `maker_asset_address`, must be a follow pattern or equal to `/^0x[0-9a-f]{40}$/`"
            )  # noqa: E501

        self._maker_asset_address = maker_asset_address

    @property
    def taker_asset_address(self):
        """Gets the taker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The taker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._taker_asset_address

    @taker_asset_address.setter
    def taker_asset_address(self, taker_asset_address):
        """Sets the taker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param taker_asset_address: The taker_asset_address of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if taker_asset_address is not None and not re.search(
            r"^0x[0-9a-f]{40}$", taker_asset_address
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `taker_asset_address`, must be a follow pattern or equal to `/^0x[0-9a-f]{40}$/`"
            )  # noqa: E501

        self._taker_asset_address = taker_asset_address

    @property
    def maker_asset_data(self):
        """Gets the maker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The maker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._maker_asset_data

    @maker_asset_data.setter
    def maker_asset_data(self, maker_asset_data):
        """Sets the maker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param maker_asset_data: The maker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if maker_asset_data is not None and not re.search(
            r"^0x(([0-9a-f][0-9a-f])+)?$", maker_asset_data
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `maker_asset_data`, must be a follow pattern or equal to `/^0x(([0-9a-f][0-9a-f])+)?$/`"
            )  # noqa: E501

        self._maker_asset_data = maker_asset_data

    @property
    def taker_asset_data(self):
        """Gets the taker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The taker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._taker_asset_data

    @taker_asset_data.setter
    def taker_asset_data(self, taker_asset_data):
        """Sets the taker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param taker_asset_data: The taker_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if taker_asset_data is not None and not re.search(
            r"^0x(([0-9a-f][0-9a-f])+)?$", taker_asset_data
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `taker_asset_data`, must be a follow pattern or equal to `/^0x(([0-9a-f][0-9a-f])+)?$/`"
            )  # noqa: E501

        self._taker_asset_data = taker_asset_data

    @property
    def trader_asset_data(self):
        """Gets the trader_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :return: The trader_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :rtype: str
        """
        return self._trader_asset_data

    @trader_asset_data.setter
    def trader_asset_data(self, trader_asset_data):
        """Sets the trader_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.


        :param trader_asset_data: The trader_asset_data of this RelayerApiOrdersChannelSubscribePayloadSchema.
        :type: str
        """
        if trader_asset_data is not None and not re.search(
            r"^0x(([0-9a-f][0-9a-f])+)?$", trader_asset_data
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `trader_asset_data`, must be a follow pattern or equal to `/^0x(([0-9a-f][0-9a-f])+)?$/`"
            )  # noqa: E501

        self._trader_asset_data = trader_asset_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value,
                    )
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(
            other, RelayerApiOrdersChannelSubscribePayloadSchema
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
