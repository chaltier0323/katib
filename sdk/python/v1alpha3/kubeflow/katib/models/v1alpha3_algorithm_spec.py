# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    OpenAPI spec version: v1alpha3-0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.models.v1alpha3_algorithm_setting import V1alpha3AlgorithmSetting  # noqa: F401,E501
from kubeflow.katib.models.v1alpha3_early_stopping_spec import V1alpha3EarlyStoppingSpec  # noqa: F401,E501


class V1alpha3AlgorithmSpec(object):
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
        'algorithm_name': 'str',
        'algorithm_settings': 'list[V1alpha3AlgorithmSetting]',
        'early_stopping': 'V1alpha3EarlyStoppingSpec'
    }

    attribute_map = {
        'algorithm_name': 'algorithmName',
        'algorithm_settings': 'algorithmSettings',
        'early_stopping': 'earlyStopping'
    }

    def __init__(self, algorithm_name=None, algorithm_settings=None, early_stopping=None):  # noqa: E501
        """V1alpha3AlgorithmSpec - a model defined in Swagger"""  # noqa: E501

        self._algorithm_name = None
        self._algorithm_settings = None
        self._early_stopping = None
        self.discriminator = None

        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if algorithm_settings is not None:
            self.algorithm_settings = algorithm_settings
        if early_stopping is not None:
            self.early_stopping = early_stopping

    @property
    def algorithm_name(self):
        """Gets the algorithm_name of this V1alpha3AlgorithmSpec.  # noqa: E501


        :return: The algorithm_name of this V1alpha3AlgorithmSpec.  # noqa: E501
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        """Sets the algorithm_name of this V1alpha3AlgorithmSpec.


        :param algorithm_name: The algorithm_name of this V1alpha3AlgorithmSpec.  # noqa: E501
        :type: str
        """

        self._algorithm_name = algorithm_name

    @property
    def algorithm_settings(self):
        """Gets the algorithm_settings of this V1alpha3AlgorithmSpec.  # noqa: E501

        Key-value pairs representing settings for suggestion algorithms.  # noqa: E501

        :return: The algorithm_settings of this V1alpha3AlgorithmSpec.  # noqa: E501
        :rtype: list[V1alpha3AlgorithmSetting]
        """
        return self._algorithm_settings

    @algorithm_settings.setter
    def algorithm_settings(self, algorithm_settings):
        """Sets the algorithm_settings of this V1alpha3AlgorithmSpec.

        Key-value pairs representing settings for suggestion algorithms.  # noqa: E501

        :param algorithm_settings: The algorithm_settings of this V1alpha3AlgorithmSpec.  # noqa: E501
        :type: list[V1alpha3AlgorithmSetting]
        """

        self._algorithm_settings = algorithm_settings

    @property
    def early_stopping(self):
        """Gets the early_stopping of this V1alpha3AlgorithmSpec.  # noqa: E501


        :return: The early_stopping of this V1alpha3AlgorithmSpec.  # noqa: E501
        :rtype: V1alpha3EarlyStoppingSpec
        """
        return self._early_stopping

    @early_stopping.setter
    def early_stopping(self, early_stopping):
        """Sets the early_stopping of this V1alpha3AlgorithmSpec.


        :param early_stopping: The early_stopping of this V1alpha3AlgorithmSpec.  # noqa: E501
        :type: V1alpha3EarlyStoppingSpec
        """

        self._early_stopping = early_stopping

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
        if issubclass(V1alpha3AlgorithmSpec, dict):
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
        if not isinstance(other, V1alpha3AlgorithmSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
