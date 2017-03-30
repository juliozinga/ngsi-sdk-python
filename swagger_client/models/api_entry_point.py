# coding: utf-8

"""
    ngsi-v2

    NGSI V2 API

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class APIEntryPoint(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, entities_url=None, types_url=None, subscriptions_url=None):
        """
        APIEntryPoint - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entities_url': 'str',
            'types_url': 'str',
            'subscriptions_url': 'str'
        }

        self.attribute_map = {
            'entities_url': 'entities_url',
            'types_url': 'types_url',
            'subscriptions_url': 'subscriptions_url'
        }

        self._entities_url = entities_url
        self._types_url = types_url
        self._subscriptions_url = subscriptions_url


    @property
    def entities_url(self):
        """
        Gets the entities_url of this APIEntryPoint.
        URL which points to the entities resource

        :return: The entities_url of this APIEntryPoint.
        :rtype: str
        """
        return self._entities_url

    @entities_url.setter
    def entities_url(self, entities_url):
        """
        Sets the entities_url of this APIEntryPoint.
        URL which points to the entities resource

        :param entities_url: The entities_url of this APIEntryPoint.
        :type: str
        """
        if entities_url is None:
            raise ValueError("Invalid value for `entities_url`, must not be `None`")

        self._entities_url = entities_url

    @property
    def types_url(self):
        """
        Gets the types_url of this APIEntryPoint.
        URL which points to the types resource

        :return: The types_url of this APIEntryPoint.
        :rtype: str
        """
        return self._types_url

    @types_url.setter
    def types_url(self, types_url):
        """
        Sets the types_url of this APIEntryPoint.
        URL which points to the types resource

        :param types_url: The types_url of this APIEntryPoint.
        :type: str
        """
        if types_url is None:
            raise ValueError("Invalid value for `types_url`, must not be `None`")

        self._types_url = types_url

    @property
    def subscriptions_url(self):
        """
        Gets the subscriptions_url of this APIEntryPoint.
        URL which points to the subscriptions resource

        :return: The subscriptions_url of this APIEntryPoint.
        :rtype: str
        """
        return self._subscriptions_url

    @subscriptions_url.setter
    def subscriptions_url(self, subscriptions_url):
        """
        Sets the subscriptions_url of this APIEntryPoint.
        URL which points to the subscriptions resource

        :param subscriptions_url: The subscriptions_url of this APIEntryPoint.
        :type: str
        """
        if subscriptions_url is None:
            raise ValueError("Invalid value for `subscriptions_url`, must not be `None`")

        self._subscriptions_url = subscriptions_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
