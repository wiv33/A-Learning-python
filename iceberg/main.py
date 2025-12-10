# uv run python main.py
from pyiceberg.catalog import load_catalog


def delete_table_data():
    catalog = load_catalog(
        "nessie",
        **{
            "type": "rest",
            "uri": "http://nessie.datalake.svc.cluster.local:19120/iceberg/main",
        },
    )


    tables_to_truncate = [
        ("order_item_summary", "order_item_region"),
        ("order_item_summary", "order_item_summary_daily"),
        ("order_item_summary", "orderer_category_dim"),
        ("order_item_summary", "orderer_dim"),
    ]

    for namespace, table_name in tables_to_truncate:
        table_id = f"{namespace}.{table_name}"
        try:
            table = catalog.load_table((namespace, table_name))
            # Delete all rows
            table.delete(delete_filter="true")
            print(f"Deleted all data from: {table_id}")
        except Exception as e:
            print(f"Failed to delete data from {table_id}: {e}")

    catalog.close()


if __name__ == "__main__":
    delete_table_data()