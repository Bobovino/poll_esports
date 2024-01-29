from mwrogue.esports_client import EsportsClient
import urllib.request
import os

def main():

    def get_filename_url_to_open(site: EsportsClient, filename, team, width=None):
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


        folder_path = "./TeamIcons"
         # Constructing the full file path
        full_file_path = os.path.join(folder_path, team + '.png')

        # Ensure the folder exists
        os.makedirs(folder_path, exist_ok=True)

        # Download and save the image
        urllib.request.urlretrieve(url, full_file_path)



    teams = ["Dplus KIA"]

    site = EsportsClient("lol")
    for team in teams:
        url = f"{team}logo square.png"
        get_filename_url_to_open(site, url, team)


if __name__ == "__main__":
    main()