import pathlib

from client import OpenContractsClient, SemanticIcon, LabelType

API_KEY = "dcfbca8a89e88e38822988e15b2230b83cc0c500"
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

meta_data_label = client.create_annotation_label(
    text="Meta Label",
    description="Test meta label",
    icon=SemanticIcon.KEY,
    labelset_id=labelset_id,
    label_type=LabelType.METADATA_LABEL
)

doc_type_data_label = client.create_annotation_label(
    text="Doc Type Label",
    description="Test doc type label",
    icon=SemanticIcon.KEY,
    labelset_id=labelset_id,
    label_type=LabelType.DOC_TYPE_LABEL
)

text_data_data_label = client.create_annotation_label(
    text="Span Label",
    description="Test span label",
    icon=SemanticIcon.KEY,
    labelset_id=labelset_id,
    label_type=LabelType.TOKEN_LABEL
)

print(client.create_corpus(
    icon_path=pathlib.Path("/home/jman/PycharmProjects/OpenContractsApiClientTest/icon.png"),
    title="USC Labels",
    description="Code for United States Code Labels",
    labelset_id=labelset_id,
))

test_pdf_path = pathlib.Path("test.pdf")

print(
    client.upload_document(
        test_pdf_path,
        title="Test Doc",
        description="Test document uploaded for API client test."
    )
)

