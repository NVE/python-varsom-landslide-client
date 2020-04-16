# coding: utf-8

"""
    Jordskredvarsel API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class MediaTypeHeaderValue(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'char_set': 'str',
        'parameters': 'list[NameValueHeaderValue]',
        'media_type': 'str'
    }

    attribute_map = {
        'char_set': 'CharSet',
        'parameters': 'Parameters',
        'media_type': 'MediaType'
    }

    def __init__(self, char_set=None, parameters=None, media_type=None):  # noqa: E501
        """MediaTypeHeaderValue - a model defined in Swagger"""  # noqa: E501
        self._char_set = None
        self._parameters = None
        self._media_type = None
        self.discriminator = None
        if char_set is not None:
            self.char_set = char_set
        if parameters is not None:
            self.parameters = parameters
        if media_type is not None:
            self.media_type = media_type

    @property
    def char_set(self):
        """Gets the char_set of this MediaTypeHeaderValue.  # noqa: E501


        :return: The char_set of this MediaTypeHeaderValue.  # noqa: E501
        :rtype: str
        """
        return self._char_set

    @char_set.setter
    def char_set(self, char_set):
        """Sets the char_set of this MediaTypeHeaderValue.


        :param char_set: The char_set of this MediaTypeHeaderValue.  # noqa: E501
        :type: str
        """

        self._char_set = char_set

    @property
    def parameters(self):
        """Gets the parameters of this MediaTypeHeaderValue.  # noqa: E501


        :return: The parameters of this MediaTypeHeaderValue.  # noqa: E501
        :rtype: list[NameValueHeaderValue]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MediaTypeHeaderValue.


        :param parameters: The parameters of this MediaTypeHeaderValue.  # noqa: E501
        :type: list[NameValueHeaderValue]
        """

        self._parameters = parameters

    @property
    def media_type(self):
        """Gets the media_type of this MediaTypeHeaderValue.  # noqa: E501


        :return: The media_type of this MediaTypeHeaderValue.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this MediaTypeHeaderValue.


        :param media_type: The media_type of this MediaTypeHeaderValue.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MediaTypeHeaderValue, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MediaTypeHeaderValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other