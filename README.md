# immchiAutoAlbum

## Desciption
This Python script is designed to emulate the smart albums from Google Photos for [Immich](https://github.com/immich-app/immich).
This will aggregate "people" in an album automatically.


## Configuration

The `config.json.example` file contains the following settings:

- `isFirtsRun`: This setting processes all images and adds them to the album; if set to false, only the last 100 pictures are processed.
- `accounts`:  this will be the list of accounts to contribute to the album, each user that uses the app and will contribute to an album is required to generate an API key that will be used to add the photos to the shared album
- `accoutnName`: name of the account, not used for logic just for information
- `apiKey`: user account API key, [follow this instructions of how to generate one](https://immich.app/docs/features/command-line-interface#obtain-the-api-key)
- `url`: URL to the you immich instance in the following format: somelocation.com/api. example: http://127.0.0.1:3001/api
- `albuns`: this will contain the list of albuns that the current account will contribute with photos
- `id`: album ID, this can be seen in the URL when you open a album, example: bbdf5884-925a-40eb-bc4e-ac66a186c82f
- `name`: name of the album, not used for logic just for information
- `persons`: the list of people that the user has in his account and wants to add to the album
- `id`: "people" id, this can be seen in the URL when you open a "people". example: 9cdaf954-9f92-43a8-b79d-4a4f71640db3
- `name`:  name of the person, not used for logic just for information


## How To setup

1. Create a album that you whant to use as the "Smart album" and share it with all the users that should contribute to it.
2. On each user account generate an API key and add that account to the config.
3. for each account added add the album with the correct album ID to the albuns configuration. you can add any amount of albuns
4. for each album added add the people id from that account to the persons configuration. You can add any amount of people to each album
5. repeat this steps for each account that you want.


## How To run

### Run directly
1. Make sure you have Python installed on your system.
3. Update the configuration in the 'config.json' file with your desired settings.
4. Run the script using the following command:

    ```bash
    python ImmichAutoAlbum.py
    ```

### Run Using Docker:

1. Update the `crontab` file with the desired interval for checking the Media, this file will be used by the container to schedule the actions. The current configuration will check every day at midnight:
    
    ```bash
    0 0 * * * /usr/local/bin/python3 /app/ImmichAutoAlbum.py > /proc/1/fd/1 2>/proc/1/fd/2 
    ```

2. Build the Docker image:

    ```bash
    docker build -t immich_auto_album .
    ```

3. Run the Docker container:

    ```bash
    docker run -d --name immich_auto_album immich_auto_album
    ```

