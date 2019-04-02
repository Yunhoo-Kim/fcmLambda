from pyfcm import FCMNotification

def fcmPush(event, context):
    fcm = FCMNotification(api_key="API-KEY")
  
    tokens = event.get("tokens", [])
    msg = event.get("msg", "")
    msg_data = event.get("msg_data", {})

    fcm.notify_multiple_devices(
            registration_ids=tokens,
            message_body=msg,
            data_message=msg_data,
            content_available=True,
            sound="default"
        )
    return msg
