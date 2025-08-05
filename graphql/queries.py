from configuration.configuration import get_excluded_clusters_uuids


def all_cluster_info_query() -> tuple[str, dict]:
    variables = {
        "filter": {
            "productFilters": [
                {
                    "productType": "CDM"
                }
            ],
            "excludeId": get_excluded_clusters_uuids()
        }
    }

    query = f"""query ListAllClustersInfo($filter: ClusterFilterInput,$sortBy: ClusterSortByEnum = ClusterName){{
      allClusterConnection(filter: $filter, sortBy: $sortBy){{
        nodes{{
          id
          name
          state{{
            connectedState
          }}
        }}
      }}
    }}"""

    return query, variables


def search_object(name: str, cluster_ids: list[str]) -> tuple[str, dict]:
    variables = {
        "filter": [
            {
                "field": "LOCATION",
                "texts": [
                    name
                ]
            },
            {
                "field": "CLUSTER_ID",
                "texts": cluster_ids
            },
            {
                "field": "IS_PROTECTED",
                "texts": [
                    "true"
                ]
            },
            {
                "field": "IS_GHOST",
                "texts": [
                    "false"
                ]
            },
            {
                "field": "IS_ACTIVE",
                "texts": [
                    "true"
                ]
            }
        ],
        "sortBy": "NAME",
        "sortOrder": "ASC",
        "first": 10
    }

    query = f"""query GlobalSearchObjectQuery($first: Int!, 
    $filter: [Filter!]!, 
    $sortBy: HierarchySortByField, 
    $sortOrder: SortOrder, 
    $after: String) {{
      globalSearchResults(
        first: $first
        filter: $filter
        sortBy: $sortBy
        sortOrder: $sortOrder
        after: $after
      ) {{
        nodes {{
        	id
        	name
        	objectType
          effectiveSlaDomain {{
            id
            name
          }}
        }}
      }}
    }}"""

    return query, variables
