import click
import os
from datetime import datetime
from PIL import Image
import shutil

POSTS_DIR = "_posts"
IMAGES_DIR = "assets/images"


def create_post(title, image_description, image_path):
    # create new post file
    today = datetime.today().strftime('%Y-%m-%d')
    post_filename = f"{today}-{title.lower().replace(' ', '')}.md"
    post_path = os.path.join(POSTS_DIR, post_filename)
    with open(post_path, "w") as post_file:
        post_file.write(f"---\nlayout: post\ntitle:  \"{title}\"\ncategories: [ PleinAir ]\nimage: {os.path.join(IMAGES_DIR, os.path.basename(image_path))}\nbeforetoc: \"{image_description}\"\ntoc: true\n---\n\n{image_description}")

    # copy image to assets/images directory
    shutil.copy(image_path, os.path.join(IMAGES_DIR, os.path.basename(image_path)))

    # get image description
    click.echo(f"Added post {post_filename} with image {os.path.basename(image_path)} and description: {image_description}")

@click.command()
@click.option('--title', prompt='Post title', help='Title of the post')
@click.option('--description', prompt='Description', help='Title of the post')
def main(title, description):
    # open file picker dialog and get path to selected file
    from tkinter.filedialog import askopenfilename
    image_path = askopenfilename()
    create_post(title, description, image_path)

if __name__ == '__main__':
    main()
