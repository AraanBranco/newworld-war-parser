from paddleocr import PaddleOCR

class ProcessImages:
    def __init__(self, image_paths):
        self.image_paths = image_paths
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def process(self):
        results = []

        for image_path in self.image_paths:
            result = self.ocr.ocr(img=image_path, cls=False, det=True, rec=True, inv=True, bin=False)
            result = self.generateRows(result)
            results.extend(result)

        clean_results = self.remove_duplicate_player(results)
        results_ordered = sorted(clean_results, key=lambda d: d['rank'])
        return results_ordered

    def generateRows(self, result):
        lines = result[0]
        text = [line[1][0] for line in lines]
        rows = []
        row = {}

        j = 1
        for i in range(len(text)):
            if j == 8:
                # Damage
                row['damage'] = text[i]

                rows.append(row)
                row = {}
                j = 1
            else:
                # Rank
                if j == 1:
                    row['rank'] = '{:0>2}'.format(int(text[i]))
                    j += 1
                    continue

                # Name
                if j == 2:
                    if len(text[i]) < 3:
                        continue

                    row['name'] = text[i]
                    j += 1
                    continue

                # Score
                if j == 3:
                    row['score'] = text[i]
                    j += 1
                    continue

                # Kills
                if j == 4:
                    row['kills'] = text[i]
                    j += 1
                    continue

                # Deaths
                if j == 5:
                    row['deaths'] = text[i]
                    j += 1
                    continue

                # Assists
                if j == 6:
                    row['assists'] = text[i]
                    j += 1
                    continue

                # Healing
                if j == 7:
                    row['healing'] = text[i]
                    j += 1
                    continue

        return rows

    def remove_duplicate_player(self, results):
        players = []
        clean_results = []

        for result in results:
            if result['name'] not in players:
                players.append(result['name'])
                clean_results.append(result)

        return clean_results