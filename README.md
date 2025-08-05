# rubrik-rsc-search-for-protected-objects

A tool to search all (protected) objects, such as Oracle Databases, SQL Server Databases and filesets for a given list of hostnames.

## Dependencies

- Python >= 3.11
- pandas
- requests
- tdqm
- numpy

## How to use it

1- Create a JSON file named `config.json` with your Rubrik Security Cloud (RSC) and RSC Service Account information like in the example below and add it inside `configuration` folder:

*config.json*

```json
{
 "client_id": "your_client_id",
 "client_secret": "your_client_secret",
 "name": "name_you_gave",
 "access_token_uri": "https://yourdomain.my.rubrik.com/api/client_token",
 "graphql_url": "https://yourdomain.my.rubrik.com/api/graphql",
 "google_drive_upload_folder_id": ["your_drive_folders_ids_here"],
 "tz_info": "America/Sao_Paulo",
 "excluded_clusters_uuids": ["cluster_uuid_that_you_want_to_exclude"]
}
```

`config.json` parameters explained:

| Key Name                      | Required? | What it does                                                |
| ----------------------------- | --------- | ----------------------------------------------------------- |
| client_id                     | `Yes`     | RSC Service Account Id                                      |
| client_secret                 | `Yes`     | RSC Service Account "password"                              |
| name                          | `Yes`     | RSC Service Account Name                                    |
| access_token_uri              | `Yes`     | On the URL example above replace the inicial domain with your RSC domain |
| graphql_url                   | `Yes`     | On the URL example above replace the inicial domain with your RSC domain |
| tz_info                       | `No`      | Your timezone for date and time convertions, if necessary. If `tz_info` is not declared or left blank (`""`) it will use UTC+0. To select the correct timezone name use `pytz.all_timezones` on a Python Prompt with the lib `pytz` imported |

2- Add your lists of hostname as csv files, they most have only one column with no headers, like the example below, on the folder `reports\input\`.

```
hostname1
hostname2
hostname3
```

3- Download this repository and place in a computer or server that has access to your Rubrik RSC.

4- Run main.py
