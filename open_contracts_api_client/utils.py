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
import base64
import random

from pathlib import Path


def package_file_into_base64(file_path: Path) -> str:
    return base64.b64encode(file_path.open("rb").read()).decode("utf-8")


def random_hex_color() -> str:
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


def base_64_encode_bytes(doc_bytes: bytes):
    """
    Given bytes, encode base64 and utf-8
    """
    base64_encoded_data = base64.b64encode(doc_bytes)
    base64_encoded_message = base64_encoded_data.decode("utf-8")
    return base64_encoded_message
