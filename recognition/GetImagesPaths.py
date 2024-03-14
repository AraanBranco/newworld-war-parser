import os

class GetImagesPathsFromFolder:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.ext_available = ['png', 'jpg']

    def exec(self):
        if not os.path.exists(self.image_folder):
            raise FileNotFoundError(f"The folder '{self.image_folder}' does not exist.")

        images_path = []
        allFiles = os.listdir(self.image_folder)

        for file in allFiles:
            file = file.strip()
            ext = file.split('.')[1:]
            if ext[0].lower() in self.ext_available:
                images_path.append(self.image_folder + '/' + file)

        return images_path
