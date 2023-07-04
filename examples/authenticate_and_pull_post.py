import json
import os

import dotenv
from pythorhead import Lemmy

if __name__ == "__main__":

    # load the environment file
    dotenv.load_dotenv(".env")

    lemmy = Lemmy(
        os.environ["LEMMY_INSTANCE"],
    )

    lemmy.log_in(
        os.environ["LEMMY_USERNAME"],
        os.environ["LEMMY_PASSWORD"],
    )

    post_id = lemmy.post.list()[0]["post"]["id"]

    post = lemmy.post.get(post_id)

    print(json.dumps(post, indent=4))
