import sys
import os




import markdown
from flask import Flask, render_template
import markdown.extensions.fenced_code


from ln import get_info, fee_report

app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("content/index.md", "r")
    md_template_string = markdown.markdown(
        '# header'
        #readme_file.read(), extensions=["fenced_code"]
    )
    app.logger.info(md_template_string)

    #return '<html/> <body> {} </body> </html>'.format(md_template_string)

    data = get_info()

    return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run()