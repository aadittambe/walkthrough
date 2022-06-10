from flask_frozen import Freezer
from app import app, district_get_csv, school_get_csv
freezer = Freezer(app)


@freezer.register_generator
def district_detail():
    for d_row in district_get_csv():
        yield {'district_id': d_row['district_id']}


@freezer.register_generator
def school_detail():
    for s_row in school_get_csv():
        yield {'school_id': s_row['school_id']}


if __name__ == '__main__':
    freezer.freeze()
