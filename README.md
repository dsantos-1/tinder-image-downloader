# Tinder Image Downloader (TID)

## Note: this exploit no longer works as of August 19th, 2020, since the Tinder development team has patched the vulnerability. Thank you for your comprehension.

This script downloads the unblurred photos of users that liked your Tinder profile. That feature is available to premium users only.
It exploits a Tinder API vulnerability explained in Sanskar Jethi's [Medium post](https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44).

# Requirements

This has been developed and tested in Python 3.7.2, on Windows 10.

# Installation

1. Clone this repository.
2. Install Python 3.7.2.
3. Install dependencies with `pip install -r requirements.txt`.
4. Find your Tinder X-Auth-Token using the instructions in Sanskar Jethi's [Medium post](https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44).
5. Run the script with `python tinder-img-downloader.py "X-Auth-Token"`, where `X-Auth-Token` is the X-Auth-Token you just found.
    * The script creates a directory called **Unblurred Tinder Photos**, which contains a directory for each user that liked your profile. Each directory contains the pictures of that user.
	
# Credits (in alphabetical order)

* **@jidicula**, whose [script](https://github.com/jidicula/tinderizer) I have studied and took inspiration from to write mine. I also took inspiration from the README.md file of his repository to write mine.
* **Marcelo Duchêne**, for sharing Sanskar's post with me.
* **@stealthanthrax**, for writing and sharing this post.
