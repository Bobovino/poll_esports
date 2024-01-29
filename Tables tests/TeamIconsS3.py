import boto3

def upload_to_s3(url, bucket_name, s3_filename):
    s3_client = boto3.client('s3')
    with urllib.request.urlopen(url) as f:
        s3_client.upload_fileobj(f, bucket_name, s3_filename)

def get_filename_url_to_s3(site: EsportsClient, filename, team, bucket_name, width=None):
    response = site.client.api(
        action="query",
        format="json",
        titles=f"File:{filename}",
        prop="imageinfo",
        iiprop="url",
        iiurlwidth=width,
    )

    image_info = next(iter(response["query"]["pages"].values()))["imageinfo"][0]

    if width:
        url = image_info["thumburl"]
    else:
        url = image_info["url"]

    upload_to_s3(url, bucket_name, team + '.png')

# Usage
bucket_name = "your-s3-bucket-name"
site = EsportsClient("lol")
for team in teams:
    url = f"{team}logo square.png"
    get_filename_url_to_s3(site, url, team, bucket_name)
