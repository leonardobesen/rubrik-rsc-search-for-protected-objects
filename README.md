# rubrik-rsc-search-for-protected-objects

A tool to search selected or all (protected) objects, such as Physical Host, Volume Group, Oracle Databases, SQL Server Databases and Filesets for a given list of hostnames.

## Dependencies

- Python >= 3.14
- pip install requirements.txt

## How to use it

1- Create a JSON file named `config.json` with your Rubrik Security Cloud (RSC) and RSC Service Account information like in the example below and add it inside `configuration` folder:

### config.json

```json
{
 "client_id": "your_client_id",
 "client_secret": "your_client_secret",
 "name": "name_you_gave",
 "access_token_uri": "https://yourdomain.my.rubrik.com/api/client_token",
 "graphql_url": "https://yourdomain.my.rubrik.com/api/graphql",
 "tz_info": "America/Sao_Paulo",
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

2- Add your lists of hostname as csv files, they most have only one column with no headers, like the example below, on the folder `reports\input\`.

```
hostname1
hostname2
hostname3
```

3- Download this repository and place in a computer or server that has access to your Rubrik RSC.

4- Run main.py
