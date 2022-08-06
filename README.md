### How to use

```python
from devlibx_avro_helper.month_data import MonthDataAvroHelper

input = "PAg4LTE23AEIOC0xN94BCDgtMTTYAQg4LTE12gEIOC0xOOABCDgtMTniAQg4LTMw"
        "+AEIOC0zMfoBCDgtMTLUAQg4LTEz1gEIOC0xMNABCDgtMTHSAQY5LTH8AQY5LTL"
        "+AQY5LTOAAgg4LTI38gEGOS00ggIGOC02yAEIOC0yOPQBBjgtN8oBCDgtMjXuAQY4LTjMAQg4LTI28AEGOC05zgEIOC0yOfYBCDgtMjDkAQg4LTIz6gEIOC0yNOwBCDgtMjHmAQg4LTIy6AEAEGhhcmlzaF8x "
helper = MonthDataAvroHelper()
result = helper.process(input)
print(result)

# Result
# {'days': {'8-16': 110, '8-17': 111, '8-14': 108, '8-15': 109, '8-18': 112, '8-19': 113, '8-30': 124, '8-31': 125, '8-12': 106, '8-13': 107, '8-10': 104, '8-11': 105, '9-1': 126, '9-2': 127, '9-3': 128, '8-27': 121, '9-4': 129, '8-6': 100, '8-28': 122, '8-7': 101, '8-25': 119, '8-8': 102, '8-26': 120, '8-9': 103, '8-29': 123, '8-20': 114, '8-23': 117, '8-24': 118, '8-21': 115, '8-22': 116}, 'entity_id': 'harish_1'}
```