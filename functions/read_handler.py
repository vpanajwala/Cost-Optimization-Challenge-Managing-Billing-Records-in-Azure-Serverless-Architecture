def get_billing_record(record_id):
    try:
        return cosmosdb_client.read(record_id)
    except cosmosdb_client.NotFoundError:
        return blob_storage_client.read_blob(f"{record_id}.json")
