# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

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

# Oracle-selected code and test snippets
### application/modules/clients/controllers/Clients.php
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
class Clients extends Admin_Controller
{
    private const CLIENT_TITLE = 'client_title';

    /**
     * Clients constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->load->model('mdl_clients');
    }

    public function index(): void
    {
        // Display active clients by default
        redirect('clients/status/active');
    }

    /**
     * @param int $page
     */
    public function status(string $status = 'active', $page = 0): void
    {
        if (is_numeric(array_search($status, ['active', 'inactive'], true))) {
            $function = 'is_' . $status;
            $this->mdl_clients->{$function}();
        }

        $this->mdl_clients->with_total_balance()->paginate(site_url('clients/status/' . $status), $page);
        $clients = $this->mdl_clients->result();

        $req_einvoicing = get_setting('einvoicing');
        if ($req_einvoicing) {
            $this->load->helper('e-invoice'); // eInvoicing++

            foreach ($clients as &$client) {
                // Get a check of filled Required (client and users) fields for eInvoicing
                $req_einvoicing = get_req_fields_einvoice($client);

                $client = $this->check_client_einvoice_active($client, $req_einvoicing);
            }
            unset($client);
        }

        $this->layout->set(
            [
                'records'            => $clients,
                'filter_display'     => true,
                'filter_placeholder' => trans('filter_clients'),
                'filter_method'      => 'filter_clients',
                'einvoicing'         => get_setting('einvoicing'),
            ]
        );

        $this->layout->buffer('content', 'clients/index');
        $this->layout->render();
    }

