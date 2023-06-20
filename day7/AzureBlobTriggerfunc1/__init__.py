import logging

import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage

def main(myblob: func.InputStream):
    # Get the blob name and size
    blob_name = myblob.name
    blob_size = myblob.length

    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    # Send a message to the Service Bus topic

    message = ServiceBusMessage(f"New blob uploaded: {blob_name} ({blob_size} bytes)")

    servicebus_client = ServiceBusClient.from_connection_string('Endpoint=sb://eventtriggerns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=pVxopB6SiBX/PIItmybyFcHhw2PFeKbWt+ASbFHpG4M=')

    with servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name='event-topic1')
        sender.send_messages(message)
        logging.info("Message sent to the Service Bus topic")
