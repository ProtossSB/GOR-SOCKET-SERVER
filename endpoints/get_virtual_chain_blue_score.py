# encoding: utf-8

from server import gord_client


async def get_virtual_selected_parent_blue_score():
    """
    Returns the blue score of virtual selected parent
    """
    resp = await gord_client.request("getVirtualSelectedParentBlueScoreRequest")
    return resp["getVirtualSelectedParentBlueScoreResponse"]
