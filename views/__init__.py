# -*- coding: utf-8 -*-
import os
module_path = os.path.dirname(os.path.abspath(__file__))
views = [f for f in os.listdir(module_path) if f.endswith('.py') and f != '__init__.py']
__all__ = views
print('Imported views: %s' % ', '.join(views) if views else 'No views avaiable in the views directory.')
