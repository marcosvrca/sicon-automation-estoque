
import csv
import re
from pathlib import Path

class SLKConverter:
    def __init__(self, pasta_destino):
        self.pasta_destino = Path(pasta_destino)
        self.coord_pattern = re.compile(r'C;Y(\d+);X(\d+);K(?:"(.*?)"|([^;]*))')

    def converter(self, slk_file):
        csv_file = slk_file.with_suffix(".csv")
        data = {}

        with open(slk_file, 'r', encoding='utf-8', errors='ignore') as infile:
            for line in infile:
                if line.startswith('C;'):
                    match = self.coord_pattern.search(line)
                    if match:
                        y, x = int(match.group(1)), int(match.group(2))
                        value = match.group(3) or match.group(4) or ''
                        data.setdefault(y, {})[x] = value.strip()

        if not data:
            raise ValueError("Nenhum dado encontrado no SLK.")

        max_row, max_col = max(data), max(max(r) for r in data.values())
        with open(csv_file, 'w', newline='', encoding='utf-8-sig') as outfile:
            writer = csv.writer(outfile, delimiter=';')
            for y in range(1, max_row + 1):
                row = [data.get(y, {}).get(x, '') for x in range(1, max_col + 1)]
                if any(cell.strip() for cell in row):
                    writer.writerow(row)

        slk_file.unlink()
        print(f"✔ CSV gerado: {csv_file}")
        return csv_file
