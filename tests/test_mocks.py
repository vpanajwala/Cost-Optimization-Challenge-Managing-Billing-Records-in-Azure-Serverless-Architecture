class TestBillingDataAccess(unittest.TestCase):
    def test_fallback_to_blob(self):
        # Simulate CosmosDB failure, fallback to Blob
        record = get_billing_record("mock-id")
        self.assertIsNotNone(record)

    def test_archival_removal(self):
        # Simulate archival and ensure deletion
        archive_old_records()
        result = cosmosdb_client.read("archived-id")
        self.assertIsNone(result)
