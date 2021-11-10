import json

with open("ssci.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("ssci.opml", "w", encoding="utf-8") as f:
    f.write(r'''<?xml version="1.0" encoding="UTF-8"?>''')
    f.write("\n")
    f.write(r'''<opml version="1.0">''')
    f.write("\n")
    f.write(" " * 2)
    f.write("<head>")
    f.write("\n")
    f.write(" " * 4)
    f.write("<title>generated by Zheng Shuai</title>")
    f.write("\n")
    f.write(" " * 2)
    f.write("</head>")
    f.write("\n")
    f.write(" " * 2)
    f.write("<body>")
    f.write("\n")
    f.write(" " * 4)
    f.write(r'''<outline text="SSCI" title="SSCI">''')

    for journal in data:
        xmlUrl = data[journal][0]
        htmlUrl = data[journal][1]
        f.write("\n")
        f.write(" " * 6)
        f.write("<outline text=\"" + journal + "\" title=\"" + journal + "\" type=\"rss\" xmlUrl=\"" + xmlUrl + "\" htmlUrl=\"" + htmlUrl + "\"/>")
    
    f.write("\n")
    f.write(" " * 4)
    f.write("</outline>")
    f.write("\n")
    f.write(" " * 2)
    f.write("</body>")
    f.write("\n")
    f.write("</opml>")
