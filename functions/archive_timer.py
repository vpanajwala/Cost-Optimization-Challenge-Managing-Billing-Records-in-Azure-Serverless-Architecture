def archive_old_records():
    records = query_cosmos("SELECT * FROM c WHERE c.timestamp < (GetCurrentTime() - 90 days)")
    for record in records:
        write_blob(f"{record['id']}.json", record)
        delete_cosmos_record(record["id"])
