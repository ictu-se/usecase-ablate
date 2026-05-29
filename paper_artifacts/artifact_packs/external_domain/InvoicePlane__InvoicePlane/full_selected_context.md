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

# Selected code and test snippets
### application/modules/users/views/form.php
<?php
$itsCompany   = $this->mdl_users->form_value('user_company') || $this->mdl_users->form_value('user_vat_id');
$qr_code_info = get_setting('qr_code') ? '<span class="pull-right"><i class="fa fa-qrcode"  data-toggle="tooltip" data-placement="bottom" title="' . trans('user_qr_code_hint') . '"></i></span>' : '';
// eInvoicing enabled?
$einvoicingTip = $einvoicing ? ' data-toggle="tooltip" data-placement="bottom" title="e-' . trans('invoicing') . ' (' : ''; // tootip base
$einvoicingReq = $einvoicing ? $einvoicingTip . trans('required_field') . ')"' : '';
$einvoicingB2B = $einvoicing ? $einvoicingTip . 'B2B ' . trans('required_field') . ')"' : '';
$einvoicingOpt = $einvoicing ? $einvoicingTip . trans('optional') . ')"' : '';
?>
<script>
    $(function () {
        show_fields();

        $('#user_type').change(function () {
            show_fields();
        });

        function show_fields() {
            $('#administrator_fields').hide();
            $('#guest_fields').hide(); // Todo this id missing (IMO: It's for old? modal user-client). (Idea* Why not a new user `type` system)

            var user_type = $('#user_type').val();

            if (user_type === '1') {
                $('#administrator_fields').show();
            } else if (user_type === '2') {
                $('#guest_fields').show(); // Todo this id missing. (Idea* For a new user type, like company? Need new module?)
            }
        }

        $('#user_country').select2({
            placeholder: '<?php _trans('country'); ?>',
            allowClear: true
        });

        $('#add-user-client-modal').click(function () {
            <?php $user_id = $id ?? ''; ?>
            $('#modal-placeholder').load("<?php echo site_url('users/ajax/modal_add_user_client/' . $user_id); ?>");
        });
    });
</script>

