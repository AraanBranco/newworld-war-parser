from recognition.GetImagesPaths import GetImagesPathsFromFolder
from recognition.ProcessImages import ProcessImages
from recognition.CreateCsvFile import CreateCsvFile

class RecMain:
    def __init__(self, image_folder, csv_file):
        self.image_folder = image_folder
        self.csv_file = csv_file

    def run(self):
        image_paths = GetImagesPathsFromFolder(self.image_folder).exec()

        results = ProcessImages(image_paths=image_paths).process()

        create_file = CreateCsvFile(results=results, csv_file=self.csv_file).exec()

        if create_file:
            print('CSV file created successfully')
        else:
            print('Error creating CSV file')
