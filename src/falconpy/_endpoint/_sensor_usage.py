"""Internal API endpoint constant library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

_sensor_usage_endpoints = [
  [
    "GetSensorUsageWeekly",
    "GET",
    "/billing-dashboards-usage/aggregates/weekly-average/v1",
    "Fetches weekly average. Each data point represents the average of how many unique AIDs were seen per week "
    "for the previous 28 days.",
    "sensor_usage",
    [
      {
        "type": "string",
        "description": "The FQL search filter. Allowed fields:\n\"event_date\" : A specified date that will be "
        " final date of the results returned. Specified date cannot be after the default.\n\tFormat: "
        "'2024-06-11'\n\tDefault: the current date, minus 2 days, in UTC\n\"period\" : An integer surrounded by single "
        "quotes representing the number of days to return.\n\tFormat: '30'\n\tDefault: '28'\n\tMinimum: '1'\n\tMaximum: "
        " '395'\n\"selected_cids\" : A comma separated list of CIDs to return data for. Caller must be a parent CID or "
        "have special access enabled.\n\tFormat: 'cid_1,cid_2,cid_3'\n\tDefault: for parent CIDs the default is the "
        "parent and all children, otherwise the current CID",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