    public function form($id = null): void
    {
        if ($this->input->post('btn_cancel')) {
            redirect('clients');
        }

        $new_client = false;

        // Set validation rule based on is_update
        if ($this->input->post('is_update') == 0 && $this->input->post('client_name') != '') {
            $check = $this->db->get_where('ip_clients', [
                'client_name'    => $this->input->post('client_name'),
                'cl
...[truncated]...

### application/modules/clients/controllers/Ajax.php
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
class Ajax extends Admin_Controller
{
    public $ajax_controller = true;

    public function name_query()
    {
        // Load the model & helper
        $this->load->model('clients/mdl_clients');

        $response = [];

        // Get the post input
        $query                   = $this->input->get('query');
        $permissiveSearchClients = $this->input->get('permissive_search_clients');

        if (empty($query)) {
            echo json_encode($response);
            exit;
        }

        // Search for chars "in the middle" of clients names
        $moreClientsQuery = $permissiveSearchClients ? '%' : '';

        // Search for clients
        $escapedQuery = $this->db->escape_str($query);
        $escapedQuery = str_replace('%', '', $escapedQuery);

        $clients = $this->mdl_clients
            ->where('client_active', 1)
            ->having("client_name LIKE '" . $moreClientsQuery . $escapedQuery . "%'")
            ->or_having("client_surname LIKE '" . $moreClientsQuery . $escapedQuery . "%'")
            ->or_having("client_fullname LIKE '" . $moreClientsQuery . $escapedQuery . "%'")
            ->order_by('client_name')
            ->get()
            ->result();

        foreach ($clients as $client) {
            $response[] = [
                'id'   => $client->client_id,
                'text' => htmlsc(format_client($client, false)),
            ];
        }

        // Return the results
        echo json_encode($response);
    }

    /**
     * Get the latest clients.
     */
    public function get_latest()
    {
        // Load the model & helper
        $this->load->model('clients/mdl_clients');

        $response = [];

        $clients = $this->mdl_clients
            ->where('client_active', 1)
            ->limit(5)
            ->order_by('client_date_created')
            ->get()
            ->result();

        foreach ($clients as $client) {
            $response[] = [
                'id'   => $client->client_id,
                'text' => htmlsc(format_client($client, false)),
            ];
        }

        // Return the results
        echo json_encode($response);
    }

    public function save_preference_permissive_search_clients()
    {
        $this->load->model('
...[truncated]...

### application/modules/clients/models/Mdl_clients.php
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
class Mdl_Clients extends Response_Model
{
    public $table = 'ip_clients';

    public $primary_key = 'ip_clients.client_id';

    public $date_created_field = 'client_date_created';

    public $date_modified_field = 'client_date_modified';

    public function default_select(): void
    {
        $this->db->select('SQL_CALC_FOUND_ROWS ' . $this->table . '.*, CONCAT(' . $this->table . '.client_name, " ", ' . $this->table . '.client_surname) as client_fullname', false);
    }

    public function default_order_by(): void
    {
        if (get_setting('sort_clients_by_surname') == '1') {
            $this->db->order_by('ip_clients.client_surname');
        } else {
            $this->db->order_by('ip_clients.client_name');
        }
    }

    public function validation_rules()
    {
        return [
            'client_title' => [
                'field' => 'client_title',
                'label' => trans('client_title'),
            ],
            'client_name' => [
                'field' => 'client_name',
                'label' => trans('client_name'),
                'rules' => 'required',
            ],
            'client_surname' => [
                'field' => 'client_surname',
                'label' => trans('client_surname'),
            ],
            'client_active' => [
                'field' => 'client_active',
            ],
            'client_language' => [
                'field' => 'client_language',
                'label' => trans('language'),
                'rules' => 'trim',
            ],
            'client_address_1' => [
                'field' => 'client_address_1',
            ],
            'client_address_2' => [
                'field' => 'client_address_2',
            ],
            'client_city' => [
                'field' => 'client_city',
            ],
            'client_state' => [
                'field' => 'client_state',
            ],
            'client_zip' => [
                'field' => 'client_zip',
            ],
            'client_country' => [
                'field' => 'client_country',
                'rules' => 'trim',
            ],
            'client_phone' => [
                'field' => 'client_phone',
            ],
            'client_fax' => [
 
...[truncated]...

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

### application/modules/invoices/controllers/Invoices.php
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
class Invoices extends Admin_Controller
{
    /**
     * Invoices constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->load->helper('file_security');
        $this->load->model('mdl_invoices');
    }

    public function index(): void
    {
        // Display all invoices by default
        redirect('invoices/status/all');
    }

    /**
     * @param int $page
     */
    public function status(string $status = 'all', $page = 0): void
    {
        // Determine which group of invoices to load
        switch ($status) {
            case 'draft':
                $this->mdl_invoices->is_draft();
                break;
            case 'sent':
                $this->mdl_invoices->is_sent();
                break;
            case 'viewed':
                $this->mdl_invoices->is_viewed();
                break;
            case 'paid':
                $this->mdl_invoices->is_paid();
                break;
            case 'overdue':
                $this->mdl_invoices->is_overdue();
                break;
        }

        $this->mdl_invoices->paginate(site_url('invoices/status/' . $status), $page);
        $invoices = $this->mdl_invoices->result();

        $this->layout->set(
            [
                'invoices'           => $invoices,
                'status'             => $status,
                'filter_display'     => true,
                'filter_placeholder' => trans('filter_invoices'),
                'filter_method'      => 'filter_invoices',
                'invoice_statuses'   => $this->mdl_invoices->statuses(),
            ]
        );

        $this->layout->buffer('content', 'invoices/index');
        $this->layout->render();
    }

    public function archive(): void
    {
        $invoice_array = $this->mdl_invoices->get_archives(0);
        $this->layout->set(
            [
                'filter_display'     => true,
                'filter_placeholder' => trans('filter_archives'),
                'filter_method'      => 'filter_archives',
                'invoices_archive'   => $invoice_array,
            ]
        );
        $this->layout->buffer('content', 'invoices/archive');
        $this->layout->render();
    }

    public function
...[truncated]...

### application/modules/invoices/controllers/Ajax.php
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
class Ajax extends Admin_Controller
{
    public $ajax_controller = true;

    public function save()
    {
        $this->load->model([
            'invoices/mdl_items',
            'invoices/mdl_invoices',
            'units/mdl_units',
            'invoices/mdl_invoice_sumex',
        ]);

        $invoice_id = $this->security->xss_clean($this->input->post('invoice_id', true));

        $this->mdl_invoices->set_id($invoice_id);

        if ($this->mdl_invoices->run_validation('validation_rules_save_invoice')) {
            $items = json_decode($this->input->post('items'));

            $invoice_discount_percent = (float) $this->input->post('invoice_discount_percent');
            $invoice_discount_amount  = (float) $this->input->post('invoice_discount_amount');

            // Percent by default. Only one allowed. Prevent set 2 global discounts by geeky client - since v1.6.3
            if ($invoice_discount_percent && $invoice_discount_amount) {
                $invoice_discount_amount = 0.0;
            }

            // New discounts (for legacy_calculation false) - since v1.6.3 Need if taxes applied after discounts
            $items_subtotal = 0.0;
            if ($invoice_discount_amount) {
                foreach ($items as $item) {
                    if ( ! empty($item->item_name)) {
                        $items_subtotal += standardize_amount($item->item_quantity) * standardize_amount($item->item_price);
                    }
                }
            }

            // New discounts (for legacy_calculation false) - since v1.6.3 Need if taxes applied after discounts
            $global_discount = [
                'amount'         => $invoice_discount_amount ? standardize_amount($invoice_discount_amount) : 0.0,
                'percent'        => $invoice_discount_percent ? standardize_amount($invoice_discount_percent) : 0.0,
                'item'           => 0.0, // Updated by ref (Need for invoice_item_subtotal calculation in Mdl_invoice_amounts)
                'items_subtotal' => $items_subtotal,
            ];

            // Automatic calculation mode
            if (get_setting('einvoicing')) {
                // Shift to false (by default). Need true? See Dev Note on ipconfig example
    
...[truncated]...

### application/modules/invoices/models/Mdl_invoices.php
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
class Mdl_Invoices extends Response_Model
{
    public $table = 'ip_invoices';

    public $primary_key = 'ip_invoices.invoice_id';

    public $date_modified_field = 'invoice_date_modified';

    /**
     * @return array
     */
    public function statuses()
    {
        return [
            '1' => [
                'label' => trans('draft'),
                'class' => 'draft',
                'href'  => 'invoices/status/draft',
            ],
            '2' => [
                'label' => trans('sent'),
                'class' => 'sent',
                'href'  => 'invoices/status/sent',
            ],
            '3' => [
                'label' => trans('viewed'),
                'class' => 'viewed',
                'href'  => 'invoices/status/viewed',
            ],
            '4' => [
                'label' => trans('paid'),
                'class' => 'paid',
                'href'  => 'invoices/status/paid',
            ],
        ];
    }

    public function default_select()
    {
        $this->db->select("
            SQL_CALC_FOUND_ROWS
            ip_quotes.*,
            ip_users.*,
            ip_clients.*,
            ip_invoice_sumex.*,
            ip_invoice_amounts.invoice_amount_id,
            IFnull(ip_invoice_amounts.invoice_item_subtotal, '0.00') AS invoice_item_subtotal,
            IFnull(ip_invoice_amounts.invoice_item_tax_total, '0.00') AS invoice_item_tax_total,
            IFnull(ip_invoice_amounts.invoice_tax_total, '0.00') AS invoice_tax_total,
            IFnull(ip_invoice_amounts.invoice_total, '0.00') AS invoice_total,
            IFnull(ip_invoice_amounts.invoice_paid, '0.00') AS invoice_paid,
            IFnull(ip_invoice_amounts.invoice_balance, '0.00') AS invoice_balance,
            ip_invoice_amounts.invoice_sign AS invoice_sign,
            (CASE WHEN ip_invoices.invoice_status_id NOT IN (1,4) AND DATEDIFF(NOW(), invoice_date_due) > 0 THEN 1 ELSE 0 END) is_overdue,
            DATEDIFF(NOW(), invoice_date_due) AS days_overdue,
            (CASE (SELECT COUNT(*) FROM ip_invoices_recurring WHERE ip_invoices_recurring.invoice_id = ip_invoices.invoice_id and ip_invoices_recurring.recur_next_date IS NOT NULL) WHEN 0 THEN 0 ELSE 1 END) AS invoice_is_recurring,
            ip
...[truncated]...

### application/modules/invoices/models/Mdl_items.php
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
class Mdl_Items extends Response_Model
{
    public $table = 'ip_invoice_items';

    public $primary_key = 'ip_invoice_items.item_id';

    public $date_created_field = 'item_date_added';

    public function default_select()
    {
        $this->db->select('ip_invoice_item_amounts.*, ip_products.*, ip_invoice_items.*,
            item_tax_rates.tax_rate_percent AS item_tax_rate_percent,
            item_tax_rates.tax_rate_name AS item_tax_rate_name');
    }

    public function default_order_by()
    {
        $this->db->order_by('ip_invoice_items.item_order');
    }

    public function default_join()
    {
        $this->db->join('ip_invoice_item_amounts', 'ip_invoice_item_amounts.item_id = ip_invoice_items.item_id', 'left');
        $this->db->join('ip_tax_rates AS item_tax_rates', 'item_tax_rates.tax_rate_id = ip_invoice_items.item_tax_rate_id', 'left');
        $this->db->join('ip_products', 'ip_products.product_id = ip_invoice_items.item_product_id', 'left');
    }

    /**
     * @return array
     */
    public function validation_rules()
    {
        return [
            'invoice_id' => [
                'field' => 'invoice_id',
                'label' => trans('invoice'),
                'rules' => 'required',
            ],
            'item_sku' => [
                'field' => 'item_sku',
                'label' => trans('item_sku'),
                'rules' => 'required|unique',
            ],
            'item_name' => [
                'field' => 'item_name',
                'label' => trans('item_name'),
                'rules' => 'required',
            ],
            'item_description' => [
                'field' => 'item_description',
                'label' => trans('description'),
            ],
            'item_quantity' => [
                'field' => 'item_quantity',
                'label' => trans('quantity'),
                'rules' => 'required',
            ],
            'item_price' => [
                'field' => 'item_price',
                'label' => trans('price'),
                'rules' => 'required',
            ],
            'item_tax_rate_id' => [
                'field' => 'item_tax_rate_id',
                'label' => trans('item_tax_rate'),
            ],
           
...[truncated]...

### application/modules/invoices/views/modal_create_invoice.php
<script>
    $(function () {
        // Display the create invoice modal
        $('#create-invoice').modal('show');

        // Enable select2 for all selects
        $('.simple-select').select2();

        <?php $this->layout->load_view('clients/script_select2_client_id.js'); ?>

        // Creates the invoice
        $('#invoice_create_confirm').click(function () {
            // Posts the data to validate and create the invoice;
            // will create the new client if necessar
            $.post("<?php echo site_url('invoices/ajax/create'); ?>", {
                    client_id: $('#create_invoice_client_id').val(),
                    invoice_date_created: $('#invoice_date_created').val(),
                    invoice_group_id: $('#invoice_group_id').val(),
                    invoice_time_created: '<?php echo date('H:i:s') ?>',
                    invoice_password: $('#invoice_password').val(),
                    user_id: '<?php echo $this->session->userdata('user_id'); ?>',
                    payment_method: $('#payment_method_id').val()
                },
                function (data) {
                    var response = json_parse(data, <?php echo (int) IP_DEBUG; ?>);
                    if (response.success === 1) {
                        // The validation was successful and invoice was created
                        window.location = "<?php echo site_url('invoices/view'); ?>/" + response.invoice_id;
                    }
                    else {
                        // The validation was not successful
                        $('.control-group').removeClass('has-error');
                        for (var key in response.validation_errors) {
                            $('#' + key).parent().parent().addClass('has-error');
                        }
                    }
                });
        });
    });

</script>

<div id="create-invoice" class="modal modal-lg"
     role="dialog" aria-labelledby="modal_create_invoice" aria-hidden="true">
    <form class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><i class="fa fa-close"></i></button>
            <h4 class="panel-title"><?php _trans('create_invoice'); ?></h4>
        </div>
        <div class="modal-body">

            <input class="hidden" id="payment_method_id"
                   value="<?php echo html_escape(get_setting('invoice_default_payment_method')); ?>">
            <input class="hidden" id="input_permissive_search_clients"
                   value="<?php echo html_escape(get_setting('enable_p
...[truncated]...

### application/modules/quotes/controllers/Quotes.php
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
class Quotes extends Admin_Controller
{
    /**
     * Quotes constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->load->model('mdl_quotes');
    }

    public function index()
    {
        // Display all quotes by default
        redirect('quotes/status/all');
    }

    /**
     * @param int $page
     */
    public function status(string $status = 'all', $page = 0)
    {
        // Determine which group of quotes to load
        switch ($status) {
            case 'draft':
                $this->mdl_quotes->is_draft();
                break;
            case 'sent':
                $this->mdl_quotes->is_sent();
                break;
            case 'viewed':
                $this->mdl_quotes->is_viewed();
                break;
            case 'approved':
                $this->mdl_quotes->is_approved();
                break;
            case 'rejected':
                $this->mdl_quotes->is_rejected();
                break;
            case 'canceled':
                $this->mdl_quotes->is_canceled();
                break;
        }

        $this->mdl_quotes->paginate(site_url('quotes/status/' . $status), $page);
        $quotes = $this->mdl_quotes->result();

        $this->layout->set(
            [
                'quotes'             => $quotes,
                'status'             => $status,
                'filter_display'     => true,
                'filter_placeholder' => trans('filter_quotes'),
                'filter_method'      => 'filter_quotes',
                'quote_statuses'     => $this->mdl_quotes->statuses(),
            ]
        );

        $this->layout->buffer('content', 'quotes/index');
        $this->layout->render();
    }

    /**
     * @param $quote_id
     */
    public function view($quote_id)
    {
        $this->load->model(
            [
                'quotes/mdl_quote_items',
                'tax_rates/mdl_tax_rates',
                'units/mdl_units',
                'mdl_quote_tax_rates',
                'custom_fields/mdl_custom_fields',
                'custom_values/mdl_custom_values',
                'custom_fields/mdl_quote_custom',
                'upload/mdl_uploads',
            ]
        );

       
...[truncated]...

### application/modules/quotes/models/Mdl_quotes.php
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
class Mdl_Quotes extends Response_Model
{
    public $table = 'ip_quotes';

    public $primary_key = 'ip_quotes.quote_id';

    public $date_modified_field = 'quote_date_modified';

    /**
     * @return array
     */
    public function statuses()
    {
        return [
            '1' => [
                'label' => trans('draft'),
                'class' => 'draft',
                'href'  => 'quotes/status/draft',
            ],
            '2' => [
                'label' => trans('sent'),
                'class' => 'sent',
                'href'  => 'quotes/status/sent',
            ],
            '3' => [
                'label' => trans('viewed'),
                'class' => 'viewed',
                'href'  => 'quotes/status/viewed',
            ],
            '4' => [
                'label' => trans('approved'),
                'class' => 'approved',
                'href'  => 'quotes/status/approved',
            ],
            '5' => [
                'label' => trans('rejected'),
                'class' => 'rejected',
                'href'  => 'quotes/status/rejected',
            ],
            '6' => [
                'label' => trans('canceled'),
                'class' => 'canceled',
                'href'  => 'quotes/status/canceled',
            ],
        ];
    }

    public function default_select()
    {
        $this->db->select("
            SQL_CALC_FOUND_ROWS
            ip_users.*,
            ip_clients.*,
            ip_quote_amounts.quote_amount_id,
            IFnull(ip_quote_amounts.quote_item_subtotal, '0.00') AS quote_item_subtotal,
            IFnull(ip_quote_amounts.quote_item_tax_total, '0.00') AS quote_item_tax_total,
            IFnull(ip_quote_amounts.quote_tax_total, '0.00') AS quote_tax_total,
            IFnull(ip_quote_amounts.quote_total, '0.00') AS quote_total,
            ip_invoices.invoice_number,
            ip_quotes.*", false);
    }

    public function save($id = null, $db_array = null)
    {
        if (is_array($db_array) && array_key_exists('quote_password', $db_array)) {
            $db_array['quote_password'] = $this->encrypt_quote_password($db_array['quote_password']);
        }

        return parent::save($id, $db_array);
    }

    public function e
...[truncated]...

### application/modules/quotes/views/modal_quote_to_invoice.php
<script>
    $(function () {
        // Display the create quote modal
        $('#modal_quote_to_invoice').modal('show');

        // Select2 for all select inputs
        $(".simple-select").select2();

        // Creates the invoice
        $('#quote_to_invoice_confirm').click(function () {
            show_loader(); // Show spinner
            $.post("<?php echo site_url('quotes/ajax/quote_to_invoice'); ?>", {
                    legacy_calculation: legacy_calculation, // Automatic. From meta (see script)
                    quote_id: <?php echo $quote_id; ?>,
                    client_id: $('#client_id').val(),
                    invoice_date_created: $('#invoice_date_created').val(),
                    invoice_time_created: '<?php echo date('H:i:s') ?>',
                    invoice_group_id: $('#invoice_group_id').val(),
                    invoice_password: $('#invoice_password').val(),
                    user_id: $('#user_id').val()
                },
                function (data) {
                    var response = json_parse(data, <?php echo (int) IP_DEBUG; ?>);
                    if (response.success === 1) {
                        window.location = "<?php echo site_url('invoices/view'); ?>/" + response.invoice_id;
                    }
                    else {
                        // The validation was not successful
                        close_loader();
                        $('.control-group').removeClass('has-error');
                        for (var key in response.validation_errors) {
                            $('#' + key).parent().parent().addClass('has-error');
                        }
                    }
                }
            );
        });
    });
</script>

<div id="modal_quote_to_invoice" class="modal modal-lg" role="dialog" aria-labelledby="modal_quote_to_invoice"
     aria-hidden="true">
    <form class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><i class="fa fa-close"></i></button>
            <h4 class="panel-title"><?php _trans('quote_to_invoice'); ?></h4>
        </div>
        <div class="modal-body">

            <input type="hidden" name="client_id" id="client_id"
                   value="<?php echo $quote->client_id; ?>">
            <input type="hidden" name="user_id" id="user_id"
                   value="<?php echo $quote->user_id; ?>">

            <div class="form-group has-feedback">
                <label for="invoice_date_created">
                    <?php _trans('invoice_date'); ?>
                </label
...[truncated]...

### application/modules/payments/controllers/Payments.php
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
class Payments extends Admin_Controller
{
    /**
     * Payments constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->load->model('mdl_payments');
    }

    /**
     * @param int $page
     */
    public function index($page = 0)
    {
        $this->mdl_payments->paginate(site_url('payments/index'), $page);
        $payments = $this->mdl_payments->result();

        $this->layout->set(
            [
                'filter_display'     => true,
                'filter_placeholder' => trans('filter_payments'),
                'filter_method'      => 'filter_payments',
                'payments'           => $payments,
            ]
        );

        $this->layout->buffer('content', 'payments/index');
        $this->layout->render();
    }

    public function form($id = null)
    {
        if ($this->input->post('btn_cancel')) {
            redirect('payments');
        }

        $this->load->model('custom_fields/mdl_payment_custom');

        if ($this->mdl_payments->run_validation()) {
            $id = $this->mdl_payments->save($id);

            $this->mdl_payment_custom->save_custom($id, $this->input->post('custom'));

            redirect('payments');
        }

        if ( ! $this->input->post('btn_submit')) {
            $prep_form = $this->mdl_payments->prep_form($id);
            if ($id && ! $prep_form) {
                show_404();
            }

            $this->load->model('custom_values/mdl_custom_values');
            $payment_custom = $this->mdl_payment_custom->where('payment_id', $id)->get();
            if ($payment_custom->num_rows()) {
                $payment_custom = $payment_custom->row();

                unset($payment_custom->payment_id, $payment_custom->payment_custom_id);

                foreach ($payment_custom as $key => $val) {
                    $this->mdl_payments->set_form_value('custom[' . $key . ']', $val);
                }
            }
        } elseif ($this->input->post('custom')) {
            foreach ($this->input->post('custom') as $key => $val) {
                $this->mdl_payments->set_form_value('custom[' . $key . ']', $val);
            }
        }

        $this->load->helper('custom_values');
        
...[truncated]...

### application/modules/payments/controllers/Ajax.php
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
class Ajax extends Admin_Controller
{
    public $ajax_controller = true;

    public function add()
    {
        $this->load->model('payments/mdl_payments');

        if ($this->mdl_payments->run_validation()) {
            $payment_id = $this->mdl_payments->save();

            $response = [
                'success'    => 1,
                'payment_id' => $payment_id,
            ];
        } else {
            $this->load->helper('json_error');
            $response = [
                'success'           => 0,
                'validation_errors' => json_errors(),
            ];
        }

        echo json_encode($response);
    }

    public function modal_add_payment()
    {
        $this->load->module('layout');
        $this->load->model('payments/mdl_payments');
        $this->load->model('payment_methods/mdl_payment_methods');
        $this->load->model('custom_fields/mdl_payment_custom');

        $data = [
            'payment_methods'        => $this->mdl_payment_methods->get()->result(),
            'invoice_id'             => $this->security->xss_clean($this->input->post('invoice_id')),
            'invoice_balance'        => $this->input->post('invoice_balance'),
            'invoice_payment_method' => $this->input->post('invoice_payment_method'),
            'payment_cf_exist'       => $this->security->xss_clean($this->input->post('payment_cf_exist')),
        ];

        $this->layout->load_view('payments/modal_add_payment', $data);
    }
}

### application/modules/payments/models/Mdl_payments.php
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
class Mdl_Payments extends Response_Model
{
    public $tabl
...[truncated]...