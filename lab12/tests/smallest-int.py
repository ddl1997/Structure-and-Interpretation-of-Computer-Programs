test = {
  'name': 'smallest-int',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int;
          11/7/2017 20:27:19|19
          11/7/2017 20:28:25|19
          11/7/2017 20:45:09|19
          11/7/2017 20:54:01|19
          11/7/2017 20:57:09|19
          11/7/2017 21:04:57|19
          11/7/2017 22:57:12|19
          11/8/2017 23:24:19|19
          11/8/2017 8:50:46|19
          11/7/2017 21:08:12|20
          11/7/2017 20:55:29|21
          11/7/2017 21:50:36|21
          11/7/2017 22:08:12|22
          11/7/2017 22:33:17|22
          11/8/2017 14:28:04|22
          11/10/2017 0:14:55|23
          11/7/2017 20:31:06|23
          11/7/2017 20:31:30|23
          11/7/2017 20:31:52|23
          11/7/2017 20:34:41|23
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}