#  Copyright (C) 2022  John Scrudato / Gordium Knot Inc. d/b/a OpenSource.Legal
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import pathlib
from typing import Optional

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from client.utils import package_file_into_base64
from .mutations import CREATE_LABELSET, CREATE_CORPUS


class OpenContractsClient:

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
    ) -> str:
        """
        Create a labelset.

        :param title: Title of labelset
        :param description: Description
        :param icon_path: Path to local icon file to upload
        :param filename: Name to give icon
        :return: Id of created labelset or None if creation failed.
        """

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
            return result['createLabelset']['obj']['id']
        else:
            return None

    def create_corpus(
        self,
        description: str,
        icon_path: pathlib.Path,
        labelset_id: str,
        title: str
    ) -> Optional[str]:

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

        print(result)

        if result['createCorpus']['ok']:
            return result['createCorpus']['objId']
        else:
            return None