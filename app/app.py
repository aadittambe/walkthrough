import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)


# def get_csv():
#     csv_path = './static/etl_district_full_data.csv'
#     csv_file = open(csv_path, 'r')
#     csv_obj = csv.DictReader(csv_file)
#     csv_list = list(csv_obj)
#     return csv_list


def district_get_csv():
    district_csv_path = './static/etl_district_full_data.csv'
    district_csv_file = open(district_csv_path, 'r')
    district_csv_obj = csv.DictReader(district_csv_file)
    district_csv_list = list(district_csv_obj)
    return district_csv_list


def school_get_csv():
    school_csv_path = './static/etl_school_full_data.csv'
    school_csv_file = open(school_csv_path, 'r')
    school_csv_obj = csv.DictReader(school_csv_file)
    school_csv_list = list(school_csv_obj)
    return school_csv_list


@app.route("/")
def district_index():
    district_template = 'index.html'
    district_object_list = district_get_csv()
    school_template = 'index.html'
    school_object_list = school_get_csv()
    return render_template('index.html', **locals())


@app.route('/district/<district_id>/')
def district_detail(district_id):
    d_template = 'district.html'
    district_object_list = district_get_csv()
    for d_row in district_object_list:
        if d_row['district_id'] == district_id:
            return render_template(d_template, district=d_row, district_object_list=district_get_csv(), school_object_list=school_get_csv())
    abort(404)


@app.route('/school/<school_id>/')
def school_detail(school_id):
    s_template = 'school.html'
    school_object_list = school_get_csv()
    for s_row in school_object_list:
        if s_row['school_id'] == school_id:
            return render_template(s_template, school=s_row)
    abort(404)


@app.template_filter()
def numberFormat(value):
    return format(int(value), ',d')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
