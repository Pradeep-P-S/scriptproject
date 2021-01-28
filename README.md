# Mathematical Calculations using JavaScript
## AIM:
To design a website to calculate the area of a triangle and volume of a cylinder using JavaScript.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Write JavaScript to perform calculations.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.


## PROGRAM:

### cylinder.html:
```
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>VOLUME OF THE CYLINDER</title>
    <link rel="stylesheet" href="{% static 'css/cylinder.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
                VOLUME OF THE CYLINDER
            </div>
            <div class="content">
                <form action="" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_a">BASE=</label>
                        <input type="text" name="value_a" id="value_a">
                    </div>
                    <div  class="forminput">
                        <label for="value_b">HEIGHT=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>                    
                    <div class="forminput">
                        <button type="button" name="button_add" id="button_add">CALCULATE</button>
                    </div>
                    <div  class="forminput">
                        <label for="value_c">RESULT=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>                   
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/mathscript.js"></script>
</body>

</html>
```

### triangle.html:
```

{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>AREA of TRIANGLE</title>
    <link rel="stylesheet" href="{% static 'css/cylinder.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
                AREA OF TRIANGLE
            </div>
            <div class="content">
                <form action="" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_b">Base=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>
                    <div  class="forminput">
                        <label for="value_h">Height=</label>
                        <input type="text" name="value_h" id="value_h">
                    </div>                    
                    <div class="forminput">
                        <button type="button" name="button_calculate" id="button_calculate">Calculate</button>
                    </div>
                    <div class="forminput">
                        <label for="value_c">Area=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/mathscript1.js/"></script>
</body>
</html>
```


## OUTPUT:

![output](./static/image/vocoutput.jpg)

![output](./static/image/aotoutput.jpg)

## VALIDATOR:

![output](./static/image/valvoc.jpg)

![output](./static/image/valaot.jpg)


## RESULT:

Thus a website is designed for area of triangle  is hosted in the URL http://pradeep.student.saveetha.in:8000/triangle/ and volume of cylinder is hosted in the URL http://pradeep.student.saveetha.in:8000/cylinder/ HTML code is validted.