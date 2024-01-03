# encoding: utf-8

from server import gord_client


async def get_network():
    """
    Get some global gor network information
    """
    resp = await gord_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
