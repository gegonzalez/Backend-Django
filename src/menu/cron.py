import json
import logging

import datetime
import requests

from .models import Menu

logger = logging.getLogger(__name__)

def menu_send_job(slack_webhook_url, host):
    """
    Send a reminder to an Slack channel with the Menu of the day
    """
    try:
        menu = Menu.objects.get(published_date=datetime.date.today())

        menu_url = host + 'menu/'+ menu.uuid

        text = f"Hello! This is a reminder for today's Menu! <{menu_url}|Click here> for details!"

        payload = {"text": text}

        response = requests.post(slack_webhook_url, data=json.dumps(payload))

        logger.info('Cronjob message status=%s', response.status_code)
    except Menu.DoesNotExist:
        logger.error('Cronjob message status=failed')
