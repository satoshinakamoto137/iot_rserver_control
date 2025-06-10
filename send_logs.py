from azure.storage.blob import BlobServiceClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def write_log_to_azure(log_message):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_BLOB_CONTAINER", "message")
    blob_name = os.getenv("AZURE_BLOB_NAME", "rmlogs.txt")

    if not connection_string:
        print("⚠️ Azure connection string not found in environment!")
        return

    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)

        existing_content = ""
        if blob_client.exists():
            existing_content = blob_client.download_blob().readall().decode('utf-8')

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_entry = f"[{timestamp}] {log_message}"
        updated_content = f"{existing_content}\n{new_entry}"

        blob_client.upload_blob(updated_content, overwrite=True)
        print("✅ Log updated successfully!")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

"""
🔧 Part of the Tenmei.tech IoT Initiative
Visit us at: https://tenmei.tech

© 2025 Tenmei.tech — All rights reserved.
This script is provided under the MIT License.
"""

