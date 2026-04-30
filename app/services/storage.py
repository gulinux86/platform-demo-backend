from google.cloud import storage


def upload_file(bucket_name: str, destination: str, data: bytes, content_type: str) -> str:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination)
    blob.upload_from_string(data, content_type=content_type)
    return f"gs://{bucket_name}/{destination}"


def list_files(bucket_name: str, prefix: str = "") -> list[dict]:
    client = storage.Client()
    blobs = client.list_blobs(bucket_name, prefix=prefix)
    return [
        {"name": b.name, "size": b.size, "updated": b.updated.isoformat()}
        for b in blobs
    ]
