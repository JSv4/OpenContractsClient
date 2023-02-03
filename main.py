import pathlib

from open_contracts_api_client.client_types.client_enums import SemanticIcon, LabelType
from open_contracts_api_client.client import OpenContractsClient

#API_KEY = "dcfbca8a89e88e38822988e15b2230b83cc0c500"
API_KEY = "1f9dfa788f071a1cf2d742f9b15b0acc140f0b1d"
url = f"http://localhost:8000/graphql/"

client = OpenContractsClient(
    graphql_url=url,
    api_key=API_KEY
)

# labelset_id = client.create_labelset(
#     icon_path=pathlib.Path("/home/jman/PycharmProjects/open-contracts-api-client/icon.png"),
#     title="USC Labels",
#     description="Code for United States Code Labels",
#     filename="icon.png"
# )
# print(f"Created labelset: {labelset_id}")
#
# meta_data_label = client.create_annotation_label(
#     text="Meta Label",
#     description="Test meta label",
#     icon=SemanticIcon.KEY,
#     labelset_id=labelset_id,
#     label_type=LabelType.METADATA_LABEL
# )
#
# doc_type_data_label = client.create_annotation_label(
#     text="Doc Type Label",
#     description="Test doc type label",
#     icon=SemanticIcon.KEY,
#     labelset_id=labelset_id,
#     label_type=LabelType.DOC_TYPE_LABEL
# )
#
# text_data_data_label = client.create_annotation_label(
#     text="Span Label",
#     description="Test span label",
#     icon=SemanticIcon.KEY,
#     labelset_id=labelset_id,
#     label_type=LabelType.TOKEN_LABEL
# )
#
# print(client.create_corpus(
#     icon_path=pathlib.Path("/home/jman/PycharmProjects/open-contracts-api-client/icon.png"),
#     title="Demo USC Labels",
#     description="Code for United States Code Labels",
#     labelset_id=labelset_id,
# ))
#
test_pdf_path = pathlib.Path("test.pdf")

doc_id = client.upload_document(
    test_pdf_path,
    title="Test Doc",
    description="Test document uploaded for API client test."
)

# client.link_document_to_corpus(
#     corpus_id=client.corpus_id,
#     document_ids=[doc_id]
# )
#
# client.upload_and_annotate_document(
#     doc_path=test_pdf_path,
#     doc_title=test_pdf_path.name,
#     metadata_to_annotate={
#         "Description": "This is my custom description",
#         "USC Section": "12345",
#         "Category": "Blue blue christmas"
#     },
#     doc_labels_to_annotate=[
#         "Nonsense",
#         "Garbage"
#         "Badly-Written"
#     ]
# )
#
