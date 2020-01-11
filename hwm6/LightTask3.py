#######################################################################################################################
# Light. Task 3
# Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
#######################################################################################################################
# In this task I used an example of data related to cars in JSON-format from the site (partially) to make this task
# closer to the reality
# https://github.com/vega/vega/blob/master/docs/data/cars.json
#######################################################################################################################
import datetime


from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docxtpl.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(event, city, date, band_name, band_lineup, duration, set, price):
    return {
        'event': event,
        'city': city,
        'date': date,
        'band_name': band_name,
        'band_lineup': band_lineup,
        'duration': duration,
        'set': set,
        'price': price
    }

def from_template(event, city, date, band_name, band_lineup, duration, set, price, template, signature):
    template = DocxTemplate(template)
    context = get_context(event, city, date, band_name, band_lineup, duration, set, price)

    img_size = Cm(10)  # sets the size of the image
    my_pic = InlineImage(template, signature, img_size)

    context['my_pic'] = my_pic  # adds the InlineImage object to the context

    template.render(context)
    template.save('music_performance' + '_' + str(datetime.datetime.now().date()) + '_offer.docx')

def generate_report(event, city, date, band_name, band_lineup, duration, set, price):
    template = 'my_band_wishlist.docx'
    signature = 'my_pic.png'
    document = from_template(event, city, date, band_name, band_lineup, duration, set,  price, template, signature)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"