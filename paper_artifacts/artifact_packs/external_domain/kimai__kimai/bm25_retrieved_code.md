# README-derived retrieval query
kimai kimai ## README.md
<p align="center">
    <img src="https://raw.githubusercontent.com/kimai/images/main/repository-header.png" alt="Kimai logo">
</p>

<p align="center">
    <a href="https://github.com/kimai/kimai/actions"><img alt="CI Status" src="https://github.com/kimai/kimai/actions/workflows/testing.yaml/badge.svg"></a>
    <a href="https://codecov.io/gh/kimai/kimai"><img alt="Code Coverage" src="https://codecov.io/gh/kimai/kimai/branch/main/graph/badge.svg"></a>
    <a href="https://packagist.org/packages/kimai/kimai"><img alt="Latest stable version" src="https://poser.pugx.org/kimai/kimai/v/stable"></a>
</p>

<h1 align="center">Kimai<br>#1 Open-Source Time-Tracker</h1>

Kimai is a professional grade time-tracking application, free and open-source. 
It handles use-cases of freelancers as well as companies with dozens or hundreds of users. 
Kimai was build to track your project times and ships with many advanced features, including but not limited to:

JSON API, invoicing, data exports, multi-timer and punch-in punch-out mode, tagging, multi-user - multi-timezones - multi-language ([over 30 translations existing](https://hosted.weblate.org/projects/kimai/)!),
authentication via SAML/LDAP/Database, two-factor authentication (2FA) with TOTP, customizable role and team permissions, responsive design,
user/customer/project specific rates, advanced search & filtering, money and time budgets, advanced reporting, support for [plugins](https://www.kimai.org/store/)
and so much more.

### Links

- [Home](https://www.kimai.org) — Kimai project homepage
- [Blog](https://www.kimai.org/blog/) — Read the latest news
- [Documentation](https://www.kimai.org/documentation/) — Learn how to use Kimai
- [Newsletter](https://www.kimai.org/en/newsletter) - Subscribe and get notified about new releases and important updates


### Requirements

- PHP 8.2 minimum with support for 8.3, 8.4, 8.5
- MariaDB / MySQL: oldest maintained LTS release (MariaDB >= [10.6](https://endoflife.date/mariadb) or MySQL >= [8.4](https://endoflife.date/mysql)) or newer
- A webserver and subdomain (subdirectory is not supported)
- PHP extensions: `gd`, `intl`, `json`, `mbstring`, `pdo`, `tokenizer`, `xml`, `xsl`, `zip`

## Installation

- Caddy with Docker-Compose at [Hetzner](https://www.kimai.org/documentation/hosting-hetzner-cloud.html) and [DigitalOcean](https://www.kimai.org/documentation/hosting-digital-ocean.html)
- [SSH setup](https://www.kimai.org/documentation/installation.html) with Git and Composer
- [Docker images](https://hub.docker.com/r/kimai/kimai2) with FPM only or incl. Apache
- [Synology](https://www.kimai.org/documentation/synology.html) user can host the Docker version 
- [Developer setups](https://www.kimai.org/documentation/developers.html) if you want to create Kimai integrations

There are more documented ways for [on-premise hosting](https://www.kimai.org/documentation/chapter-on-premise.html). 

And if you don't want to host Kimai, you can use the [Cloud version](https://www.kimai.cloud/) of it.

### Updating Kimai

- [Update Kimai](https://www.kimai.org/documentation/updates.html) — get the latest version
- [UPGRADING guide](UPGRADING.md) — version specific steps

### Plugins

- [Plugins](https://www.kimai.org/store/) — paid and free plugin marketplace
- [Developer documentation](https://www.kimai.org/documentation/developers.html) — how to create a plugin

## Roadmap and releases

You can see a rough development [roadmap](https://github.com/orgs/kimai/projects/2), which is open for changes and input from the community, your [ideas](https://github.com/kimai/kimai/issues) are welcome.

Release versions will be created on a regular basis, every couple of weeks latest.
Every code change, whether it's a new feature or a bugfix, will be done on the `main` branch.

## Contributing

You want to contribute to this repository? This is so great!
The best way to start is to [open a new issue](https://github.com/kimai/kimai/issues) for bugs or feature requests or a [discussion](https://github.com/kimai/kimai/discussions) for questions, support and such.

In case you want to contribute, but you wouldn't know how, here are some suggestions:

- Spread the word: Please [write a testimonial for our Wall of love](https://love.kimai.org), vote for Kimai on any software platform, you can toot or tweet about it, share it on LinkedIn, Reddit and any other social media platform!
- [Translate Kimai into your language](https://hosted.weblate.org/engage/kimai/), or help to improve the existing translations, many languages look for a contributor
- Answer questions: You know the answer to another user's problem? Share your knowledge.
- Something can be done better? An essential feature is missing? Create a feature request.
- Report bugs makes Kimai better for everyone.
- You don't have to be programmer, the documentation and translation could always use some attention.
- Sponsor the project: free software costs money to create!

There is one simple rule in our "Code of conduct": Don't be an ass!

## Follow Kimai

- Mastodon: [@kimai](https://phpc.social/@kimai)
- Youtube: [@kimai_org](https://www.youtube.com/@kimai_org)
- LinkedIn: [@kimai-org](https://www.linkedin.com/company/kimai-org/)
- Reddit: [r/kimai](https://www.reddit.com/r/kimai/)

### Credits

Kimai is based on modern technologies and frameworks such as [PHP](https://www.php.net/),
[Symfony](https://github.com/symfony/symfony) and [Doctrine](https://github.com/doctrine/),
[Bootstrap](https://github.com/twbs/bootstrap) and [Tabler](https://tabler.io/),
and [countless](composer.json) [others](package.json). .codecov.yml
.docker/dbtest.php
.docker/monolog.yaml
.php-cs-fixer.dist.php
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
README.md
SECURITY.md
UPGRADING-1.md
UPGRADING-3.md
UPGRADING.md
composer.json
config/bundles.php
config/locales.php
config/packages/assets.yaml
config/packages/cache.yaml
config/packages/doctrine.yaml
config/packages/doctrine_migrations.yaml
conf
...[truncated]...

# BM25 selected code snippets
### README.md
<p align="center">
    <img src="https://raw.githubusercontent.com/kimai/images/main/repository-header.png" alt="Kimai logo">
</p>

<p align="center">
    <a href="https://github.com/kimai/kimai/actions"><img alt="CI Status" src="https://github.com/kimai/kimai/actions/workflows/testing.yaml/badge.svg"></a>
    <a href="https://codecov.io/gh/kimai/kimai"><img alt="Code Coverage" src="https://codecov.io/gh/kimai/kimai/branch/main/graph/badge.svg"></a>
    <a href="https://packagist.org/packages/kimai/kimai"><img alt="Latest stable version" src="https://poser.pugx.org/kimai/kimai/v/stable"></a>
</p>

<h1 align="center">Kimai<br>#1 Open-Source Time-Tracker</h1>

Kimai is a professional grade time-tracking application, free and open-source. 
It handles use-cases of freelancers as well as companies with dozens or hundreds of users. 
Kimai was build to track your project times and ships with many advanced features, including but not limited to:

JSON API, invoicing, data exports, multi-timer and punch-in punch-out mode, tagging, multi-user - multi-timezones - multi-language ([over 30 translations existing](https://hosted.weblate.org/projects/kimai/)!),
authentication via SAML/LDAP/Database, two-factor authentication (2FA) with TOTP, customizable role and team permissions, responsive design,
user/customer/project specific rates, advanced search & filtering, money and time budgets, advanced reporting, support for [plugins](https://www.kimai.org/store/)
and so much more.

### Links

- [Home](https://www.kimai.org) — Kimai project homepage
- [Blog](https://www.kimai.org/blog/) — Read the latest news
- [Documentation](https://www.kimai.org/documentation/) — Learn how to use Kimai
- [Newsletter](https://www.kimai.org/en/newsletter) - Subscribe and get notified about new releases and important updates


### Requirements

- PHP 8.2 minimum with support for 8.3, 8.4, 8.5
- MariaDB / MySQL: oldest maintained LTS release (MariaDB >= [10.6](https://endoflife.date/mariadb) or MySQL >= [8.4](https://endoflife.date/mysql)) or newer
- A webserver and subdomain (subdirectory is not supported)
- PHP extensions: `gd`, `intl`, `json`, `mbstring`, `pdo`, `tokenizer`, `xml`, `xsl`, `zip`

## Installation

- Caddy with Docker-Compose at [Hetzner](https://www.kimai.org/documentation/hosting-hetzner-cloud.html) and [DigitalOcean](https://www.kimai.org/documentation/hosting-digital-ocean.html)
- [SSH setup](https://www.kimai.org/documentation/installation.html) with Git and Composer
- [Docker images](https://hub.docker.com/r/kimai/kimai2) with FPM only or incl. Apache
- [Synology](https
...[truncated]...

### UPGRADING-1.md
# Upgrading Kimai - Version 1.x

_Make sure to create a backup before you start!_ 

Read the [updates documentation](https://www.kimai.org/documentation/updates.html) to find out how 
you can upgrade your Kimai installation to the latest stable release.

Check below if there are more version specific steps required, which need to be executed after the normal update process.
Perform EACH version specific task between your version and the new one, otherwise you risk data inconsistency or a broken installation.

## [1.16](https://github.com/kimai/kimai/releases/tag/1.16)

If you are using MariaDB, it must be at least version 10.1, older versions are not supported any longer.

**DEVELOPER**

- Removed `formDateTime` field from API model `I18nConfig`
- Upgraded to Doctrine DBAL 3, see [docs](https://github.com/doctrine/dbal/blob/3.1.x/UPGRADE.md) - you might have to update your bundle

## [1.15](https://github.com/kimai/kimai/releases/tag/1.15)

**Many database changes: don't forget to [run the updater](https://www.kimai.org/documentation/updates.html).**

Updating the database might take quite a while, depending on the amount of timesheet entries and speed of your database server (~1 minute per 100k records).

**ATTENTION**

- This release bumps the minimum required [PHP version to 7.3](https://www.kimai.org/blog/2021/php8-support-php72-dropped/)
- Self-registration is disabled by default
- Self-registration now always requires email confirmation
- All plugins that use own databases need to be updated as well
- Removed the YearChart widget and the related configs named `userRecapThisYear`, `userRecapLastYear`, `userRecapTwoYears`, `userRecapThreeYears`

**LDAP & SAML**

Please verify your config with the [LDAP](https://www.kimai.org/documentation/ldap.html) and [SAML](https://www.kimai.org/documentation/saml.html) documentation, especially:

- SAML users: activate it by setting the `kimai.saml.activate: true` config key
- LDAP users: activate it by setting the `kimai.ldap.activate: true` config key
- LDAP and SAML users need to remove the complete `security` section from their `local.yaml`

**DEVELOPER**  

PHP 8 compatibility forced to upgrade MANY libraries, including but not limited to:

- Removed FOSUserBundle and hslavich/oneloginsaml
- Doctrine Migrations, whose new major version forces plugin updates 
- Gedmo v3 (which include BC breaks in definitions)
- Doctrine DBAL and others, which required PHP 7.3 as well

**API BC break**: Due to team structure changes, it was impossible to keep the (writing) API structure. Please adjust your code accordingly!


...[truncated]...

### UPGRADING.md
# Upgrading Kimai - Version 2.x

_Make sure to create a backup before you start!_ 

Read the [updates documentation](https://www.kimai.org/documentation/updates.html) to find out how 
you can upgrade your Kimai installation to the latest stable release.

Check below if there are more version specific steps required, which need to be executed after the normal update process.
Perform EACH version specific task between your version and the new one, otherwise you risk data inconsistency or a broken installation.

## [2.58.0](https://github.com/kimai/kimai/releases/tag/2.58.0)

The official Docker image no longer runs with the default `APP_SECRET=change_this_to_something_unique`.
If you did not explicitly set your own `APP_SECRET` (via `-e APP_SECRET=...` or your compose/environment
config), the container now generates a unique secret on first start and persists it as `var/data/.appsecret`
inside the `data` volume that the documented Docker setup already mounts.

As a one-time effect of this upgrade, all existing sessions, "remember me" cookies and pending
password-reset links become invalid — every user has to log in again once. No manual action is required;
the container starts as before. It is recommended to configure your own `APP_SECRET` explicitly.

## [2.56.0](https://github.com/kimai/kimai/releases/tag/2.56.0)

The required minimum PHP version is now 8.2, read https://www.php.net/supported-versions.php

If you are still using PHP 8.1, please be aware it is EOL and does not receive any security updates.

If you have to upgrade to a newer version, do yourself the favor and upgrade directly to PHP 8.5.
The requirement for 8.2 is an intermediate solution for the near future, and the requirement will be raised to 8.5 rather sooner than later. 

## [2.0.30](https://github.com/kimai/kimai/releases/tag/2.0.30)

The `DATABASE_URL` in your environment settings (e.g. [.env](https://github.com/kimai/kimai/issues/4246), [docker-compose.yaml](https://github.com/tobybatch/kimai2/issues/531) or webserver config)
now requires the `charset` and `serverVersion` params, e.g.: `DATABASE_URL=mysql://user:password@127.0.0.1:3306/database?charset=utf8mb4&serverVersion=10.5.8-MariaDB` (examples in `.env`).

## [2.0](https://github.com/kimai/kimai/releases/tag/2.0)

**!! This release requires minimum PHP version to 8.1 !!**

### Breaking changes

- All plugins need to be updated: delete all previous version from your installation (`rm -r var/plugins/*`) before updating!
- The `local.yaml` is not compatible with old version, remove it before the update and then re-create it aft
...[truncated]...

### CONTRIBUTING.md
# Contributing

Kimai is an open source project, contributions made by the community are welcome.
But we can only accept contributions with a signed CLA (Contributor License Agreement) to prevent issues in the future (you will see a link when opening a PR).

Send your ideas, code reviews, pull requests and feature requests to help to improve this project.

## Pull request rules

- Make your changes in a new git branch, based on the latest code in `main`
- Apply our code-style by running `composer codestyle-fix`
- Run the static code analysis with `composer phpstan`
- Verify everything still works with `composer tests` 
- Add tests for your changes

Further documentation can be found in the [developer documentation](https://www.kimai.org/documentation/developers.html).

### UPGRADING-3.md
# Upgrading Kimai - Version 3.x

_Make sure to create a backup before you start!_ 

Read the [updates documentation](https://www.kimai.org/documentation/updates.html) to find out how you can upgrade your Kimai installation to the latest stable release.

Check below if there are more version specific steps required, which need to be executed after the normal update process.
Perform EACH version specific task between your version and the new one, otherwise you risk data inconsistency or a broken installation.

## 3.0

**!! This release requires minimum PHP version 8.4 !!**

### Developer

Do not use method chaining: all fluent interface, especially in Entities, are no longer supported. 

Removed translations:
- `action.edit`: use `edit` instead
- `my.profile`: use `user_profile` instead
- `stats.userAmountToday`: use `` instead
- `stats.userAmountWeek`: use `` instead
- `stats.userAmountMonth`: use `` instead
- `stats.userAmountYear`: use `` instead
- `stats.userAmountTotal`: use `` instead
- `update_multiple`

### AGENTS.md
# Kimai Core Agent Guide

Use this file when working in the Kimai core repository.

## Stack

- Kimai is a professional open source time-tracking application
- PHP versions: 8.2, 8.3, 8.4, 8.5
- Main framework: Symfony 6.4
- Core libraries: Doctrine, Twig
- API libraries: FOSRestBundle, NelmioApiDocBundle
- Frontend: Bootstrap with Tabler.io
- Frontend build: Webpack Encore via `symfony/webpack-encore`
- Package managers: Composer and Yarn
- Tests: PHPUnit
- Code styles: PhpCsFixer
- Static analysis: PHPStan
- Project information in README.md
- Translations managed with Weblate online service

## Scope

- This guide applies to Kimai core only
- Work in `var/plugins/` is out of scope unless explicitly requested
- Each subdirectory in `var/plugins/` is a separate Kimai plugin and its own Git repository
- In fresh installations, `var/data/` and `var/plugins/` are empty

## Repository Map

- `.docker/` Docker image build files
- `.github/` GitHub Actions and repository metadata
- `assets/` JavaScript and Sass sources
- `bin/` executable entry points, especially `bin/console`
- `config/` Symfony configuration and bundle setup
- `migrations/` Doctrine migrations for installs and upgrades
- `public/` web root with `index.php`
- `public/build/` generated frontend assets
- `public/bundles/` generated public bundle assets
- `src/` core PHP source code
- `src/API/` the JSON API
- `templates/` Twig templates
- `tests/` PHPUnit tests
- `translations/` XLIFF files named `<component>.<locale>.xlf`
- `var/` runtime storage and generated content
- `vendor/` Composer dependencies

## Never Touch

- Do not read from or write to `var/cache/`, it is Symfony-managed internal state
- Do not modify `vendor/`
- Do not modify `var/data/`
- Do not modify `var/log/`
- Do not modify `public/build/`, generated frontend assets
- Do not modify `public/bundles/`, frintend assets from plugins
- Do not modify plugins in `var/plugins/` unless explicitly asked

## Agent Workflow

- Read the surrounding code before editing
- Follow existing local patterns before introducing new abstractions
- Keep changes small and targeted
- Keep code, identifiers, comments, branches, commit text, and documentation in English
- Ask before touching security-sensitive areas such as authentication, authorization, or permissions

## Architecture Rules

- Do not introduce new composer packages without prior discussion
- Prefer services over static helper classes
- Keep business logic out of controllers
- Use Twig templates for HTML output
- Preserve backward compatibility for upgrades

## Database Rules

- Doctr
...[truncated]...

### composer.json
{
    "name": "kimai/kimai",
    "license": "AGPL-3.0-or-later",
    "type": "project",
    "description": "Kimai - Time Tracking",
    "authors": [
        {
            "name": "Kevin Papst",
            "homepage": "https://www.kevinpapst.de"
        },
        {
            "name": "All contributors",
            "homepage": "https://github.com/kimai/kimai/contributors"
        }
    ],
    "require": {
        "php": ">=8.2",
        "ext-gd": "*",
        "ext-intl": "*",
        "ext-json": "*",
        "ext-mbstring": "*",
        "ext-pdo": "*",
        "ext-tokenizer": "*",
        "ext-xml": "*",
        "ext-xsl": "*",
        "ext-zip": "*",
        "composer-runtime-api": "^2.0",
        "azuyalabs/yasumi": "^2.6",
        "composer/semver": "^3.3",
        "doctrine/doctrine-bundle": "^2.7",
        "doctrine/doctrine-migrations-bundle": "^3.3",
        "doctrine/orm": "^2.8",
        "easybill/zugferd-php": "^2.1",
        "endroid/qr-code": "^4.8",
        "erusev/parsedown": "^1.6",
        "friendsofsymfony/rest-bundle": "^3.0",
        "gedmo/doctrine-extensions": "^3.6",
        "horstoeko/zugferd": "^1.0",
        "horstoeko/zugferdublbridge": "^1.0",
        "jms/serializer-bundle": "^5.0",
        "kevinpapst/tabler-bundle": "^2.0",
        "league/csv": "^9.4",
        "mpdf/mpdf": "^8.0",
        "nelmio/api-doc-bundle": "^5.0",
        "nelmio/cors-bundle": "^2.0",
        "onelogin/php-saml": "^4.0",
        "openspout/openspout": "^4.0",
        "pagerfanta/pagerfanta": "^4.0",
        "phpoffice/phpspreadsheet": "^2.0",
        "phpoffice/phpword": "^1.0",
        "psr/container": "^2.0",
        "psr/log": "^3.0",
        "scheb/2fa-backup-code": "^6.2",
        "scheb/2fa-bundle": "^6.2",
        "scheb/2fa-totp": "^6.2",
        "symfony/asset": "^6.0",
        "symfony/console": "^6.0",
        "symfony/dotenv": "^6.0",
        "symfony/expression-language": "^6.0",
        "symfony/flex": "^2",
        "symfony/form": "^6.0",
        "symfony/framework-bundle": "^6.0",
        "symfony/http-client": "^6.0",
        "symfony/intl": "^6.0",
        "symfony/mailer": "^6.0",
        "symfony/mime": "^6.0",
        "symfony/monolog-bundle": "^3.4",
        "symfony/process": "^6.0",
        "symfony/rate-limiter": "^6.0",
        "symfony/runtime": "^6.0",
        "symfony/security-bundle": "^6.0",
        "symfony/security-csrf": "^6.0",
        "symfony/serializer": "^6.0",
        "symfony/translation": "^6.0",
        "symfony/twig-bundle": "^6.0",
        "symfony/validator": "^6.0",
        "symfony/webpack-encore-bun
...[truncated]...

### config/packages/scheb_2fa.yaml
# Documentation at https://symfony.com/bundles/SchebTwoFactorBundle/6.x/configuration.html
scheb_two_factor:
    security_tokens:
        - Symfony\Component\Security\Core\Authentication\Token\UsernamePasswordToken
        - Symfony\Component\Security\Http\Authenticator\Token\PostAuthenticationToken
        - App\Saml\SamlToken

    totp:
        enabled: true
        template: security/2fa.html.twig    # Overwritten template
        leeway: 29                          # How many seconds the code is valid
        issuer: Kimai                       # Issuer name used in QR code

    two_factor_condition: App\Security\TwoFactorCondition

    # TODO add:  backup codes - https://symfony.com/bundles/SchebTwoFactorBundle/current/backup_codes.html
    # TODO add: Trusted device feature - https://github.com/scheb/2fa/blob/6.x/doc/configuration.rst

### config/packages/tabler.yaml
#
# Configuration file for the Tabler bundle
#
# For more information about the bundle settings visit:
# https://github.com/kevinpapst/TablerBundle/blob/master/Resources/docs/configurations.md
#
tabler:
    options:
        theme_auto: true
        dark_mode: false
        navbar_condensed: true
        navbar_overlap: false
        navbar_dark: true
        boxed_layout: false
        rtl_mode: false
        user_menu_condensed: false
        logo_url: "touch-icon-192x192.png"
        theme_base: "neutral"
        theme_radius: 0.5
        theme_primary: "blue"

    knp_menu:
        enable: false
        main_menu: tabler_main
        breadcrumb_menu: false

    routes:
        tabler_welcome: dashboard
        tabler_login: login
        tabler_login_check: security_check
        tabler_registration: registration_register
        tabler_registration_register: registration_register
        tabler_password_reset: resetting_request
        tabler_password_reset_sent: resetting_send_email

    icons:
        about: fas fa-info-circle
        activity: fas fa-tasks
        admin: fas fa-wrench
        administration: fas fa-toolbox
        applications: fas fa-rocket
        audit: fas fa-history
        avatar: fas fa-user
        back: fas fa-long-arrow-alt-left
        barcode: fas fa-barcode
        bookmark: far fa-star
        bookmarked: fas fa-star
        break: fas fa-utensils
        calendar: far fa-calendar-alt
        cancel: fas fa-times
        clock: far fa-clock
        collapse: fas fa-chevron-down
        columns: fas fa-table
        comment: far fa-comment
        configuration: fas fa-cog
        contract: fas fa-balance-scale
        copy: far fa-copy
        create: fas fa-plus
        csv: fas fa-table
        customer: fas fa-user-tie
        dashboard: fas fa-tachometer-alt
        debug: far fa-file-alt
        delete: far fa-trash-alt
        details: fas fa-info-circle
        display: fas fa-layer-group
        doctor: fas fa-medkit
        documentation: fas fa-book
        dot: fas fa-circle
        download: fas fa-download
        duration: fas fa-stopwatch
        edit: far fa-edit
        end: fas fa-hourglass-end
        export: fas fa-download
        failure: fas fa-times
        fax: fas fa-fax
        filter: fas fa-filter
        help: far fa-question-circle
        holiday: fas fa-umbrella-beach
        home: fas fa-home
        info: fas fa-info-circle
        import: fas fa-file-import
        invoice: fas fa-file-contract
        invoice-template: fas fa-file-signature
        left: fas fa-chevron-left
      
...[truncated]...

### SECURITY.md
# Security Policy

As announced in the [README](README.md) security fixes will only be added to the `main` branch. 

| Version              | Supported          |
|----------------------|--------------------|
| main branch          | :white_check_mark: |
| older releases       | :x:                |

You find all information in our [Bughunter documentation](https://www.kimai.org/documentation/bughunter.html).

### config/packages/kimai.yaml
# ---------------------------------------------------------------------------------------------
# DO NOT EDIT THIS FILE, INSTEAD CREATE THE FILE "local.yaml" AND ADD YOUR SETTINGS IN THERE.
# See https://www.kimai.org/documentation/local-yaml.html
#
# Be aware that this file is YAML format and the indentation is important.
# Each config level needs to be indented with 4 additional spaces.
# ---------------------------------------------------------------------------------------------
kimai:

# --------------------------------------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------------------------------------
#    user:
#        registration: false
#        password_reset: true
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# TIME-TRACKING
# --------------------------------------------------------------------------------
    timesheet:

        # Allows to render timesheet descriptions with markdown
        # This setting can be changed through the Administration screen
        # markdown_content: false

        # Configures the duration drop-down select.
        # null = use rounding rules, 0 = deactivate, every other number is used as minute/step increment
        # duration_increment: ~

        # Configures the minute select for begin and end date-time.
        # null = use rounding rules, every number > 0 is used as minute/step increment
        # time_increment: ~

        # The time-tracking mode that should be used.
        # mode: default

        # The default time to pre-fill the "create timesheet" form (in some cases).
        # This setting is only respected by some time-tracking modes and not in all situations.
        #
        # Accepted formats, see
        # - https://www.php.net/manual/en/datetime.formats.php
        # - https://www.php.net/manual/en/datetime.formats.time.php
        # default_begin: now

        # Rounding rules are used to round the begin & end dates and the duration for timesheet records.
        # The "default" rule will round "begin" down and "end" up to the full minute, the "duration" will not be rounded.
        # rounding:
        #    default:
        #        days: ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        #        begin: 1
        #        end: 1
        #        duration: 0
        #        mode: default

        # If you want to apply different hourly rates for specific weekdays, you can 
...[truncated]...

### package.json
{
  "name": "kimai",
  "homepage": "https://github.com/kimai/kimai",
  "license": "AGPL",
  "maintainers": [
    {
      "name": "Kevin Papst",
      "url": "https://www.kevinpapst.de"
    }
  ],
  "repository": {
    "type": "git",
    "url": "git+https://github.com/kimai/kimai.git"
  },
  "scripts": {
    "dev-server": "encore dev-server",
    "dev": "encore dev",
    "watch": "encore dev --watch",
    "lint": "eslint assets/js/",
    "build": "encore production"
  },
  "browserslist": [
    "defaults"
  ],
  "dependencies": {
    "@babel/core": "^7.29.0",
    "@babel/eslint-parser": "^7.28.6",
    "@babel/plugin-syntax-dynamic-import": "^7.8.3",
    "@babel/preset-env": "^7.29.5",
    "@eslint/js": "^9.39.4",
    "@fortawesome/fontawesome-free": "^6.7.2",
    "@fullcalendar/bootstrap5": "^5.11.5",
    "@fullcalendar/core": "^5.11.5",
    "@fullcalendar/daygrid": "^5.11.5",
    "@fullcalendar/google-calendar": "^5.11.5",
    "@fullcalendar/icalendar": "^5.11.5",
    "@fullcalendar/interaction": "^5.11.5",
    "@fullcalendar/timegrid": "^5.11.5",
    "@popperjs/core": "^2.11.8",
    "@symfony/webpack-encore": "^6.0.0",
    "@tabler/core": "^1.4.0",
    "bootstrap": "^5.3.8",
    "chart.js": "^4.5.1",
    "core-js": "^3.49.0",
    "dompurify": "^3.4.5",
    "eslint": "^9.39.4",
    "globals": "^15.15.0",
    "gridstack": "^7.3.0",
    "highlight.js": "^11.11.1",
    "litepicker": "^2.0.12",
    "luxon": "^3.7.2",
    "sass": "^1.100.0",
    "sass-loader": "^16.0.8",
    "tom-select": "2.5.2",
    "webpack": "^5.107.1",
    "webpack-cli": "^6.0.1"
  },
  "pnpm": {
    "onlyBuiltDependencies": [
      "@parcel/watcher"
    ],
    "ignoredBuiltDependencies": [
      "core-js"
    ]
  },
  "packageManager": "pnpm@10.15.1+sha512.34e538c329b5553014ca8e8f4535997f96180a1d0f614339357449935350d924e22f8614682191264ec33d1462ac21561aff97f6bb18065351c162c7e8f6de67"
}

### config/packages/doctrine.yaml
parameters:
    # Adds a fallback DATABASE_URL if the env var is not set.
    # This allows you to run cache:warmup even if your
    # environment variables are not available yet.
    # You should not need to change this value.
    env(DATABASE_URL): ''

doctrine:
    dbal:
        default_connection: default
        connections:
            default:
                # existing migrations will fail if the schema filter is activated
                #schema_filter: ~^(?!(bundle_migration_|kimai2_sessions))~
                url: '%env(DATABASE_URL)%'
                driver: 'pdo_mysql'
                charset: utf8mb4
                default_table_options:
                    charset: utf8mb4
                    collation: utf8mb4_unicode_ci
                schema_manager_factory: doctrine.dbal.default_schema_manager_factory

        types:
            datetime: App\Doctrine\UTCDateTimeType
            datetime_immutable: App\Doctrine\UTCDateTimeImmutableType
    orm:
        controller_resolver:
            # FIXME this is causing a deprecation and needs to be changed
            # auto_mapping: false
            auto_mapping: true
        auto_generate_proxy_classes: '%kernel.debug%'
        default_entity_manager: default
        enable_lazy_ghost_objects: true
        entity_managers:
            default:
                report_fields_where_declared: true
                connection: default
                naming_strategy: doctrine.orm.naming_strategy.underscore_number_aware
                auto_mapping: true
                mappings:
                    App:
                        type: attribute
                        dir: '%kernel.project_dir%/src/Entity'
                        prefix: 'App\Entity'
                        alias: Kimai
                dql:
                    datetime_functions:
                        date: App\Doctrine\Extensions\Date
                        day: App\Doctrine\Extensions\Day
                        month: App\Doctrine\Extensions\Month
                        year: App\Doctrine\Extensions\Year

when@test:
    doctrine:
        dbal:
            connections:
                default:
                    logging: false
                    use_savepoints: true

when@prod:
    doctrine:
        orm:
            metadata_cache_driver:
                type: pool
                pool: doctrine.system_cache_pool
            query_cache_driver:
                type: pool
                pool: doctrine.system_cache_pool
            result_cache_driver:
                type: pool
                pool: doctrine.result_cache_pool

### src/Utils/ReleaseVersion.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Utils;

use App\Constants;
use Composer\Semver\Semver;
use Composer\Semver\VersionParser;

/**
 * Code inspired by https://github.com/consolidation/self-update (MIT license - 03 Sept. 2022)
 */
final class ReleaseVersion
{
    /**
     * Get all releases from GitHub.
     *
     * @return array<string, array{'version': non-empty-string, 'date': \DateTimeInterface, 'url': non-empty-string, 'download': non-empty-string, 'content': string}>
     */
    private function getReleasesFromGithub(): array
    {
        $versionParser = new VersionParser();
        $opts = [
            'http' => [
                'method' => 'GET',
                'header' => [
                    'User-Agent: ' . Constants::SOFTWARE . ' ' . Constants::VERSION . ' Update-Check (PHP)',
                ],
            ],
        ];

        $context = stream_context_create($opts);

        $releases = file_get_contents('https://api.github.com/repos/' . Constants::GITHUB_REPO . '/releases', false, $context);
        if ($releases === false) {
            throw new \Exception('Could not load releases from GitHub repository: ' . Constants::GITHUB_REPO);
        }
        /** @var array<string, array{url: non-empty-string, html_url: non-empty-string, tag_name: non-empty-string, name: non-empty-string, draft: bool, immutable: bool, prerelease: bool, created_at: non-empty-string, updated_at: non-empty-string, published_at: non-empty-string, zipball_url: non-empty-string, body: string}> $releases */
        $releases = json_decode($releases, true);

        if ($releases === false) {
            throw new \Exception('Failed parsing release found at GitHub repository: ' . Constants::GITHUB_REPO);
        }

        $parsed = [];
        foreach ($releases as $release) {
            if ($release['draft'] || $release['prerelease']) {
                continue;
            }

            try {
                $normalized = $versionParser->normalize($release['tag_name']);
            } catch (\UnexpectedValueException $e) {
                continue;
            }

            if (VersionParser::parseStability($normalized) !== 'stable') {
                continue;
            }

            $date = $release['published_at'];
            try {
                $date = new \DateTimeImmutable($date);
            } catch (\Exception $ex) {
                continue;
            }

            $p
...[truncated]...

### src/Controller/PluginController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\Controller;

use App\Plugin\PluginManager;
use App\Utils\PageSetup;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;
use Symfony\Contracts\Cache\CacheInterface;
use Symfony\Contracts\Cache\ItemInterface;
use Symfony\Contracts\HttpClient\HttpClientInterface;

#[Route(path: '/admin/plugins')]
#[IsGranted('plugins')]
final class PluginController extends AbstractController
{
    #[Route(path: '/', name: 'plugins', methods: ['GET'])]
    public function indexAction(PluginManager $manager, HttpClientInterface $client, CacheInterface $cache): Response
    {
        $installed = [];
        $plugins = $manager->getPlugins();
        foreach ($plugins as $plugin) {
            $installed[$plugin->getId()] = $plugin;
        }

        $page = new PageSetup('menu.plugin');
        $page->setHelp('plugins.html');

        $all = $this->getPluginInformation($client, $cache);
        $bundles = [];
        $updates = [];
        foreach ($all as $item) {
            if ($item['bundle'] !== null) {
                $bundles[$item['bundle']] = $item;
                if (\array_key_exists($item['bundle'], $installed)) {
                    $updates[$item['bundle']] = version_compare($installed[$item['bundle']]->getMetadata()->getVersion(), $item['latest_release']) === -1;
                }
            }
        }

        return $this->render('plugin/index.html.twig', [
            'page_setup' => $page,
            'plugins' => $plugins,
            'installed' => array_keys($installed),
            'extensions' => $all,
            'bundles' => $bundles,
            'updates' => $updates,
        ]);
    }

    private function getPluginInformation(HttpClientInterface $client, CacheInterface $cache): array
    {
        return $cache->get('kimai.marketplace_extensions', function (ItemInterface $item) use ($client) {
            try {
                $response = $client->request('GET', 'https://www.kimai.org/plugins.json');

                if ($response->getStatusCode() !== 200) {
                    return [];
                }

                $json = json_decode($response->getContent(), true);

                if ($json === null) {
                    return [];
                }

                $item->expiresAfter(86400); // one day

                return
...[truncated]...

### src/API/StatusController.php
<?php

/*
 * This file is part of the Kimai time-tracking app.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace App\API;

use App\API\Model\Plugin;
use App\API\Model\Version;
use App\Plugin\PluginManager;
use FOS\RestBundle\View\View;
use FOS\RestBundle\View\ViewHandlerInterface;
use Nelmio\ApiDocBundle\Attribute\Model;
use OpenApi\Attributes as OA;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Http\Attribute\IsGranted;

#[IsGranted('API')]
#[OA\Tag(name: 'Default')]
final class StatusController extends BaseApiController
{
    public function __construct(private readonly ViewHandlerInterface $viewHandler)
    {
    }

    /**
     * Testing route for the API
     */
    #[OA\Response(response: 200, description: "A simple route that returns a 'pong', which you can use for testing the API", content: new OA\JsonContent(example: "{'message': 'pong'}"))]
    #[Route(methods: ['GET'], path: '/ping')]
    public function pingAction(): Response
    {
        $view = new View(['message' => 'pong'], 200);

        return $this->viewHandler->handle($view);
    }

    /**
     * Fetch Kimai release
     */
    #[OA\Response(response: 200, description: 'Returns version information about the current release', content: new OA\JsonContent(ref: new Model(type: Version::class)))]
    #[Route(methods: ['GET'], path: '/version')]
    public function versionAction(): Response
    {
        return $this->viewHandler->handle(new View(new Version(), 200));
    }

    /**
     * Fetch installed Plugins
     */
    #[OA\Response(response: 200, description: 'Returns a list of plugin names and versions', content: new OA\JsonContent(type: 'array', items: new OA\Items(ref: new Model(type: Plugin::class))))]
    #[Route(methods: ['GET'], path: '/plugins')]
    public function pluginAction(PluginManager $pluginManager): Response
    {
        $plugins = [];
        foreach ($pluginManager->getPlugins() as $plugin) {
            $plugins[] = new Plugin($plugin);
        }

        return $this->viewHandler->handle(new View($plugins, 200));
    }
}

### .docker/dbtest.php
<?php
$DATABASE_HOST = urldecode($argv[1]);
$DATABASE_BASE = urldecode($argv[2]);
$DATABASE_PORT = $argv[3];
$DATABASE_USER = urldecode($argv[4]);
$DATABASE_PASS = urldecode($argv[5]);

echo "Testing DB:";

try {
    $pdo = new \PDO("mysql:host=$DATABASE_HOST;dbname=$DATABASE_BASE;port=$DATABASE_PORT", "$DATABASE_USER", "$DATABASE_PASS", [
        \PDO::ATTR_ERRMODE => \PDO::ERRMODE_EXCEPTION
    ]);
} catch(\Exception $ex) {
    switch ($ex->getCode()) {
        case 1045:
            // we can immediately stop here and show the error message
            echo 'Access denied (1045)';
            die(1);
        case 1049:
            // error "Unknown database (1049)" can be ignored, the database will be created by Kimai
            return;
        // a lot of errors share the same meaningless error code zero
        case 0:
            // this error includes the database name, so we can only search for the static part of the error message
            if (stripos($ex->getMessage(), 'SQLSTATE[HY000] [1049] Unknown database') !== false) {
                // error "Unknown database (1049)" can be ignored, the database will be created by Kimai
                return;
            }
            switch ($ex->getMessage()) {
                // eg. no response (fw) - the startup script should retry it a couple of times
                case 'SQLSTATE[HY000] [2002] Operation timed out':
                    echo 'Operation timed out (0-2002)';
                    die(4);
                // special case "localhost" with a stopped db server (should not happen in docker compose setup)
                case 'SQLSTATE[HY000] [2002] No such file or directory':
                    echo 'Connection could not be established (0-2002)';
                    die(5);
                // using IP with stopped db server - the startup script should retry it a couple of times
                case 'SQLSTATE[HY000] [2002] Connection refused':
                    echo 'Connection refused (0-2002)';
                    die(5);
            }
            echo $ex->getMessage() . " (0)";
            die(7);
        default:
            // unknown error
            echo $ex->getMessage() . " (?)";
            die(10);
    }
}