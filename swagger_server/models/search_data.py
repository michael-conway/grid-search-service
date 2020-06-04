# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.index_schema_description import IndexSchemaDescription  # noqa: F401,E501
from swagger_server.models.search_data_search_result import SearchDataSearchResult  # noqa: F401,E501
from swagger_server import util


class SearchData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, index_schema_description: IndexSchemaDescription = None,
                 search_result: List[SearchDataSearchResult] = None):  # noqa: E501
        """SearchData - a model defined in Swagger

        :param index_schema_description: The index_schema_description of this SearchData.  # noqa: E501
        :type index_schema_description: IndexSchemaDescription
        :param search_result: The search_result of this SearchData.  # noqa: E501
        :type search_result: List[SearchDataSearchResult]
        """
        self.swagger_types = {
            'index_schema_description': IndexSchemaDescription,
            'search_result': List[SearchDataSearchResult]
        }

        self.attribute_map = {
            'index_schema_description': 'index-schema-description',
            'search_result': 'search_result'
        }
        self._index_schema_description = index_schema_description
        self._search_result = search_result

    @classmethod
    def from_dict(cls, dikt) -> 'SearchData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The search_data of this SearchData.  # noqa: E501
        :rtype: SearchData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index_schema_description(self) -> IndexSchemaDescription:
        """Gets the index_schema_description of this SearchData.


        :return: The index_schema_description of this SearchData.
        :rtype: IndexSchemaDescription
        """
        return self._index_schema_description

    @index_schema_description.setter
    def index_schema_description(self, index_schema_description: IndexSchemaDescription):
        """Sets the index_schema_description of this SearchData.


        :param index_schema_description: The index_schema_description of this SearchData.
        :type index_schema_description: IndexSchemaDescription
        """

        self._index_schema_description = index_schema_description

    @property
    def search_result(self) -> List[SearchDataSearchResult]:
        """Gets the search_result of this SearchData.


        :return: The search_result of this SearchData.
        :rtype: List[SearchDataSearchResult]
        """
        return self._search_result

    @search_result.setter
    def search_result(self, search_result: List[SearchDataSearchResult]):
        """Sets the search_result of this SearchData.


        :param search_result: The search_result of this SearchData.
        :type search_result: List[SearchDataSearchResult]
        """

        self._search_result = search_result
