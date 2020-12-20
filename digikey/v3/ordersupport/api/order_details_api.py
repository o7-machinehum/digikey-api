# coding: utf-8

"""
    Order Details

    Retrieve information about current and past orders.  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from digikey.v3.ordersupport.api_client import ApiClient


class OrderDetailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def order_history(self, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Retrieves a list of SalesOrderIds and dates for all SalesOrders within a date range belonging to a CustomerId.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_history(authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param int customer_id: CustomerId that is on the Digi-Key account with which you authenticated. If not provided, will  default to the first CustomerId on the Digi-Key account.
        :param bool open_only: If true will only return open orders. If false, will return open and closed orders.
        :param bool include_company_orders: Include all company orders for the location associated with the given CustomerId.
        :param str start_date: Begining of date range in ISO 8601 format. For example: 2018-10-31
        :param str end_date: End of date range in ISO 8601 format. For example: 2018-10-31
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth with  fields that you do not wish to receive. For example: \"SalesOrderId,PurchaseOrder\"
        :return: list[SalesOrderHistoryItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_history_with_http_info(authorization, x_digikey_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.order_history_with_http_info(authorization, x_digikey_client_id, **kwargs)  # noqa: E501
            return data

    def order_history_with_http_info(self, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Retrieves a list of SalesOrderIds and dates for all SalesOrders within a date range belonging to a CustomerId.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_history_with_http_info(authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param int customer_id: CustomerId that is on the Digi-Key account with which you authenticated. If not provided, will  default to the first CustomerId on the Digi-Key account.
        :param bool open_only: If true will only return open orders. If false, will return open and closed orders.
        :param bool include_company_orders: Include all company orders for the location associated with the given CustomerId.
        :param str start_date: Begining of date range in ISO 8601 format. For example: 2018-10-31
        :param str end_date: End of date range in ISO 8601 format. For example: 2018-10-31
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth with  fields that you do not wish to receive. For example: \"SalesOrderId,PurchaseOrder\"
        :return: list[SalesOrderHistoryItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_digikey_client_id', 'customer_id', 'open_only', 'include_company_orders', 'start_date', 'end_date', 'includes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `order_history`")  # noqa: E501
        # verify the required parameter 'x_digikey_client_id' is set
        if ('x_digikey_client_id' not in params or
                params['x_digikey_client_id'] is None):
            raise ValueError("Missing the required parameter `x_digikey_client_id` when calling `order_history`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in params:
            query_params.append(('CustomerId', params['customer_id']))  # noqa: E501
        if 'open_only' in params:
            query_params.append(('OpenOnly', params['open_only']))  # noqa: E501
        if 'include_company_orders' in params:
            query_params.append(('IncludeCompanyOrders', params['include_company_orders']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('StartDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('EndDate', params['end_date']))  # noqa: E501
        if 'includes' in params:
            query_params.append(('Includes', params['includes']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_digikey_client_id' in params:
            header_params['X-DIGIKEY-Client-Id'] = params['x_digikey_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/History', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SalesOrderHistoryItem]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_status(self, sales_order_id, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Retrieve order status for given SalesOrderId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_status(sales_order_id, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sales_order_id: SalesOrderId belonging to you or your company that you wish to lookup (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth with  fields that you do not wish to receive. For example: \"SalesOrderId,ShippingDetails\"
        :return: OrderStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.order_status_with_http_info(sales_order_id, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.order_status_with_http_info(sales_order_id, authorization, x_digikey_client_id, **kwargs)  # noqa: E501
            return data

    def order_status_with_http_info(self, sales_order_id, authorization, x_digikey_client_id, **kwargs):  # noqa: E501
        """Retrieve order status for given SalesOrderId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.order_status_with_http_info(sales_order_id, authorization, x_digikey_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sales_order_id: SalesOrderId belonging to you or your company that you wish to lookup (required)
        :param str authorization: OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info. (required)
        :param str x_digikey_client_id: The Client Id for your App. (required)
        :param str includes: Comma separated list of fields to return. Used to customize response to reduce bandwidth with  fields that you do not wish to receive. For example: \"SalesOrderId,ShippingDetails\"
        :return: OrderStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sales_order_id', 'authorization', 'x_digikey_client_id', 'includes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sales_order_id' is set
        if ('sales_order_id' not in params or
                params['sales_order_id'] is None):
            raise ValueError("Missing the required parameter `sales_order_id` when calling `order_status`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `order_status`")  # noqa: E501
        # verify the required parameter 'x_digikey_client_id' is set
        if ('x_digikey_client_id' not in params or
                params['x_digikey_client_id'] is None):
            raise ValueError("Missing the required parameter `x_digikey_client_id` when calling `order_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sales_order_id' in params:
            path_params['salesOrderId'] = params['sales_order_id']  # noqa: E501

        query_params = []
        if 'includes' in params:
            query_params.append(('Includes', params['includes']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_digikey_client_id' in params:
            header_params['X-DIGIKEY-Client-Id'] = params['x_digikey_client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Status/{salesOrderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
