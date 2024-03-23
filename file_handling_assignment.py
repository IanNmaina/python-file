import csv
with open('my_file.text', 'r') as file:
  reader=csv.reader(file)
  for row in reader:
    print(row)
with open('my_file.text', 'r+') as file:
  writer=csv.writer(file)
  writer.writerow(['Name', 'Age', 'Gender'])
  writer.writerow(['John', '25', 'Male'])
  writer.writerow(['Jane', '30', 'Female'])