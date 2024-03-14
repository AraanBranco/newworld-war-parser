from recognition.RecMain import RecMain

image_folder = './images'
csv = './results.csv'

if __name__ == "__main__":
    RecMain(image_folder=image_folder, csv_file=csv).run()