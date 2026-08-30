from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

marker = "/* TNS PERF: mobile hero text stability */"
css = '''\n/* TNS PERF: mobile hero text stability */\n@media(max-width:980px){\n  .hero .sub{\n    font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;\n    font-size:17.5px;\n    line-height:1.7;\n    font-synthesis:none;\n  }\n  .hero .sub b{font-family:inherit;font-weight:600}\n}\n'''

if marker in text:
    print("Mobile hero stability CSS already present; no change needed.")
else:
    needle = "</style>"
    if needle not in text:
        raise SystemExit("Could not find </style> in index.html")
    text = text.replace(needle, css + "\n" + needle, 1)
    path.write_text(text, encoding="utf-8")
    print("Added mobile hero text stability CSS.")
