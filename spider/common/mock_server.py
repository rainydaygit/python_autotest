# coding:utf-8
from mock import mock

def mock_post(mock_method, mock_data, url, data, headers):
    mock_method = mock.Mock(return_value=mock_data)
    res = mock_method(url, data, headers)
    return res
