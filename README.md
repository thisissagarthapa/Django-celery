
# Django Celery Project

This project demonstrates the integration of Django with Celery for asynchronous task handling and scheduling.

## Features
- Asynchronous task execution using Celery
- Periodic tasks scheduling with django-celery-beat
- Task result tracking with django-celery-results
- Redis as a message broker

## Requirements
Ensure you have the following installed:
- Python (3.8+)
- Redis server

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/thisissagarthapa/django-celery.git
   cd django-celery
   ```

2. **Create a virtual environment** and activate it:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For Linux/MacOS
   myenv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**:

   Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Redis**:
   
   Ensure Redis is installed and running. You can install Redis via:
   
   - **Linux**: `sudo apt-get install redis`
   - **Mac**: `brew install redis`
   - **Windows**: [Download Redis](https://github.com/microsoftarchive/redis/releases)

   Start the Redis server by running:
   
   ```bash
   redis-server
   ```

5. **Run Celery**:
   
   Start a Celery worker with the following command:

   ```bash
   celery -A myCelery worker --loglevel=info
   ```

   Start the Celery beat scheduler:

   ```bash
   celery -A myCelery beat --loglevel=info
   ```

6. **Run Django Development Server**:
   
   ```bash
   python manage.py runserver
   ```

## Celery Tasks

This project includes example tasks in `myapp/tasks.py`. Tasks can be enqueued as follows:

```python
from myapp.tasks import add
result = add.delay(10, 20)  # Asynchronous task execution
```

You can track task results and states using the task ID.

## Beat Scheduling

Periodic tasks can be configured in `settings.py` using either timedelta or crontab for scheduling. Here's an example using crontab:

```python
app.conf.beat_schedule = {
    'every-minute-task': {
        'task': 'myapp.tasks.clear_session_cache',
        'schedule': crontab(minute='*/1'),
        'args': ('1111',),
    }
}
```

## Project Structure

```
myCelery/
├── myapp/
│   ├── tasks.py  # Celery tasks
│   ├── views.py  # Django views
├── myCelery/
│   ├── __init__.py
│   ├── celery.py  # Celery configuration
├── requirements.txt  # Project dependencies
├── manage.py  # Django management commands
```

## Dependencies

This project uses the following major dependencies:

- **Django 5.1.1**: Web framework.
- **Celery 5.4.0**: For task handling.
- **django-celery-beat 2.7.0**: Periodic task scheduler.
- **django-celery-results 2.5.1**: To store task results.
- **Redis 5.0.8**: Message broker.
- **Python-crontab 3.2.0**: Cron job manager for scheduling.

Make sure to have Redis installed and running.

## License
This project is licensed under the MIT License.
