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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AttributeValueApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_attribute_value(self, entity_id, attr_name, **kwargs):
        """
        
        This operation returns the `value` property with the value of the attribute. * If attribute value is JSON Array or Object:   * If `Accept` header can be expanded to `application/json` or `text/plain` return the value as a JSON with a     response type of application/json or text/plain (whichever is the first in `Accept` header or     `application/json` in the case of `Accept: */*`).   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: application/json, text/plain\" * If attribute value is a string, number, null or boolean:   * If `Accept` header can be expanded to text/plain return the value as text. In case of a string, citation     marks are used at the begining and end.   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: text/plain\" Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_attribute_value(entity_id, attr_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: Id of the entity in question (required)
        :param str attr_name: Name of the attribute to be retrieved. (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: AttributeValue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_attribute_value_with_http_info(entity_id, attr_name, **kwargs)
        else:
            (data) = self.get_attribute_value_with_http_info(entity_id, attr_name, **kwargs)
            return data

    def get_attribute_value_with_http_info(self, entity_id, attr_name, **kwargs):
        """
        
        This operation returns the `value` property with the value of the attribute. * If attribute value is JSON Array or Object:   * If `Accept` header can be expanded to `application/json` or `text/plain` return the value as a JSON with a     response type of application/json or text/plain (whichever is the first in `Accept` header or     `application/json` in the case of `Accept: */*`).   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: application/json, text/plain\" * If attribute value is a string, number, null or boolean:   * If `Accept` header can be expanded to text/plain return the value as text. In case of a string, citation     marks are used at the begining and end.   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: text/plain\" Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_attribute_value_with_http_info(entity_id, attr_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: Id of the entity in question (required)
        :param str attr_name: Name of the attribute to be retrieved. (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: AttributeValue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'attr_name', 'type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attribute_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params) or (params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_attribute_value`")
        # verify the required parameter 'attr_name' is set
        if ('attr_name' not in params) or (params['attr_name'] is None):
            raise ValueError("Missing the required parameter `attr_name` when calling `get_attribute_value`")


        collection_formats = {}

        resource_path = '/entities/{entityId}/attrs/{attrName}/value'.replace('{format}', 'json')
        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']
        if 'attr_name' in params:
            path_params['attrName'] = params['attr_name']

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'plain/text'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['fiware_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AttributeValue',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def update_attribute_value(self, entity_id, attr_name, body, **kwargs):
        """
        
        The request payload is the new attribute value. * If the request payload MIME type is `application/json`, then the value of the attribute is set to   the JSON object or array coded in the payload (if the payload is not a valid JSON document,   then an error is returned). * If the request payload MIME type is `text/plain`, then the following algorithm is applied to the   payload:   * If the payload starts and ends with citation-marks (`\"`), the value is taken as a string     (the citation marks themselves are not considered part of the string)   * If `true` or `false`, the value is taken as a boolean.   * If `null`, the value is taken as null.   * If these first three tests 'fail', the text is interpreted as a number.   * If not a valid number, then an error is returned and the attribute's value is unchanged. The payload MIME type in the request is specified in the `Content-Type` HTTP header. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_attribute_value(entity_id, attr_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: Id of the entity to be updated. (required)
        :param str attr_name: Attribute name. (required)
        :param AttributeValue body: JSON AttributeValue Representation (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_attribute_value_with_http_info(entity_id, attr_name, body, **kwargs)
        else:
            (data) = self.update_attribute_value_with_http_info(entity_id, attr_name, body, **kwargs)
            return data

    def update_attribute_value_with_http_info(self, entity_id, attr_name, body, **kwargs):
        """
        
        The request payload is the new attribute value. * If the request payload MIME type is `application/json`, then the value of the attribute is set to   the JSON object or array coded in the payload (if the payload is not a valid JSON document,   then an error is returned). * If the request payload MIME type is `text/plain`, then the following algorithm is applied to the   payload:   * If the payload starts and ends with citation-marks (`\"`), the value is taken as a string     (the citation marks themselves are not considered part of the string)   * If `true` or `false`, the value is taken as a boolean.   * If `null`, the value is taken as null.   * If these first three tests 'fail', the text is interpreted as a number.   * If not a valid number, then an error is returned and the attribute's value is unchanged. The payload MIME type in the request is specified in the `Content-Type` HTTP header. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_attribute_value_with_http_info(entity_id, attr_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: Id of the entity to be updated. (required)
        :param str attr_name: Attribute name. (required)
        :param AttributeValue body: JSON AttributeValue Representation (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'attr_name', 'body', 'type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_attribute_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params) or (params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `update_attribute_value`")
        # verify the required parameter 'attr_name' is set
        if ('attr_name' not in params) or (params['attr_name'] is None):
            raise ValueError("Missing the required parameter `attr_name` when calling `update_attribute_value`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_attribute_value`")


        collection_formats = {}

        resource_path = '/entities/{entityId}/attrs/{attrName}/value'.replace('{format}', 'json')
        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']
        if 'attr_name' in params:
            path_params['attrName'] = params['attr_name']

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'plain/text'])

        # Authentication setting
        auth_settings = ['fiware_token']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
