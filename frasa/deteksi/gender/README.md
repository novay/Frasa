Tebak Gender

Client for the gender.frasa.id web service.


Basic usage

Import the Gender class and call its get method with a list of names.

```
from frasa.gender import Gender
print(Gender().get(['Novi', 'Melani', 'Buaya']))
```

```
[{u'count': 1037, u'gender': u'male', u'name': u'Novi', u'probability': 0.45},
 {u'count': 234, u'gender': u'female', u'name': u'Melani', u'probability': 1.0},
 {u'gender': None, u'name': u'Buaya'}]
```

