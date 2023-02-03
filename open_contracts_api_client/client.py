#  Copyright (C) 2022  John Scrudato / Gordium Knot Inc. d/b/a OpenSource.Legal
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
import pathlib
from typing import Optional

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from open_contracts_api_client.utils import base_64_encode_bytes, package_file_into_base64, random_hex_color
from open_contracts_api_client.client_types.client_enums import SemanticIcon, LabelType
from open_contracts_api_client.graphql.mutations import (
    CREATE_LABELSET,
    CREATE_CORPUS,
    CREATE_ANNOTATION_LABEL_FOR_LABEL_SET,
    UPLOAD_DOCUMENT,
    LINK_DOCUMENTS_TO_CORPUS,
    ANNOTATE_DOCUMENT
)


#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
class OpenContractsClient:

    label_store = {}

    corpus_id: str = None
    label_set_id: str = None

    def __init__(self, graphql_url: str, api_key: str):
        # Select your transport with a defined url endpoint
        transport = AIOHTTPTransport(
            url=graphql_url,
            headers={'AUTHORIZATION': f'Key {api_key}'}
        )
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def create_labelset(
        self,
        title: str,
        description: str,
        icon_path: pathlib.Path,
        filename: str
    ) -> Optional[str]:
        """
        Create a labelset.

        :param title: Title of labelset
        :param description: Description
        :param icon_path: Path to local icon file to upload
        :param filename: Name to give icon
        :return: Id of created labelset or None if creation failed.
        """

        if self.label_set_id is not None:
            print("Labelset already created. Exiting")
            return

        icon_str = package_file_into_base64(icon_path)

        # Execute the query on the transport
        result = self.client.execute(
            CREATE_LABELSET,
            variable_values={
                "title": title,
                "icon": icon_str,
                "description": description,
                "filename": filename
            }
        )

        if result['createLabelset']['ok']:
            self.label_set_id = result['createLabelset']['obj']['id']
            return self.label_set_id
        else:
            return None

    def create_corpus(
        self,
        description: str,
        icon_path: pathlib.Path,
        labelset_id: str,
        title: str
    ) -> Optional[str]:

        if self.corpus_id is not None:
            print("Corpus already created. Exiting")
            return

        icon_str = package_file_into_base64(icon_path)

        result = self.client.execute(
            CREATE_CORPUS,
            variable_values={
                "labelSet": labelset_id,
                "icon": icon_str,
                "description": description,
                "title": title
            }
        )

        if result['createCorpus']['ok']:
            self.corpus_id = result['createCorpus']['objId']
            return self.corpus_id
        else:
            return None

    def create_annotation_label(
        self,
        description: str,
        icon: SemanticIcon,
        text: str,
        label_type: LabelType,
        labelset_id: str,
        color: str = None
    ) -> Optional[str]:

        if text in self.label_store:
            raise ValueError("We're not currently allowing duplicate labels with same name.")

        if color is None:
            color = random_hex_color()

        result = self.client.execute(
            CREATE_ANNOTATION_LABEL_FOR_LABEL_SET,
            variable_values={
                "color": color,
                "description": description,
                "icon": icon.value,
                "text": text,
                "labelType": label_type,
                "labelsetId": labelset_id,
            }
        )
        print(f"Result: {result}")

        if result['createAnnotationLabelForLabelset']['ok']:
            self.label_store[text] = result['createAnnotationLabelForLabelset']['objId']
            return result['createAnnotationLabelForLabelset']['objId']
        else:
            return None

    def get_or_create_annotation_label(
            self,
            description: str,
            icon: SemanticIcon,
            text: str,
            label_type: LabelType,
            labelset_id: str,
            color: str = None
    ) -> Optional[str]:

        if text in self.label_store:
            return self.label_store[text]

        return self.create_annotation_label(
            description=description,
            icon=icon,
            text=text,
            label_type=label_type,
            labelset_id=labelset_id,
            color=color
        )

    def upload_document(
        self,
        path: pathlib.Path,
        title: str,
        description: str,
        metadata: dict = {}
    ) -> Optional[str]:

        with open(path, 'rb') as doc_file:
            doc_base_64_string = base_64_encode_bytes(doc_file.read())

        filename = path.name

        result = self.client.execute(
            UPLOAD_DOCUMENT,
            variable_values={
                "base64FileString": doc_base_64_string,
                "filename": filename,
                "customMeta": metadata,
                "description": description,
                "title": title
            }
        )

        print(f"Result: {result}")

        if result['uploadDocument']['ok']:
            return result['uploadDocument']['document']['id']
        else:
            return None

    def link_document_to_corpus(
        self,
        corpus_id: str,
        document_ids: list[str]
    ) -> bool:

        result = self.client.execute(
            LINK_DOCUMENTS_TO_CORPUS,
            variable_values={
                "corpusId": corpus_id,
                "documentIds": document_ids
            }
        )
        print(f"Result: {result}")

        return result['linkDocumentsToCorpus']


    def apply_label_to_document(
        self,
        corpus_id: str,
        document_id: str,
        annotation_label_id: str,
        raw_text: str = "",
        json: dict = {},
        page: int= 1
    ) -> Optional[str]:

        result = self.client.execute(
            ANNOTATE_DOCUMENT,
            variable_values={
                "json": json,
                "page": page,
                "rawText": raw_text,
                "corpusId": corpus_id,
                "documentId": document_id,
                "annotationLabelId": annotation_label_id,
            }
        )
        print(f"Result: {result}")

        if result['addAnnotation']['ok']:
            return result['addAnnotation']['annotation']['id']
        else:
            return None

    def upload_and_annotate_document(
        self,
        doc_path: pathlib.Path,
        doc_title: str,
        metadata_to_annotate: dict[str, str],
        doc_labels_to_annotate: list[str]
    ):

        if self.label_set_id is None or self.corpus_id is None:
            raise ValueError("LabelSet and Corpus must be created first.")

        # upload doc first
        doc_id = self.upload_document(
            path=doc_path,
            title=doc_title,
            description="Uploaded via API"
        )

        self.link_document_to_corpus(
            document_ids=[doc_id],
            corpus_id=self.corpus_id
        )

        # For each metadata field, first check annotation label exists and, if not, create
        for annotation_label_name, annotation_value in metadata_to_annotate.items():
            if annotation_label_name in self.label_store:
                annotation_label_id = self.label_store[annotation_label_name]
            else:
                annotation_label_id = self.get_or_create_annotation_label(
                    description="Metadata label",
                    icon=SemanticIcon.TAGS,
                    text=annotation_label_name,
                    label_type=LabelType.METADATA_LABEL,
                    labelset_id=self.label_set_id
                )
                self.label_store[annotation_label_name] = annotation_label_id

            self.apply_label_to_document(
                corpus_id=self.corpus_id,
                document_id=doc_id,
                annotation_label_id=annotation_label_id,
                raw_text=annotation_value
            )

        for doc_label in doc_labels_to_annotate:
            if doc_label in self.label_store:
                doc_label_id = self.label_store[doc_label]
            else:
                doc_label_id = self.create_annotation_label(
                    description="Doc label",
                    icon=SemanticIcon.TAGS,
                    text=doc_label,
                    label_type=LabelType.DOC_TYPE_LABEL,
                    labelset_id=self.label_set_id
                )
                self.label_store[doc_label] = doc_label_id

            self.apply_label_to_document(
                corpus_id=self.corpus_id,
                document_id=doc_id,
                annotation_label_id=doc_label_id,
                raw_text=""
            )
