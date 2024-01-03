# encoding: utf-8

from server import gord_client


async def get_blockdag():
    """
    Get some global gor BlockDAG information
    """
    resp = await gord_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