<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('user_form'); ?></h1>
        <?php echo $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">
        <div class="row">
            <div class="col-xs-12 col-md-6 col-md-offset-3">

                <?php echo $this->layout->load_view('layout/alerts'); ?>

                <div id="userInfo">

                    <div class="panel panel-default">
                        <div class="panel-heading"><?php _trans('account_information'); ?></div>

                        <div class="panel-body">
                            <div class="form-group">
                                <label for="user_name"><?php _trans('nam
...[truncated]...

### application/modules/users/views/form_change_password.php
<script src="<?php _core_asset('js/zxcvbn.js'); ?>"></script>

<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('change_password'); ?></h1>
        <?php echo $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <div class="row">
            <div class="col-xs-12 col-md-6 col-md-offset-3">

                <?php $this->layout->load_view('layout/alerts'); ?>

                <div class="panel panel-default">
                    <div class="panel-heading">
                        <?php _trans('change_password'); ?>
                    </div>

                    <div class="panel-body">
                        <div class="form-group">
                            <label for="user_password">
                                <?php _trans('password'); ?>
                            </label>
                            <input type="password" name="user_password" id="user_password"
                                   class="form-control passwordmeter-input" required>
                            <div class="progress" style="height:3px;">
                                <div class="progress-bar progress-bar-danger passmeter passmeter-1"
                                     style="width: 33%"></div>
                                <div class="progress-bar progress-bar-warning passmeter passmeter-2"
                                     style="display: none; width: 33%"></div>
                                <div class="progress-bar progress-bar-success passmeter passmeter-3"
                                     style="display: none; width: 34%"></div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="user_passwordv">
                                <?php _trans('verify_password'); ?>
                            </label>
                            <input type="password" name="user_passwordv" id="user_passwordv"
                                   class="form-control" required>
                        </div>
                    </div>

                </div>

            </div>
        </div>

    </div>

</form>

### application/modules/tasks/views/form.php
<?php
if ($this->mdl_tasks->form_value('task_id') && $this->mdl_tasks->form_value('task_status') == 4) :
    ?>
    <script type="text/javascript">
        $(document).ready(function () {
            $('#task-form').find(':input').prop('disabled', 'disabled');
            $('#btn-submit').hide();
            $('#btn-cancel').prop('disabled', false);
        });
    </script>
<?php endif ?>

<form method="post" id="task-form">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('tasks_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

<?php
if ($this->mdl_tasks->form_value('task_id') && $this->mdl_tasks->form_value('task_status') == 4) {
    ?>
        <div class="alert alert-warning small"><?php echo trans('info_task_readonly') ?></div>
<?php
}
?>

        <div class="row">
            <div class="col-xs-12 col-sm-6">
                <div class="panel panel-default">
                    <div class="panel-heading">
<?php
if ($this->mdl_tasks->form_value('task_id')) {
    ?>
                            #<?php echo $this->mdl_tasks->form_value('task_id'); ?>&nbsp;
                            <?php echo $this->mdl_tasks->form_value('task_name', true); ?>
<?php
} else {
    ?>
                            <?php _trans('new_task'); ?>
<?php
}
?>
                    </div>
                    <div class="panel-body">

                        <div class="form-group">
                            <label for="task_name"><?php _trans('task_name'); ?></label>
                            <input type="text" name="task_name" id="task_name" class="form-control"
                                   value="<?php echo $this->mdl_tasks->form_value('task_name', true); ?>" required>
                        </div>

                        <div class="form-group">
                            <label for="task_description"><?php _trans('task_description'); ?></label>
                            <textarea name="task_description" id="task_description" class="form-control" rows="3"
                            ><?php echo $this->mdl_tasks->form_value('task_description', true); ?></textarea>
                        </div>

                        <div class="form-group">
                            <label for="task_price"><?php _trans('task_price'); ?></label>
                            <div class="input-group">
                                <input type="text" name="task_price" id="task_price" class="amount
...[truncated]...

### application/modules/units/views/form.php
<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('add_unit'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <div class="row">
            <div class="col-xs-12 col-md-6 col-md-offset-3">

                <?php $this->layout->load_view('layout/alerts'); ?>

                <input class="hidden" name="is_update" type="hidden"
                    <?php if ($this->mdl_units->form_value('is_update')) {
                        echo 'value="1"';
                    } else {
                        echo 'value="0"';
                    } ?>
                >

                <div class="form-group">
                    <label for="unit_name">
                        <?php _trans('unit_name'); ?>
                    </label>
                    <input type="text" name="unit_name" id="unit_name" class="form-control"
                           value="<?php echo $this->mdl_units->form_value('unit_name', true); ?>" required>
                </div>

                <div class="form-group">
                    <label for="unit_name_plrl">
                        <?php _trans('unit_name_plrl'); ?>
                    </label>
                    <input type="text" name="unit_name_plrl" id="unit_name_plrl" class="form-control"
                           value="<?php echo $this->mdl_units->form_value('unit_name_plrl', true); ?>" required>
                </div>

            </div>
        </div>

    </div>

</form>

### application/modules/clients/views/form.php
<?php
$client_active = $this->mdl_clients->form_value('client_active');
$active        = ($client_active == 1 || ! is_numeric($client_active)) ? ' checked="checked"' : '';
$itsCompany    = $this->mdl_clients->form_value('client_company') || $this->mdl_clients->form_value('client_vat_id');
if ($req_einvoicing) {
    // eInvoicing panel
    $nb_users    = count($req_einvoicing->users);
    $me          = $req_einvoicing->users[$_SESSION['user_id']]->show_table;
    $nb          = $req_einvoicing->show_table; // Of users in error
    $ln          = 'user' . (($nb ?: $nb_users) > 1 ? 's' : ''); // tweak 1 on more nb_users no ok
    $user_toggle = ($req_einvoicing->show_table ? ($me ? 'danger' : 'warning') : 'default') . ' ' . ($me ? '" aria-expanded="true' : '" collapsed" aria-expanded="false');
}
// eInvoicing enabled?
$einvoicingTip = $req_einvoicing ? ' data-toggle="tooltip" data-placement="bottom" title="e-' . trans('invoicing') . ' (' : ''; // tootip base
$einvoicingReq = $req_einvoicing ? $einvoicingTip . trans('required_field') . ')"' : '';
$einvoicingB2B = $req_einvoicing ? $einvoicingTip . 'B2B ' . trans('required_field') . ')"' : '';
$einvoicingOpt = $req_einvoicing ? $einvoicingTip . trans('optional') . ')"' : '';
?>
<script type="text/javascript">
    // eInvoicing button panel helper user(s) icon toggle
    const switch_fa_toggle = function (id) {
        const f = $('#'+id);f.toggleClass('fa-user').toggleClass('fa-users');
    }

    $(function () {
        $("#client_country").select2({
            placeholder: "<?php _trans('country'); ?>",
            allowClear: true
        });

<?php $this->layout->load_view('clients/js/script_select_client_title.js'); ?>

    });

</script>

<form method="post">
    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('client_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>
    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <input class="hidden" name="is_update" type="hidden" value="<?php echo $this->mdl_clients->form_value('is_update') ? '1' : '0'; ?>">

        <div class="row">
            <div class="col-xs-12 col-sm-6"><!-- personal -->
                <div class="panel panel-default">
                    <div class="panel-heading form-inline clearfix">
                        <?php _trans('personal_information'); ?>
                        <div class="pull-right">
                            <label for="client_active" class="control-label">
                          
...[truncated]...

### application/modules/families/views/form.php
<?php
$is_update = $this->mdl_families->form_value('is_update');
?>
<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans($is_update ? 'family' : 'add_family'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <div class="row">
            <div class="col-xs-12 col-md-6 col-md-offset-3">

                <?php $this->layout->load_view('layout/alerts'); ?>

                <input class="hidden" name="is_update" type="hidden" value="<?php echo $is_update ? '1' : '0'; ?>">

                <div class="form-group">
                    <label for="family_name">
                        <?php _trans('family_name'); ?>
                    </label>
                    <input type="text" name="family_name" id="family_name" class="form-control"
                           value="<?php echo $this->mdl_families->form_value('family_name', true); ?>" required>
                </div>

            </div>
        </div>

    </div>

</form>

### application/modules/payments/views/form.php
<script>
    $(function () {
        var $invoice_id = $('#invoice_id');
        $invoice_id.focus();

        amounts = json_parse('<?php echo $amounts; ?>', <?php echo (int) IP_DEBUG; ?>);
        invoice_payment_methods = json_parse('<?php echo $invoice_payment_methods; ?>', <?php echo (int) IP_DEBUG; ?>);
        $invoice_id.change(function () {
            var invoice_identifier = "invoice" + $('#invoice_id').val();
            $('#payment_amount').val(amounts[invoice_identifier].replace("&nbsp;", " "));
            $('#payment_method_id').val(invoice_payment_methods[invoice_identifier]).trigger('change');

            if (invoice_payment_methods[invoice_identifier] != 0) {
                $('.payment-method-wrapper').append("<input type='hidden' name='payment_method_id' id='payment-method-id-hidden' class='hidden' value='" + invoice_payment_methods[invoice_identifier] + "'>");
                $('#payment_method_id').prop('disabled', true);
            } else {
                $('#payment-method-id-hidden').remove();
                $('#payment_method_id').prop('disabled', false);
            }
        });
    });
</script>

<form method="post" class="form-horizontal">

    <?php _csrf_field(); ?>

<?php
if ($payment_id) {
    ?>
    <input type="hidden" name="payment_id" value="<?php echo $payment_id; ?>">
<?php
}
        ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('payment_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons', ['attribute_cancel' => 'onclick="window.location.href = `' . site_url('payments') . '`;"']); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <div class="form-group">
            <div class="col-xs-12 col-sm-2 text-right text-left-xs">
                <label for="invoice_id" class="control-label"><?php _trans('invoice'); ?></label>
            </div>
            <div class="col-xs-12 col-sm-6">
                <select name="invoice_id" id="invoice_id" class="form-control simple-select" required>
<?php
if ( ! $payment_id) {
    foreach ($open_invoices as $invoice) {
        ?>
                        <option value="<?php echo $invoice->invoice_id; ?>"
                                <?php check_select($this->mdl_payments->form_value('invoice_id'), $invoice->invoice_id); ?>>
                            <?php echo htmlsc($invoice->invoice_number) . ' - ' . htmlsc(format_client($invoice)) . ' - ' . format_currency($invoice->invoice_balance); ?>
                        </option>
<?php
    } // End foreach
} else {
...[truncated]...

### application/modules/products/views/form.php
<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('products_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <div class="row">
            <div class="col-xs-12 col-md-6">

                <div class="panel panel-default">
                    <div class="panel-heading">

<?php if ($this->mdl_products->form_value('product_id')) : ?>
                        #<?php echo $this->mdl_products->form_value('product_id'); ?>&nbsp;
                        <?php echo $this->mdl_products->form_value('product_name', true); ?>
<?php else : ?>
                        <?php _trans('new_product'); ?>
<?php endif; ?>

                    </div>
                    <div class="panel-body">

                        <div class="form-group">
                            <label for="family_id">
                                <?php _trans('family'); ?>
                            </label>

                            <select name="family_id" id="family_id" class="form-control simple-select">
                                <option value="0"><?php _trans('select_family'); ?></option>
<?php foreach ($families as $family) { ?>
                                <option value="<?php echo $family->family_id; ?>"
                                    <?php check_select($this->mdl_products->form_value('family_id'), $family->family_id) ?>
                                ><?php echo htmlsc($family->family_name); ?></option>
<?php } ?>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="product_sku">
                                <?php _trans('product_sku'); ?>
                            </label>

                            <input type="text" name="product_sku" id="product_sku" class="form-control"
                                   value="<?php echo $this->mdl_products->form_value('product_sku', true); ?>">
                        </div>

                        <div class="form-group">
                            <label for="product_name">
                                <?php _trans('product_name'); ?>
                            </label>

                            <input type="text" name="product_name" id="product_name" class="form-control" required
                                   value="<?php echo $this->mdl_products->form_value('product_name', true); ?>" require
...[truncated]...

### application/modules/projects/views/form.php
<script>
    $(function () {
        <?php $this->layout->load_view('clients/script_select2_client_id.js'); ?>
    });
</script>

<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('projects_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <div class="form-group">
            <label for="project_name"><?php _trans('project_name'); ?></label>
            <input type="text" name="project_name" id="project_name" class="form-control"
                   value="<?php echo $this->mdl_projects->form_value('project_name', true); ?>" required>
        </div>

        <div class="form-group has-feedback">
            <label for="client_id"><?php _trans('client'); ?></label>
            <div class="input-group">
                <span id="toggle_permissive_search_clients" class="input-group-addon" title="<?php _trans('enable_permissive_search_clients'); ?>" style="cursor:pointer;">
                    <i class="fa fa-toggle-<?php echo get_setting('enable_permissive_search_clients') ? 'on' : 'off' ?> fa-fw" ></i>
                </span>
                <select name="client_id" id="client_id" class="client-id-select form-control" autofocus="autofocus">
<?php
$permissive = get_setting('enable_permissive_search_users');
        if ( ! empty($project->client_id)) {
            ?>
                    <option value="<?php echo $project->client_id; ?>"><?php _htmlsc(format_client($project)); ?></option>
<?php
        }
        ?>
                </select>
            </div>
        </div>

        <input class="hidden" id="input_permissive_search_clients"
               value="<?php echo html_escape(get_setting('enable_permissive_search_clients')); ?>">
    </div>

</form>

### application/modules/tax_rates/views/form.php
<form method="post" class="form-horizontal">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('tax_rate_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <div class="form-group">
            <div class="col-xs-12 col-sm-2 text-right text-left-xs">
                <label class="control-label">
                    <?php _trans('tax_rate_name'); ?>
                </label>
            </div>
            <div class="col-xs-12 col-sm-6">
                <input type="text" name="tax_rate_name" id="tax_rate_name" class="form-control"
                       value="<?php echo $this->mdl_tax_rates->form_value('tax_rate_name', true); ?>" required>
            </div>
        </div>

        <div class="form-group has-feedback">
            <div class="col-xs-12 col-sm-2 text-right text-left-xs">
                <label class="control-label">
                    <?php _trans('tax_rate_percent'); ?>
                </label>
            </div>
            <div class="col-xs-12 col-sm-6">
                <input type="text" name="tax_rate_percent" id="tax_rate_percent" class="form-control"
                       value="<?php echo format_amount($this->mdl_tax_rates->form_value('tax_rate_percent')); ?>" required>
                <span class="form-control-feedback">%</span>
            </div>
        </div>

    </div>

</form>

### application/modules/custom_fields/views/form.php
<?php
$disabled           = $custom_field_usage ? ' disabled' : '';
$custom_field_table = $this->mdl_custom_fields->form_value('custom_field_table');
$custom_field_type  = $this->mdl_custom_fields->form_value('custom_field_type');
?>
<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('custom_field_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
        <div class="headerbar-item pull-right">
            <a href="<?php echo site_url('custom_values/field/' . $custom_field_id) ?>" class="btn btn-sm btn-default">
                                <i class="fa fa-list fa-margin"></i> <?php _trans('values'); ?></a>
        </div>
    </div>
<?php
if ($disabled) {
    ?>
    <input type="hidden" name="custom_field_table" value="<?php echo $custom_field_table; ?>">
    <input type="hidden" name="custom_field_type" value="<?php echo $custom_field_type; ?>">
<?php
}
?>
    <div id="content" class="row">

        <div class="col-xs-12 col-md-6 col-md-offset-3">

            <?php $this->layout->load_view('layout/alerts'); ?>

            <div class="form-group">
                <label for="custom_field_label"><?php _trans('label'); ?></label>
                <input type="text" name="custom_field_label" id="custom_field_label" class="form-control"
                       value="<?php echo $this->mdl_custom_fields->form_value('custom_field_label', true); ?>" required>
            </div>

            <div class="form-group">
                <label for="custom_field_table"><?php _trans('table'); ?></label>
                <select name="custom_field_table" id="custom_field_table" class="form-control simple-select"<?php echo $disabled ?: ' required'; ?>>
<?php
// New field? Auto select (work if come from custom_fields/table/*)
$custom_field_table = $custom_field_table ?: (isset($_SERVER['HTTP_REFERER']) ? 'ip_' . basename($_SERVER['HTTP_REFERER']) . '_custom' : '');
foreach ($custom_field_tables as $table => $label) {
    ?>
                    <option value="<?php echo $table; ?>" <?php check_select($custom_field_table, $table); ?>><?php _trans($label); ?></option>
<?php
}
?>
                </select>
            </div>

            <div class="form-group">
                <label for="custom_field_location"><?php _trans('position'); ?></label>
                <select name="custom_field_location" id="custom_field_location" class="form-control simple-select"></select>
            </div>

            <div class="form-group">
                <label for="custom_field_ty
...[truncated]...

### application/modules/invoice_groups/views/form.php
<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('invoice_group_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <div class="row">
            <div class="col-xs-12 col-md-6 col-md-offset-3">

                <?php $this->layout->load_view('layout/alerts'); ?>

                <div class="form-group">
                    <label class="control-label" for="invoice_group_name">
                        <?php _trans('name'); ?>
                    </label>
                    <input type="text" name="invoice_group_name" id="invoice_group_name" class="form-control"
                           value="<?php echo $this->mdl_invoice_groups->form_value('invoice_group_name', true); ?>" required>
                </div>

                <div class="form-group">
                    <label class="control-label" for="invoice_group_identifier_format">
                        <?php _trans('identifier_format'); ?>
                    </label>
                    <input type="text" class="form-control taggable"
                           name="invoice_group_identifier_format" id="invoice_group_identifier_format"
                           value="<?php echo $this->mdl_invoice_groups->form_value('invoice_group_identifier_format', true); ?>"
                           placeholder="INV-{{{id}}}" required>
                </div>

                <div class="form-group">
                    <label class="control-label" for="invoice_group_next_id">
                        <?php _trans('next_id'); ?>
                    </label>
                    <input type="number" name="invoice_group_next_id" id="invoice_group_next_id" class="form-control"
                           value="<?php echo $this->mdl_invoice_groups->form_value('invoice_group_next_id'); ?>" required>
                </div>

                <div class="form-group">
                    <label class="control-label" for="invoice_group_left_pad">
                        <?php _trans('left_pad'); ?>
                    </label>
                    <input type="number" name="invoice_group_left_pad" id="invoice_group_left_pad" class="form-control"
                           value="<?php echo $this->mdl_invoice_groups->form_value('invoice_group_left_pad'); ?>" required>
                </div>

                <hr>

                <div class="form-group no-margin">

                    <label for="tags_client"><?php _trans('identifier_format_template_tags'); ?></label>

     
...[truncated]...

### application/modules/email_templates/views/form.php
<form method="post">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('email_template_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <input class="hidden" name="is_update" type="hidden" value="<?php echo ($this->mdl_email_templates->form_value('is_update')) ? '1' : '0'; ?>">

        <div class="row">
            <div class="col-xs-12 col-md-8 col-md-offset-2">

                <div class="form-group">
                    <label for="email_template_title" class="control-label"><?php _trans('title'); ?></label>
                    <input type="text" name="email_template_title" id="email_template_title"
                           value="<?php echo $this->mdl_email_templates->form_value('email_template_title', true); ?>"
                           class="form-control" required>
                </div>

                <div class="form-group">
                    <label for="email_template_type" class="control-label"><?php _trans('type'); ?></label>
                    <div class="radio">
                        <label>
                            <input type="radio" name="email_template_type" id="email_template_type_invoice"
                                   value="invoice" checked>
                            <?php _trans('invoice'); ?>
                        </label>
                    </div>
                    <div class="radio">
                        <label>
                            <input type="radio" name="email_template_type" id="email_template_type_quote"
                                   value="quote">
                            <?php _trans('quote'); ?>
                        </label>
                    </div>
                </div>

                <hr>

                <div class="form-group">
                    <label for="email_template_from_name" class="control-label">
                        <?php _trans('from_name'); ?>
                    </label>
                    <input type="text" name="email_template_from_name" id="email_template_from_name"
                           class="form-control taggable"
                           value="<?php echo $this->mdl_email_templates->form_value('email_template_from_name', true); ?>">
                </div>

                <div class="form-group">
                    <label for="email_template_from_email" class="control-label">
                        <?php _trans('from_email'); ?>
           
...[truncated]...

### application/modules/payment_methods/views/form.php
<form method="post" class="form-horizontal">

    <?php _csrf_field(); ?>

    <div id="headerbar">
        <h1 class="headerbar-title"><?php _trans('payment_method_form'); ?></h1>
        <?php $this->layout->load_view('layout/header_buttons'); ?>
    </div>

    <div id="content">

        <?php $this->layout->load_view('layout/alerts'); ?>

        <input class="hidden" name="is_update" type="hidden"
            <?php if ($this->mdl_payment_methods->form_value('is_update')) {
                echo 'value="1"';
            } else {
                echo 'value="0"';
            } ?>
        >

        <div class="form-group">
            <div class="col-xs-12 col-sm-2 text-right text-left-xs">
                <label for="payment_method_name" class="control-label">
                    <?php _trans('payment_method'); ?>:
                </label>
            </div>
            <div class="col-xs-12 col-sm-6">
                <input type="text" name="payment_method_name" id="payment_method_name" class="form-control"
                       value="<?php echo $this->mdl_payment_methods->form_value('payment_method_name', true); ?>" required>
            </div>
        </div>

    </div>

</form>

### application/modules/guest/views/payment_information.php
<!DOCTYPE html>

<!--[if lt IE 7]>
<html class="no-js ie6 oldie" lang="<?php _trans('cldr'); ?>"> <![endif]-->
<!--[if IE 7]>
<html class="no-js ie7 oldie" lang="<?php _trans('cldr'); ?>"> <![endif]-->
<!--[if IE 8]>
<html class="no-js ie8 oldie" lang="<?php _trans('cldr'); ?>"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" lang="<?php _trans('cldr'); ?>"> <!--<![endif]-->

<head>
    <title><?php echo get_setting('custom_title', 'InvoicePlane', true); ?></title>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="robots" content="NOINDEX,NOFOLLOW">
    <meta name="_csrf" content="<?php echo $this->security->get_csrf_hash() ?>">
    <meta name="csrf_token_name" content="<?php echo config_item('csrf_token_name'); ?>">
    <meta name="csrf_cookie_name" content="<?php echo config_item('csrf_cookie_name'); ?>">
    <meta name="csrf_token_value" content="<?php echo $this->security->get_csrf_hash(); ?>">
    <meta name="legacy_calculation" content="<?php echo (int) (config_item('legacy_calculation')); ?>">

    <link rel="icon" href="<?php _core_asset('img/favicon.png'); ?>" type="image/png">

    <link rel="stylesheet" href="<?php _theme_asset('css/style.css'); ?>" type="text/css">
    <link rel="stylesheet" href="<?php _core_asset('css/custom.css'); ?>" type="text/css">

<?php if (get_setting('monospace_amounts') == 1) { ?>
    <link rel="stylesheet" href="<?php _theme_asset('css/monospace.css'); ?>" type="text/css">
<?php } ?>

    <!--[if lt IE 9]>
    <script src="<?php _core_asset('js/legacy.min.js'); ?>"></script>
    <![endif]-->

    <script src="<?php _core_asset('js/dependencies.min.js'); ?>"></script>

</head>
<body>

<nav class="navbar navbar-default ">
    <div class="container">

        <div class="navbar-brand">
            <?php _trans('online_payment_for_invoice'); ?> #<?php echo htmlsc($invoice->invoice_number); ?>
        </div>

        <ul class="nav navbar-nav navbar-right">
            <li>
                <a target="_blank" href="<?php echo site_url('guest/view/generate_invoice_pdf/' . $invoice->invoice_url_key); ?>">
                    <i class="fa fa-print"></i> <?php _trans('download_pdf'); ?>
                </a>
            </li>
        </ul>

    </div>
</nav>

<div class="container">

    <div class="row">
        <div class="col-xs-12 col-md-8 col-md-offset-2">

            <br>
<?php
            $logo = invoice_logo();
if ($logo) {
    echo $logo . '<br><br>';
}
?>

            <div cl
...[truncated]...

### application/modules/guest/controllers/Payment_information.php
<?php

if ( ! defined('BASEPATH')) {
    exit('No direct script access allowed');
}

/*
 * InvoicePlane
 *
 * @author      InvoicePlane Developers & Contributors
 * @copyright   Copyright (c) 2012 - 2018 InvoicePlane.com
 * @license     https://invoiceplane.com/license.txt
 * @link        https://invoiceplane.com
 */

#[AllowDynamicProperties]
class Payment_Information extends Base_Controller
{
    public function __construct()
    {
        parent::__construct();

        $this->load->model('invoices/mdl_invoices');
    }

    public function form($invoice_url_key, $payment_provider = null)
    {
        $this->load->model('payment_methods/mdl_payment_methods');
        $disable_form = false;

        // Check if the invoice exists and is billable
        $invoice = $this->mdl_invoices->guest_visible()->where('ip_invoices.invoice_url_key', $invoice_url_key)->get()->row();

        if ( ! $invoice) {
            $this->session->set_flashdata('alert_error', lang('invoice_not_found'));
            redirect('guest'); // /invoices
        }

        // Check if the invoice is payable
        if ($invoice->invoice_balance == 0) {
            if ($this->session->user_id) {
                $this->session->set_flashdata('alert_info', lang('invoice_already_paid'));
                redirect('guest'); // /invoices
            }

            $disable_form = true;
            show_404();
        }

        // Get all payment gateways
        $this->load->model('mdl_settings');
        $this->config->load('payment_gateways');
        $gateways = $this->config->item('payment_gateways');

        $available_drivers = [];
        if ( ! $disable_form) {
            foreach ($gateways as $driver => $fields) {
                $d = mb_strtolower($driver);

                if (get_setting('gateway_' . $d . '_enabled') == 1) {
                    $invoice_payment_method = $invoice->payment_method;
                    $driver_payment_method  = get_setting('gateway_' . $d . '_payment_method');

                    if ($invoice_payment_method == 0 || $driver_payment_method == 0 || $driver_payment_method == $invoice_payment_method) {
                        $available_drivers[] = $driver;
                    }
                }
            }
        }

        // If only one provider is available, serve it without showing options
        if (count($available_drivers) == 1) {
            $payment_provider = $available_drivers[0];
        }

        // Get additional invoice information
        $payment_method = $this->mdl_payment_methods->where('payment_method_id', $invoice->payme
...[truncated]...

### application/core/User_Controller.php
<?php

if ( ! defined('BASEPATH')) {
    exit('No direct script access allowed');
}

/*
 * InvoicePlane
 *
 * @author      InvoicePlane Developers & Contributors
 * @copyright   Copyright (c) 2012 - 2018 InvoicePlane.com
 * @license     https://invoiceplane.com/license.txt
 * @link        https://invoiceplane.com
 */

#[AllowDynamicProperties]
class User_Controller extends Base_Controller
{
    /**
     * User_Controller constructor.
     *
     * @param string $required_key
     * @param int    $required_val
     */
    public function __construct($required_key, $required_val)
    {
        parent::__construct();

        if ($this->session->userdata($required_key
...[truncated]...