from devlibx_avro_helper.month_data import MonthDataAvroHelper

base64Str = "BgY3LTMCBjYtNgIGNy01BAAAAAI="
helper = MonthDataAvroHelper()
result = helper.process(base64Str)
print(result)
