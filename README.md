# Django-Stripe Subscription App
A simple Django-Stripe subscription application that listens to live events. We'll manually handle Stripe integrations instead of relying on dj-stripe. And use Postgresql database to manage, store and retrieve user data. 

<br>

**To run this locally, run these commands:**

```html
git clone https://github.com/aqeeladil/django-user-app.git
cd django-user-app
virtualenv venv
pip install -r requirements.txt    (OR pip install django django-environ stripe psycopg2-binary)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Now open http://127.0.0.1:8000/ in your browser to view this project

<br>
**To listen to stripe events, run these commands :**

```html
stripe login
stripe listen --forward-to localhost:8000/subscriptions/webhooks/stripe/
stripe trigger invoice.payment_succeeded
stripe trigger invoice.payment_failed
stripe trigger customer.subscription.updated
stripe trigger customer.subscription.deleted

```
<br><br>







        
