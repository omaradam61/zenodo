"""
  Copyright 2018 INFN (Italy)

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

__author__ = 'marco'

from flask import Blueprint, current_app, redirect, request, url_for
from flask_security import login_user
from invenio_accounts.models import User
from invenio_oauthclient.utils import get_safe_redirect_target


blueprint = Blueprint(
    'zenodo_webauthclient',
    __name__,
    url_prefix='/webauth'
)

@blueprint.route('/login')
def login():
    user = request.environ.get(current_app.config.get('WEBAUTHCLIENT_REMOTE_USER'))
    mail = request.environ.get(current_app.config.get('WEBAUTHCLIENT_REMOTE_MAIL'))
    current_app.logger.info('Try to authenticate %s with mail %s'%(user, mail))
    user = User.query.filter_by(email="info@zenodo.org").one_or_none()

    if user is not None:
        pass
    login_user(user, remember=False)
    next = request.args.get('next')

    return redirect(next)
