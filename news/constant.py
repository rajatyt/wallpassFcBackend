from django.utils.translation import gettext_lazy as _

STAFF_TYPE = [("owner", _('Owner')),
              ("manager", _('Manager')),
              ]

TEAM = [('Goalkeepers', _('Goalkeepers')),
        ('Defenders', _('Defenders')),
        ('Midfielders', _('Midfielders')),
        ('Forwards', _('Forwards')),
        ('CoachingStaff', _('CoachingStaff'))]

NEWS = [('Overall', _('Overall')),
        ('Academy', _('Academy'))]

CATEGORY = [('under18', _('under18')),
            ('under15', _('under15')),
            ('under13', _('under13'))]

# POSITION = [('Goalkeepers', _('Goalkeepers')),
#             ('Defenders', _('Defenders')),
#             ('Midfielders', _('Midfielders')),
#             ('Forwards', _('Forwards'))]
