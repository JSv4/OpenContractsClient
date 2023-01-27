import pathlib

from client import OpenContractsClient

API_KEY = "7fdce209accfe8377403bff31da84c139ab9f35c"
url = f"http://localhost:8000/graphql/"

client = OpenContractsClient(
    graphql_url=url,
    api_key=API_KEY
)

labelset_id = client.create_labelset(
    icon_path=pathlib.Path("/home/jman/PycharmProjects/OpenContractsApiClientTest/icon.png"),
    title="USC Labels",
    description="Code for United States Code Labels",
    filename="icon.png"
)

print(client.create_corpus(
    icon_path=pathlib.Path("/home/jman/PycharmProjects/OpenContractsApiClientTest/icon.png"),
    title="USC Labels",
    description="Code for United States Code Labels",
    labelset_id=labelset_id,
))


