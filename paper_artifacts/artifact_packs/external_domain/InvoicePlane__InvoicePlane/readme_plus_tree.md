# README
## README.md
<img align="right" alt="InvoicePlane logo" src="/assets/core/img/favicon.png">

# _InvoicePlane_

<div align="center">

_A libre self-hosted web application designed to help you manage invoices, clients, and payments efficiently._

<br>

[![Curent version](https://img.shields.io/badge/dynamic/json.svg?label=Current%20Version&url=https%3A%2F%2Fapi.github.com%2Frepos%2FInvoicePlane%2FInvoicePlane%2Freleases%2Flatest&query=%24.name&colorB=%23429ae1)](https://www.invoiceplane.com/)
[![Downloads](https://img.shields.io/github/downloads/invoiceplane/invoiceplane/total?colorB=%23429ae1)](https://www.invoiceplane.com/)
[![Translation](https://img.shields.io/badge/Translations-%40%20Crowdin-429ae1)](https://translations.invoiceplane.com/project/fusioninvoice)

<br>

[![Wiki](https://img.shields.io/badge/Help%3A-Official%20Wiki-429ae1.svg)](https://wiki.invoiceplane.com/)
[![Community Forums](https://img.shields.io/badge/Help%3A-Community%20Forums-429ae1.svg)](https://community.invoiceplane.com/)
[![Issue Tracker](https://img.shields.io/badge/Development%3A-Issue%20Tracker-429ae1.svg)](https://github.com/invoiceplane/invoiceplane/issues/)
[![Contribution Guide](https://img.shields.io/badge/Development%3A-Contribution%20Guide-429ae1.svg)](CONTRIBUTING.md)

</div>

---

## What's New in Version 1.7.0

**InvoicePlane 1.7.0** brings PHP 8.2+ compatibility and critical security enhancements to keep your financial data safe.

### Major Improvements

- **PHP 8.2+ Compatibility:** Full support for modern PHP versions (8.1, 8.2, 8.3+)
- **Enhanced Security:** Multiple security vulnerabilities have been addressed:
  - Fixed Cross-Site Scripting (XSS) vulnerabilities across templates and user inputs
  - Resolved Local File Inclusion (LFI) vulnerabilities in PDF generation
  - Patched log poisoning vulnerability in file upload handling
- **SVG Logo Protection:** SVG uploads are now blocked to prevent embedded script execution (see details below)
- **Updated Dependencies:** All PHP packages updated for compatibility and security

### Issues Fixed in Version 1.7.0

**Security Fixes:**
- #1433 - Local File Inclusion (LFI) vulnerabilities in PDF template handling (Post-v1.7.0 tag)
- #1388, #1387 - Unsafe jQuery plugin vulnerabilities (Code scanning alerts)
- #1383 - File access vulnerabilities across all controllers
- Security fixes for XSS vulnerabilities (multiple fields sanitized - see CHANGELOG.md)
- Security fix for log poisoning in file upload handling

**Bug Fixes and Improvements:**
- #1389 - Workflow permissions in GitHub Actions
- #1381 - E-invoicing field migration and version checking
- #1380 - Dependency update (qs package bump)
- #1377 - QR code image width reduced to 100px
- #1375 - Email address verification now supports comma and semicolon separators
- #1373 - Removed deprecated library dependencies
- #1367, #1368 - Various bug fixes

### Fields Sanitized for Security

The following fields have been sanitized to prevent XSS attacks:
- Quote and invoice number fields (all templates)
- Tax rate names
- Payment method names
- Custom field labels
- Client addresses
- Sumex observations
- Quote notes and passwords
- Email template content
- File names in upload logging (prevents log poisoning)

### Upgrading from Version 1.6.x

If you're upgrading from InvoicePlane 1.6.x:

1. **Backup your data** - Create a full backup of your database and files
2. **Check PHP version** - Ensure your server runs PHP 8.1 or higher
3. **Update files** - Replace all application files with the new version
4. **Run migrations** - Visit `/index.php/setup` to apply database updates
5. **Review logo settings** - If using an SVG logo, convert it to PNG/JPG (see SVG notice below)

For detailed upgrade instructions, visit the [InvoicePlane Wiki](https://wiki.invoiceplane.com/).

> **Full Release Notes:** See [CHANGELOG.md](CHANGELOG.md) for a complete list of changes, security fixes, and improvements.

---

## Key Features

- **Invoice & Quote Management:** Create, send, and manage professional invoices and quotes effortlessly.
- **Client Management:** Maintain detailed client records, including contact information and transaction history.
- **Payment Tracking:** Monitor payments, set up reminders, and integrate with multiple payment gateways.
- **Customization:** Tailor templates, themes, and settings to match your brand preferences.
- **Reporting:** Generate insightful reports to track your financial performance.

---

## Getting Started

To get started with InvoicePlane, you have several options depending on your needs:

### Quick Start with Docker (Recommended for Development)

The easiest way to get InvoicePlane running locally is with Docker:

```bash
# Clone the repository
git clone https://github.com/InvoicePlane/InvoicePlane.git
cd InvoicePlane

# Install dependencies
composer install
yarn install
yarn build

# Configure the application
cp ipconfig.php.example ipconfig.php
# Edit ipconfig.php to set your database connection (use settings from docker-compose.yml)

# Start Docker containers (PHP 8.2, MariaDB, nginx, phpMyAdmin)
docker-compose up -d

# Access the application
# InvoicePlane: http://localhost
# phpMyAdmin: http://localhost:8081
```

### Production Installation

For production deployments:

1. **Download the Latest Version:**
   - Visit the [InvoicePlane website](https://www.invoiceplane.com/) to download the latest release.

2. **Extract and Upload:**
   - Extract the downloaded package and upload the files to your web server or hosting environment.

3. **Configuration:**
   - Duplicate `ipconfig.php.example` and rename it to `ipconfig.php`.
   - Open `ipconfig.php` in a text editor and set your base URL and database credentials.

4. **Run the Installer:**
   - Navigate to `http://your-domain.com/index.php/setup` in your browser and follow the on-screen instructions to complete the installation.

For a **detailed installation guide**, including prerequisites and troubleshooting tips, refer to [INSTALLATION.md](INSTALLATION.md).

---

## Removing `index.php` from URLs (Optional)

To remove `index.php` from your URLs:

1. **Enable mod_rewrite:**
   - Ensure the `mod_rewrite` module is enabled on your web server.

2. **Update Configuration:**
   - Set `REMOVE_INDEXPHP` to `true` in your `ipconfig.php` file.

3. **Rename `.htaccess`:**
   - Rename the `htaccess` file in the root directory to `.htaccess`.

> **Note:** If you experience issues after making these changes, revert to the default settings by undoing the steps above.

---

## Container Deployment

> [!WARNING]
> The container always uses the new calculation.

A pre-built container image is available. Configuration is provided entirely through environment variables — no `ipconfig.php` file is needed. The entrypoint generates the configuration and runs any pending database migrations automatically on startup.

### Required environment variables

| Variable | Description |
|---|---|
| `IP_URL` | Public base URL without trailing slash, e.g. `https://invoices.example.com` |
| `DB_HOSTNAME` | Database host |
| `DB_USERNAME` | Database user |
| `DB_PASSWORD` | Database password |
| `DB_DATABASE` | Database name |
| `ENCRYPTION_KEY` | Secret key for encrypted data — generate with `openssl rand -base64 32` |

### Optional environment variables

| Variable | Default | Description |
|---|---|---|
| `DB_PORT` | `3306` | Database port |
| `CI_ENV` | `production` | Set to `development` to show all PHP errors |
| `ENABLE_DEBUG` | `false` | Enable advanced debug logging |
| `CUSTOM_TEMPLATES_FOLDER` | `/var/www/html/templates/` | Absolute path to a directory of custom invoice/quote templates. Mount a volume at the chosen path and set this variable to point at it. The directory should mirror the built-in structure: `invoice_templates/pdf/`, `invoice_templates/public/`, `quote_templates/pdf/`, `quote_templates/public/`. Templates here are listed alongside the built-in ones and take precedence when they share a name. |
| `SESS_EXPIRATION` | `864000` | Session lifetime in seconds (0 = expire on browser close) |
| `SESS_MATCH_IP` | `true` | Tie sessions to the client IP address |
| `SESS_REGENERATE_DESTROY` | `false` | Destroy the old session on regeneration |
| `X_FRAME_OPTIONS` | `SAMEORIGIN` | Value for the `X-Frame-Options` response header |
| `ENABLE_X_CONTENT_TYPE_OPTIONS` | `true` | Send the `X-Content-Type-Options: nosniff` header |
| `LEGACY_CALCULATION` | `false` | Use the classic tax/discount calculation mode. Set to `false` for simple per-item tax calculation (required for valid e-invoice XML output) |
| `ENABLE_INVOICE_DELETION` | `false` | Allow invoices to be deleted |
| `DISABLE_READ_ONLY` | `false` | Disable the read-only mode for sent invoices |
| `PASSWORD_RESET_IP_MAX_ATTEMPTS` | `5` | Max password reset attempts per IP within the time window |
| `PASSWORD_RESET_IP_WINDOW_MINUTES` | `60` | Time window in minutes for IP-based reset rate limiting |
| `PASSWORD_RESET_EMAIL_MAX_ATTEMPTS` | `3` | Max password reset attempts per email within the time window |
| `PASSWORD_RESET_EMAIL_WINDOW_HOURS` | `1` | Time window in hours for email-based reset rate limiting |
| `SUMEX_SETTINGS` | `false` | Enable Swiss medical invoice (Sumex) customizations |
| `SUMEX_URL` | — | URL to post Sumex XML to in order to receive a generated PDF |
| `ENCRYPTION_CIPHER` | `AES-256` | Cipher used for encrypted data |

### Default admin user

On first startup, if no users exist in the database, the entrypoint automatically creates an admin account. The credentials can be set via environment variables; any omitted value falls back to a safe default.

| Variable | Default | Description |
|---|---|---|
| `DEFAULT_LANGUAGE` | `english` | Default language for the application (e.g. `english`, `german`, `french`). Only applied on fresh installs; changing it after the first run has no effect. |
| `DEFAULT_ADMIN_EMAIL` | `admin@localhost` | Email address for the default admin account |
| `DEFAULT_ADMIN_PASSWORD` 
...[truncated]...

# File tree
.junie
  PR-1441-security-dry-analysis.md
  guidelines.md
ADDITIONAL_SECURITY_FIXES_v1.7.2.md
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
CVE_REQUEST_SUMMARY.md
Gruntfile.js
INSTALLATION.md
LICENSE.txt
MIGRATION_GUIDE_v1.7.2.md
README.md
RELEASE_NOTES_v1.7.2_PR_TABLE.md
SECURITY.md
SECURITY_ADVISORY_ARBITRARY_FILE_DELETION.md
SECURITY_ADVISORY_RCE_FIX.md
SECURITY_AUDIT_XSS_FAMILY_NAME.md
SECURITY_AUDIT_XSS_UNIT_INVOICE.md
SECURITY_DOCS_README.md
SECURITY_SUMMARY.md
TRANSLATIONS.md
UPGRADE.md
application
  config
    autoload.php
    config.php
    constants.php
    database.php
    doctypes.php
    foreign_chars.php
    hooks.php
    index.html
    invoice_plane.php
    memcached.php
    migration.php
    mimes.php
    number_formats.php
    payment_gateways.php
    profiler.php
    routes.php
    smileys.php
    user_agents.php
  controllers
    Welcome.php
    index.html
  core
    Admin_Controller.php
    Base_Controller.php
    Form_Validation_Model.php
    Guest_Controller.php
    MY_Loader.php
    MY_Model.php
    MY_Router.php
    Response_Model.php
    User_Controller.php
    Validator.php
    XSS_Protection_Trait.php
    index.html
  errors
    error_404.php
    error_db.php
    error_general.php
    error_php.php
    index.html
  helpers
    XMLconfigs
      README.md
    client_helper.php
    country-list
      ar
        country.php
      bg
        country.php
      ca
        country.php
      cs
        country.php
      da
        country.php
      de
        country.php
      de_CH
        country.php
      el
        country.php
      en
        country.php
      es
        country.php
      fa
        country.php
      fi
        country.php
      fr
        country.php
      fr_CA
        country.php
      he
        country.php
      hr
        country.php
      id
        country.php
      it
        country.php
      ja
        country.php
      lt
        country.php
      lv
        country.php
      nl
        country.php
      no
        country.php
      pl
        country.php
      pt_BR
        country.php
      pt_PT
        country.php
      ro
        country.php
      ru
        country.php
      sk
        country.php
      sl
        country.php
      sq
        country.php
      sr_CS
        country.php
      sv_SE
        country.php
      tr
        country.php
      vi
        country.php
    country_helper.php
    custom_values_helper.php
    date_helper.php
    diacritics_helper.php
    dropzone_helper.php
    e-invoice_helper.php
    echo_helper.php
    file_security_helper.php
    html_sanitizer_helper.php
    index.html
    invoice_helper.php
    ip_security_helper.php
    json_error_helper.php
    mailer_helper.php
    mpdf_helper.php
    number_helper.php
    orphan_helper.php
    pager_helper.php
    payments_helper.php
    pdf_helper.php
    redirect_helper.php
    security_helper.php
    settings_helper.php
    template_helper.php
    trans_helper.php
    user_helper.php
    zugferd_helper.php
  hooks
    SetTimezoneClass.php
    index.html
  index.html
  language
    english
      custom_lang.php
      gateway_lang.php
      index.html
      ip_lang.php
  libraries
    ClientTitleEnum.php
    Crypt.php
    Cryptor.php
    MY_Form_validation.php
    QrCode.php
    Sumex.php
    XMLtemplates
      README.md
    gateways
      PaypalLib.php
    index.html
  modules
    clients
      Enums
        ClientTitleEnum.php
      controllers
        Ajax.php
        Clients.php
      models
        Mdl_client_notes.php
        Mdl_clients.php
      views
        form.php
        index.php
        partial_client_address.php
        partial_client_einvoicing.php
        partial_client_table.php
        partial_notes.php
        script_select2_client_id.js
        view.php
    custom_fields
      controllers
        Custom_fields.php
      models
        Mdl_client_custom.php
        Mdl_custom_fields.php
        Mdl_invoice_custom.php
        Mdl_payment_custom.php
        Mdl_quote_custom.php
        Mdl_user_custom.php
      views
        form.php
        index.php
        partial_custom_fields_table.php
    custom_values
    dashboard
    email_templates
    families
    filter
    guest
    import
    invoice_groups
    invoices
    layout
    mailer
    payment_methods
    payments
    products
    projects
    quotes
    reports
    sessions
    settings
    setup
    tasks
    tax_rates
    units
    upload
    user_clients
    users
    welcome
  third_party
  views
compose.yml
composer.json
index.php
package.json
phpcs.xml
pint.json
rector.php
resources
robots.txt
uploads
verify_file_deletion_fix.php