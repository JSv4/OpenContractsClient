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
from gql import gql


CREATE_CORPUS = gql("""  mutation (
    $description: String
    $icon: String
    $labelSet: String
    $title: String
  ) {
    createCorpus(
      description: $description
      icon: $icon
      labelSet: $labelSet
      title: $title
    ) {
      ok
      message
      objId
    }
  }
""")

CREATE_LABELSET = gql("""
  mutation (
    $title: String!
    $description: String
    $icon: String
    $filename: String!
  ) {
    createLabelset(
      title: $title
      description: $description
      base64IconString: $icon
      filename: $filename
    ) {
      ok
      message
      obj {
        id
        title
        description
        icon
      }
    }
  }
""")

CREATE_ANNOTATION_LABEL_FOR_LABEL_SET = gql("""
mutation (
    $color: String
    $description: String
    $icon: String
    $text: String
    $labelType: String
    $labelsetId: String!
  ) {
    createAnnotationLabelForLabelset(
      color: $color
      description: $description
      icon: $icon
      text: $text
      labelType: $labelType
      labelsetId: $labelsetId
    ) {
      ok
      message
    }
  }
""")

UPLOAD_DOCUMENT = gql("""
  mutation (
    $base64FileString: String!
    $filename: String!
    $customMeta: GenericScalar!
    $description: String!
    $title: String!
  ) {
    uploadDocument(
      base64FileString: $base64FileString
      filename: $filename
      customMeta: $customMeta
      description: $description
      title: $title
    ) {
      document {
        id
        icon
        pdfFile
        title
        description
        backendLock
        docAnnotations {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
""")

LINK_DOCUMENTS_TO_CORPUS = gql("""
  mutation ($corpusId: String!, $documentIds: [String]!) {
    linkDocumentsToCorpus(corpusId: $corpusId, documentIds: $documentIds) {
      ok
      message
    }
  }
""")

ANNOTATE_DOCUMENT = gql("""
  mutation (
    $json: GenericScalar!
    $page: Int!
    $rawText: String!
    $corpusId: String!
    $documentId: String!
    $annotationLabelId: String!
  ) {
    addAnnotation(
      json: $json
      page: $page
      rawText: $rawText
      corpusId: $corpusId
      documentId: $documentId
      annotationLabelId: $annotationLabelId
    ) {
      ok
      annotation {
        id
        page
        bounds: boundingBox
        rawText
        json
        isPublic
        myPermissions
        annotationLabel {
          id
          icon
          description
          color
          text
          labelType
        }
        sourceNodeInRelationships {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
""")