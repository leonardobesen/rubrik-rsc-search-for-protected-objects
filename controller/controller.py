import logging
import os
import sys
import configuration.configuration as conf
from model.protected_object import ProtectedObject
import data.data_parser as data_parser

logger = logging.getLogger(__name__)


def show_menu(access_token: str):
    """Show user a menu to select cluster(s)."""
    clusters = data_parser.get_all_cluster_info(access_token)

    if not clusters:
        print("No clusters available.")
        return []

    print("Select the numbers of clusters you want to search the objects (comma-separated for multiple):")
    for idx, cluster in enumerate(clusters):
        print(f"{idx + 1}. {cluster.name}")

    selection = input("Your choice: ")

    try:
        selected_indices = [int(i.strip()) - 1 for i in selection.split(",")]
    except ValueError:
        print("Invalid input. Please enter only numbers separated by commas.")
        return []

    valid_indices = [i for i in selected_indices if 0 <= i < len(clusters)]
    if not valid_indices:
        print("No valid selections.")
        return []

    selected_ids = [clusters[i].id for i in valid_indices]
    return selected_ids


def parse_csv_files():
    # Ensure the directory exists
    directory = conf.report_input_path()

    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        sys.exit(1)

    # List all .csv files
    csv_files = [f for f in os.listdir(
        directory) if f.lower().endswith('.csv')]

    if not csv_files:
        print(f"No CSV files found in: {directory}")
        sys.exit(1)

    print("Select a CSV file to use:")
    for idx, filename in enumerate(csv_files):
        print(f"{idx + 1}. {filename}")

    try:
        selection = int(input("Your choice: ")) - 1
        if selection < 0 or selection >= len(csv_files):
            print("Invalid selection.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

    selected_file = os.path.join(directory, csv_files[selection])
    print(f"You selected: {selected_file}")

    # Read file line-by-line as hostnames
    try:
        with open(selected_file, mode='r', encoding='utf-8') as f:
            hostnames = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Failed to read CSV file: {e}")
        sys.exit(1)

    return hostnames


def search_list_objects(access_token: str,
                        selected_clusters: list[str],
                        csv_data: str) -> list[ProtectedObject]:
    objects = data_parser.get_all_protected_objects(
        access_token, selected_clusters, csv_data
    )

    return objects
