import base64
import uuid

import helper.constant_helper as constant_helper
import helper.collection_helper as collection_helper

import wrapper.request_wrapper as request_wrapper
import wrapper.security_wrapper as security_wrapper


class BaseSDKService(object):
    '''

    '''

    def __init__(self, name):
        self.name = name

    def create(self, payload, action="create"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {}
        attributes = payload

        headers.update({"authorization": "Basic " + base64.b64encode("%(name)s:%(pass)s".encode("utf-8") %
                                                                     {"name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret})})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        if apimapopts.get(action).get("has_signature") is True:
            headers.update({"x-signature": security_wrapper.sucurity_wrapper.get_wrapper().process_hmac_signature(
                value=collection_helper.CollectioHelper.process_serialize_data({"value": attributes}), password=request_wrapper.request_wrapper.get_wrapper().secret)})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_post(
            url=url, headers=headers, params=params, data=attributes)

    def get(self, id=None, action="get"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {"id": id} if id is not None else dict()

        headers.update({"authorization": "Basic " + base64.b64encode("%(name)s:%(pass)s".encode("utf-8") %
                                                                     {"name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret})})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_get(
            url=url, headers=headers, params=params)

    def get_by(self, by_key, by_value, swap_id=None, action="get"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {"id": str(uuid.uuid4())}

        url = ("%(url)s?%(key)s=%(value)s" %
               {"url": url, "key": by_key, "value": by_value})

        url = (url + ("&swap_id=%(swap_id)s" %
                      {swap_id: swap_id})) if swap_id is not None else url

        headers.update({"authorization": "Basic " + base64.b64encode("%(name)s:%(pass)s".encode("utf-8") %
                                                                     {"name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret})})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        headers.update(
            {"content-type": "application/x-www-form-urlencoded"})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_get(
            url=url, headers=headers, params=params)

    def save(self, id, payload, action="save"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {"id": id}
        attributes = payload

        headers.update({"authorization": "Basic " + base64.b64encode("%(name)s:%(pass)s".encode("utf-8") %
                                                                     {"name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret})})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        if apimapopts.get(action).get("has_signature") is True:
            headers.update({"x-signature": security_wrapper.sucurity_wrapper.get_wrapper().process_hmac_signature(
                value=collection_helper.CollectioHelper.process_serialize_data({"value": attributes}), password=request_wrapper.request_wrapper.get_wrapper().secret)})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_put(
            url=url, headers=headers, params=params, data=attributes)

    def delete(self, id=None, action="get"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {"id": id} if id is not None else dict()

        headers.update({"authorization": "Basic " + base64.b64encode("%(name)s:%(pass)s".encode("utf-8") %
                                                                     {"name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret})})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_delete(
            url=url, headers=headers, params=params)

    def fetch(self, filter, paging={"page": 1, "limit": 20}, action="fetch"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {**filter, **paging}

        headers.update({"authorization": "Basic " + base64.b64encode("%(name)s:%(pass)s".encode("utf-8") %
                                                                     {"name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret})})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_get(
            url=url, headers=headers, params=params)
