# README
## README.md
# Backend for [tough-dev.school](https://tough-dev.school/)

![CI](https://github.com/tough-dev-school/education-backend/actions/workflows/ci.yml/badge.svg) [![Crossplatform](https://github.com/tough-dev-school/education-backend/actions/workflows/crossplatform.yml/badge.svg)](https://github.com/tough-dev-school/education-backend/actions/workflows/crossplatform.yml)

Django-based production project, integrated with Tinkoff, Dashamail, Postmark, S3 and telegram. Frontend is built on vue.js in the [separate repo](https://github.com/tough-dev-school/lms-frontend-v2).

## Configuration

Configuration is stored in `src/core/.env`, for examples see `src/core/.env.ci`

## Installing on a local machine

This project requires python 3.14. Deps are managed by [uv](https://docs.astral.sh/uv/).

Install requirements:

```bash
uv sync
```

Configure postgres and redis. It's convenient to use docker and docker-compose:

```bash
docker compose up -d
```

If you don't have access to de-anonymized db image use `postgres:13.6-alpine` in `docker-compose.yml` instead:

```yaml
postgres:
    image: postgres:13.6-alpine
    ...
```

Run the server:

```bash
cp src/core/.env.ci src/core/.env

uv run python src/manage.py migrate
uv run python src/manage.py createsuperuser

make server
```

Testing:

```bash
# run lint
make lint

# run unit tests
make test
```

## Backend Code requirements

### Style

* Obey [django's style guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style).
* Configure your IDE to use `ruff` for checking your python code. For running linters manualy, do `make lint`
* Prefer English over your native language in comments and commit messages.
* Commit messages should contain the unique id of issue they are linked to (refs #100500)
* Every model and a model method should have a docstring.

### Code organisation

* KISS and DRY.
* Obey [django best practices](http://django-best-practices.readthedocs.io/en/latest/index.html)
* If you want to implement some business logic — make a service for that. Service examples: [UserCreator](https://github.com/tough-dev-school/education-backend/blob/master/src/apps/users/services/user_creator.py), [OrderCreator](https://github.com/tough-dev-school/education-backend/blob/master/src/apps/orders/services/order_creator.py)
* **No logic is allowed within the views or templates**. Only services and models.
* Use PEP-484 [type hints](https://www.python.org/dev/peps/pep-0484/) when possible.
* Prefer [Manager](https://docs.djangoproject.com/en/dev/topics/db/managers/) methods over static methods.
* Do not use [signals](https://docs.djangoproject.com/en/dev/topics/signals/) for business logic. Signals are good only for notification purposes.
* No l10n is allowed in python code, use [django translation](https://docs.djangoproject.com/en/dev/topics/i18n/translation/).

# File tree
.hadolint.yaml
.yamllint.yml
AGENTS.md
README.md
compose.yml
conftest.py
pyproject.toml
renovate.json
src
  apps
    __init__.py
    a12n
      __init__.py
      admin.py
      api
        forms.py
        serializers.py
        throttling.py
        views.py
      apps.py
      jwt.py
      models.py
      signals
        handlers.py
      tests
        __init__.py
        api
          tests_obtain_jwt_via_passwordless_token.py
          tests_obtain_jwt_via_user_id.py
          tests_obtain_token.py
          tests_password_change.py
          tests_password_reset_confirm.py
          tests_refresh_token.py
          tests_request_password_reset.py
          tests_request_passwordless_token.py
        tests_jwt_blacklisting.py
        tests_passwordless_token_absolute_url.py
      urls.py
      utils.py
    amocrm
      __init__.py
      apps.py
      client
        __init__.py
        client.py
        http.py
      dto
        __init__.py
        catalogs.py
        customer.py
        groups.py
        lead.py
        lead_note.py
        lead_task.py
        pipelines.py
        product.py
        transaction.py
        user_operator.py
      exceptions.py
      ids.py
      models
        __init__.py
        amocrm_course.py
        amocrm_order_lead.py
        amocrm_order_transaction.py
        amocrm_product_group.py
        amocrm_user.py
      services
        __init__.py
        access_token_getter.py
        course_pusher.py
        group_pusher.py
        orders
          order_pusher.py
          order_returner.py
          order_task_creator.py
        user_pusher.py
      tasks.py
      tests
        __init__.py
        conftest.py
        dto
          conftest.py
          tests_catalogs.py
          tests_customer.py
          tests_groups.py
          tests_lead.py
          tests_lead_note.py
          tests_lead_task.py
          tests_pipelines.py
          tests_product.py
          tests_transaction.py
          tests_user_operator.py
        http
          __init__.py
          tests_http.py
        ids
          tests_b2c_pipeline_id.py
          tests_catalog_id.py
          tests_contact_fields_ids.py
          tests_product_fields_ids.py
        services
          order
          tests_course_pusher.py
          tests_group_pusher.py
          tests_user_pusher.py
        tests_access_token_getter.py
      types.py
    b2b
      __init__.py
      admin
        __init__.py
        customers.py
        deals
          __init__.py
          actions.py
          admin.py
          forms.py
        students.py
      apps.py
      factory.py
      models
        __init__.py
        customer.py
        deal.py
        student.py
      services
        __init__.py
        bulk_student_creator.py
        deal_completer.py
        deal_creator.py
        deal_currency_changer.py
      tests
        conftest.py
        deal_completer
          conftest.py
          test_deal_completer.py
          test_deal_completer_existing_order_assignment.py
          test_deal_completer_happiness_message.py
          test_deal_completer_new_order_creation.py
          test_deal_completer_shipping_without_payment.py
        test_bulk_student_creator.py
        test_deal_creator_service.py
        test_deal_currency_changer.py
        test_deal_status_str.py
      utils.py
    banking
      __init__.py
      admin
        __init__.py
        acquiring_percent.py
        currency_rate.py
      api
        serializers.py
      apps.py
      b2b.py
      base.py
      currency.py
      exceptions.py
      factory.py
      fixtures.py
      models.py
      price_calculator.py
      selector.py
      tests
        __init__.py
        tests_get_bank.py
        tests_get_bank_or_default.py
        tests_get_currency_rate.py
        tests_get_id.py
        tests_price_calculator.py
      urls.py
      zero_price_bank.py
    chains
      __init__.py
      admin
        __init__.py
        chain.py
        forms.py
        message.py
      apps.py
      models
        __init__.py
        chain.py
        message.py
        progress.py
      services
        __init__.py
        chain_sender.py
        message_sender.py
      tasks.py
      tests
        __init__.py
        chain_sender
          conftest.py
          test_chain_sender_integrational.py
          test_chain_tasks.py
          test_sending_next_messages.py
          test_sending_root_messages.py
        conftest.py
        message_sender
          conftest.py
          test_sending_message.py
        test_message_time_to_send.py
        unit
          test_chain_queryset_active.py
          test_chain_queryset_editable.py
          test_progress_get_last.py
    dashamail
      __init__.py
      apps.py
      directcrm
        events
          __init__.py
          base.py
          order_created.py
          order_paid.py
      enabled.py
      exceptions.py
      fixtures.py
      lists
      services
      tasks.py
      tests
    diplomas
    homework
    lms
    mailing
    notion
    orders
    products
    stripebank
    studying
    tinkoff
    users
  core
  manage.py