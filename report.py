import base64
import os
from io import BytesIO

import altair
import altair_saver
import numpy
import pandas

# Create an altair chart
x, y = numpy.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2
source = pandas.DataFrame({"x": x.ravel(), "y": y.ravel(), "z": z.ravel()})
chart = altair.Chart(source).mark_rect().encode(x="x:O", y="y:O", color="z:Q")

# Save it to PNG in a bytes buffer
b = BytesIO()
altair_saver.save(chart, b, fmt="png", method="node")

# Construct a data url for the image
b.seek(0)
data = base64.b64encode(b.read())
url = f"data:image/png;base64,{data.decode('utf8')}"

if "GITHUB_STEP_SUMMARY" in os.environ:
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        f.write(
            f"""
# My Image

![image]({url})
![image2](https://www.randomkittengenerator.com/cats/92703.1.jpg)
"""
        )

print(url)
