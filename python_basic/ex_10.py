files = ['report.hwp', 'newJeans', 'attention.png', 'ditto.jpg', 'address.xslx']

print(list(filter(lambda x : 'jpg' in x or 'png' in x, files)))