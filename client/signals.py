# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from client.models import Order
# from job.views import get_filtered_workers
#
#
# @receiver(m2m_changed, sender=Order.job_id.through)
# def send_order_notification(sender, instance, action, **kwargs):
#     """ Orderga aniq job-lar bog'langanda worker-larga xabar yuborish """
#     if action == "post_add":  # Many-to-Many malumotlari saqlangandan keyin
#         channel_layer = get_channel_layer()
#
#         # To'g'ri filterlangan workerlarni olamiz
#         workers = get_filtered_workers(instance)
#
#         for worker in workers:
#             async_to_sync(channel_layer.group_send)(
#                 f"worker_{worker.id}",
#                 {
#                     "type": "send_order_notification",
#                     "order_id": instance.id,
#                     "job_category": instance.job_category.id if instance.job_category else None,
#                     "job_id": list(instance.job_id.values_list("id", flat=True)),
#                     "desc": instance.desc,
#                     "price": instance.price,
#                     "region": instance.region.id if instance.region else None,
#                     "city": instance.city.id if instance.city else None,
#                     "client": str(instance.client) if instance.client else None,
#                     "created_at": instance.created_at.strftime('%Y-%m-%d %H:%M:%S'),
#                 }
#             )
