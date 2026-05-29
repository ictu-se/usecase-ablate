# Deterministic random code snippets
### application/modules/quotes/views/modal_create_quote.php
<script>
    $(function () {
        // Display the create quote modal
        $('#create-quote').modal('show');

        // Select2 for all select inputs
        $('.simple-select').select2();

        <?php $this->layout->load_view('clients/script_select2_client_id.js'); ?>

        // Creates the quote
        $('#quote_create_confirm').click(function () {
            show_loader(); // Show spinner
            // Posts the data to validate and create the quote;
            // will create the new client if necessary
            $.post("<?php echo site_url('quotes/ajax/create'); ?>", {
                    client_id: $('#create_quote_client_id').val(),
                    quote_date_created: $('#quote_date_created').val(),
                    quote_password: $('#quote_password').val(),
                    user_id: '<?php echo $this->session->userdata('user_id'); ?>',
                    invoice_group_id: $('#invoice_group_id').val()
                },
                function (data) {
                    var response = json_parse(data, <?php echo (int) IP_DEBUG; ?>);
                    if (response.success === 1) {
                        // The validation was successful and quote was created
                        window.location = "<?php echo site_url('quotes/view'); ?>/" + response.quote_id;
                    }
                    else {
                        // The validation was not successful
                        close_loader();
                        $('.control-group').removeClass('has-error');
                        for (var key in response.validation_errors) {
                            $('#' + key).parent().parent().addClass('has-error');
                        }
                    }
                });
        });
    });
</script>

<div id="create-quote" class="modal modal-lg" role="dialog" aria-labelledby="modal_create_quote" aria-hidden="true">
    <form class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><i class="fa fa-close"></i></button>
            <h4 class="panel-title"><?php _trans('create_quote'); ?></h4>
        </div>
        <div class="modal-body">

            <input class="hidden" id="input_permissive_search_clients"
                   value="<?php echo html_escape(get_setting('enable_permissive_search_clients')); ?>">

            <div class="form-group has-feedback">
                <label for="create_quote_client_id"><?php _trans('client'); ?></label>
                <div class="input-group">
                    <span id="toggle_permi
...[truncated]...

### application/modules/guest/controllers/gateways/Paypal.php
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
class Paypal extends Base_Controller
{
    public function __construct()
    {
        parent::__construct();
        $this->load->helper('file_security');
        $this->_create_client();
    }

    /**
     * Create the order on PayPal that is then processed when
     * the user inserts the payment method.
     *
     * @param string $invoice_url_key
     *
     * @return json the PayPal object to be loaded in the JS SDK script
     */
    public function paypal_create_order($invoice_url_key)
    {
        // Require POST request to prevent CSRF attacks
        if ($this->input->method() !== 'post') {
            show_404();
        }

        // Check if the invoice exists and is billable
        $this->load->model('invoices/mdl_invoices');

        $invoice = $this->mdl_invoices->guest_visible()->where('ip_invoices.invoice_url_key', $invoice_url_key)->get()->row();

        // Security: Verify the invoice exists and is guest-visible
        if ( ! $invoice) {
            log_message('error', __CLASS__ . '::' . __FUNCTION__ . ' - Attempted order creation for non-public or non-existent invoice with key: ' . sanitize_for_logging($invoice_url_key));
            show_404();
        }

        // Check if the invoice is payable
        if ($invoice->invoice_balance <= 0) {
            $this->session->set_userdata('alert_error', lang('invoice_already_paid'));
            redirect(site_url('guest/view/invoice/' . $invoice->invoice_url_key));
        }

        //create the order
        $paypal_client = $this->lib_paypal->createOrder([
            'invoice_id'    => $invoice->invoice_id,
            'currency_code' => get_setting('gateway_paypal_currency'),
            'value'         => $invoice->invoice_balance,
            'custom_id'     => $invoice_url_key,
        ]);

        // Decode the PayPal response
        $paypal_response = json_decode($paypal_client, true);

        // Handle JSON decode errors
        if (json_last_error() !== JSON_ERROR_NONE) {
            log_message('error', 'PayPal createOrder JSON decode error for invoice ' . sanitize_for_logging($invoice_url_key) . ': ' . sanitize_for_logging(json_last_error_msg()));
            $this->output
                ->set_status_header(500)
             
...[truncated]...

### application/modules/quotes/models/Mdl_quote_items.php
<?php

if ( ! defined('BASEPATH')) {
    exit('No direct script access allowed');
}

/*
 * InvoicePlane
 *
 * @author		InvoicePlane Developers & Contributors
 * @copyright	Copyright (c) 2012 - 2018 InvoicePlane.com
 * @license		https://invoiceplane.com/license.txt
 * @link		https://invoiceplane.com
 */

#[AllowDynamicProperties]
class Mdl_Quote_Items extends Response_Model
{
    public $table = 'ip_quote_items';

    public $primary_key = 'ip_quote_items.item_id';

    public $date_created_field = 'item_date_added';

    public function default_select()
    {
        $this->db->select('ip_quote_item_amounts.*, ip_products.*, ip_quote_items.*,
            item_tax_rates.tax_rate_percent AS item_tax_rate_percent,
            item_tax_rates.tax_rate_name AS item_tax_rate_name');
    }

    public function default_order_by()
    {
        $this->db->order_by('ip_quote_items.item_order');
    }

    public function default_join()
    {
        $this->db->join('ip_quote_item_amounts', 'ip_quote_item_amounts.item_id = ip_quote_items.item_id', 'left');
        $this->db->join('ip_tax_rates AS item_tax_rates', 'item_tax_rates.tax_rate_id = ip_quote_items.item_tax_rate_id', 'left');
        $this->db->join('ip_products', 'ip_products.product_id = ip_quote_items.item_product_id', 'left');
    }

    /**
     * @return array
     */
    public function validation_rules()
    {
        return [
            'quote_id' => [
                'field' => 'quote_id',
                'label' => trans('quote'),
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
            ],
            'item_price' => [
                'field' => 'item_price',
                'label' => trans('price'),
            ],
            'item_tax_rate_id' => [
                'field' => 'item_tax_rate_id',
                'label' => trans('item_tax_rate'),
            ],
            'item_product_id' => [
                'field' => 'item_product_id',
                'label' => trans('original_
...[truncated]...

### application/core/Response_Model.php
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
class Response_Model extends Form_Validation_Model
{
    /**
     * @param null|int   $id
     * @param null|array $db_array
     *
     * @return null|int
     */
    public function save($id = null, $db_array = null)
    {
        if ($id) {
            $this->session->set_flashdata('alert_success', trans('record_successfully_updated'));
            parent::save($id, $db_array);
        } else {
            $this->session->set_flashdata('alert_success', trans('record_successfully_created'));
            $id = parent::save(null, $db_array);
        }

        return $id;
    }

    /**
     * @param int $id
     */
    public function delete($id)
    {
        parent::delete($id);

        $this->session->set_flashdata('alert_success', trans('record_successfully_deleted'));
    }
}

### application/modules/clients/views/partial_client_address.php
<span class="client-address-street-line">
    <?php echo $client->client_address_1 ? htmlsc($client->client_address_1) . '<br>' : ''; ?>
</span>
<span class="client-address-street-line">
    <?php echo $client->client_address_2 ? htmlsc($client->client_address_2) . '<br>' : ''; ?>
</span>
<span class="client-adress-town-line">
    <?php echo $client->client_city ? htmlsc($client->client_city) . ' ' : ''; ?>
    <?php echo $client->client_state ? htmlsc($client->client_state) . ' ' : ''; ?>
    <?php echo $client->client_zip ? htmlsc($client->client_zip) : ''; ?>
</span>
<span class="client-adress-country-line">
    <?php echo $client->client_country ? '<br>' . get_country_name(trans('cldr'), $client->client_country) : ''; ?>
</span>

### application/helpers/ip_security_helper.php
<?php

if ( ! defined('BASEPATH')) {
    exit('No direct script access allowed');
}

/*
 * InvoicePlane
 *
 * @author      InvoicePlane Developers & Contributors
 * @copyright   Copyright (c) 2012 - 2025 InvoicePlane.com
 * @license     https://invoiceplane.com/license.txt
 * @link        https://invoiceplane.com
 */

/**
 * InvoicePlane Security Helper.
 *
 * Provides cryptographically secure functions for token generation, password reset tokens,
 * and other security-critical operations. This helper uses PHP's random_bytes() for CSPRNG.
 *
 * Note: This helper is named 'ip_security' to avoid conflicts with CodeIgniter's core
 * 'security' helper which provides different functionality (XSS filtering, CSRF, etc).
 */

/**
 * Sanitize exception message for logging to prevent log injection.
 *
 * @param string $message The exception message to sanitize
 *
 * @return string The sanitized message
 */
function sanitize_exception_for_logging(string $message): string
{
    // Try to use file_security_helper if loaded
    if (function_exists('sanitize_for_logging')) {
        return sanitize_for_logging($message);
    }

    // Fallback: Remove control characters to prevent log injection
    return str_replace(["\r", "\n"], '', $message);
}

/**
 * Generate a cryptographically secure random token.
 *
 * Uses PHP's random_bytes() with fallback to paragonie/random_compat for older PHP versions.
 * Provides 128+ bits of entropy for security-critical operations like password resets.
 *
 * @param int $length The length of the raw token in bytes (default: 32 bytes = 256 bits)
 *                    Must be greater than 0. The returned hex string will be twice this length.
 *
 * @return string The token as a hexadecimal string (twice the byte length)
 *
 * @throws InvalidArgumentException If $length is less than or equal to 0
 * @throws RuntimeException         If random_bytes() fails (should never happen with PHP 7.0+)
 */
function generate_secure_token(int $length = 32): string
{
    // Validate input: length must be positive
    if ($length <= 0) {
        throw new InvalidArgumentException('Token length must be greater than 0, got: ' . $length);
    }

    try {
        // Generate cryptographically secure random bytes
        $randomBytes = random_bytes($length);

        // Convert to hexadecimal for safe storage and transmission
        return bin2hex($randomBytes);
    } catch (Exception|Error $e) {
        // This should never happen with PHP 7.0+ or random_compat library
        // Catch both Exception and Error for comprehensive coverage
        $safeMessage 
...[truncated]...

### application/helpers/country-list/ca/country.php
<?php

return [
    'AF' => 'Afganistan',
    'AL' => 'Albània',
    'DE' => 'Alemanya',
    'DZ' => 'Algèria',
    'AD' => 'Andorra',
    'AO' => 'Angola',
    'AI' => 'Anguilla',
    'AG' => 'Antigua i Barbuda',
    'AN' => 'Antilles Neerlandeses',
    'AQ' => 'Antàrtida',
    'AR' => 'Argentina',
    'AM' => 'Armènia',
    'AW' => 'Aruba',
    'SA' => 'Aràbia Saudita',
    'AU' => 'Austràlia',
    'AZ' => 'Azerbaidjan',
    'BS' => 'Bahames',
    'BH' => 'Bahrain',
    'BD' => 'Bangla Desh',
    'BB' => 'Barbados',
    'BZ' => 'Belize',
    'BJ' => 'Benín',
    'BM' => 'Bermudes',
    'BT' => 'Bhutan',
    'BY' => 'Bielorússia',
    'BO' => 'Bolívia',
    'BW' => 'Botswana',
    'BR' => 'Brasil',
    'BN' => 'Brunei',
    'BG' => 'Bulgària',
    'BF' => 'Burkina Faso',
    'BI' => 'Burundi',
    'BE' => 'Bèlgica',
    'BA' => 'Bòsnia i Hercegovina',
    'KH' => 'Cambodja',
    'CM' => 'Camerun',
    'CA' => 'Canadà',
    'CV' => 'Cap Verd',
    'CO' => 'Colòmbia',
    'KM' => 'Comores',
    'CG' => 'Congo',
    'KP' => 'Corea del Nord',
    'KR' => 'Corea del Sud',
    'CR' => 'Costa Rica',
    'CI' => 'Costa d’Ivori',
    'HR' => 'Croàcia',
    'CU' => 'Cuba',
    'DK' => 'Dinamarca',
    'DJ' => 'Djibouti',
    'DM' => 'Dominica',
    'EG' => 'Egipte',
    'SV' => 'El Salvador',
    'EC' => 'Equador',
    'ER' => 'Eritrea',
    'SK' => 'Eslovàquia',
    'SI' => 'Eslovènia',
    'ES' => 'Espanya',
    'US' => 'Estats Units',
    'EE' => 'Estònia',
    'ET' => 'Etiòpia',
    'FJ' => 'Fiji',
    'PH' => 'Filipines',
    'FI' => 'Finlàndia',
    'FR' => 'França',
    'GA' => 'Gabon',
    'GE' => 'Geòrgia',
    'GH' => 'Ghana',
    'GI' => 'Gibraltar',
    'GD' => 'Grenada',
    'GL' => 'Grenlàndia',
    'GR' => 'Grècia',
    'GP' => 'Guadeloupe',
    'GF' => 'Guaiana Francesa',
    'GU' => 'Guam',
    'GT' => 'Guatemala',
    'GG' => 'Guernsey',
    'GN' => 'Guinea',
    'GW' => 'Guinea Bissau',
    'GQ' => 'Guinea Equatorial',
    'GY' => 'Guyana',
    'GM' => 'Gàmbia',
    'HT' => 'Haití',
    'HN' => 'Hondures',
    'HU' => 'Hongria',
    'YE' => 'Iemen',
    'BV' => 'Illa Bouvet',
    'CX' => 'Illa Christmas',
    'HM' => 'Illa Heard i Illes McDonald',
    'NF' => 'Illa Norfolk',
    'IM' => 'Illa de Man',
    'RE' => 'Illa de la Reunió',
    'KY' => 'Illes Caiman',
    'CC' => 'Illes Cocos',
    'CK' => 'Illes Cook',
    'FO' => 'Illes Fèroe',
    'GS' => 'Illes Geòrgia del Sud i Sandwich del Sud',
    'FK' => 'Illes Malvines',
    'MP' => 'Illes Mariannes del Nord',
    'MH' => 'Illes Marshall',
    'UM' => 'Illes Perifèriques Menors dels EUA',
  
...[truncated]...

### application/libraries/index.html
<html>
<head>
    <title>403 Forbidden</title>
</head>
<body>

<p>Directory access is forbidden.</p>

</body>
</html>

### application/third_party/MX/Controller.php
<?php

if ( ! defined('BASEPATH')) {
    exit('No direct script access allowed');
}

/** load the CI class for Modular Extensions **/
require dirname(__FILE__) . '/Base.php';

/**
 * Modular Extensions - HMVC.
 *
 * Adapted from the CodeIgniter Core Classes
 *
 * @see    http://codeigniter.com
 *
 * Description:
 * This library replaces the CodeIgniter Controller class
 * and adds features allowing use of modules and the HMVC design pattern.
 *
 * Install this file as application/third_party/MX/Controller.php
 *
 * @copyright    Copyright (c) 2015 Wiredesignz
 *
 * @version    5.5
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 **/
#[AllowDynamicProperties]
class MX_Controller
{
    public $load;

    public $autoload = [];

    public function __construct()
    {
        if (CI::$APP->config->item('controller_suffix') == null) {
        $class = str_replace('', '', get_class($this));
        } else {
        $class = str_replace(CI::$APP->config->item('controller_suffix'), '', get_class($this));
        }

        log_message('debug', $class . ' MX_Controller Initialized');
        Modules::$registry[mb_strtolower($class)] = $this;

        // copy a loader instance and initialize
        $this->load = clone load_class('Loader');
        $this->load->initialize($this);

        // autoload module items
        $this->load->_autoloader($this->autoload);
    }

    public function __get($class)
    {
        return CI::$APP->{$class};
    }
}

### application/modules/settings/controllers/Settings.php
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
class Settings extends Admin_Controller
{
    private const MIN_TAX_RATE_DECIMALS = 2;

    private const MAX_TAX_RATE_DECIMALS = 3;

    /**
     * Settings constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->load->model('mdl_settings');
        $this->load->library('crypt');
        $this->load->library('form_validation');
        $this->load->helper('payments_helper');
        $this->load->helper('file_security');

        // Security: Check for SVG logos and display warnings
        $this->check_svg_logos();
    }

    public function index()
    {
        // Get the payment gateway configurations
        $this->config->load('payment_gateways');
        $gateways = $this->config->item('payment_gateways');

        // Get the number formats configurations
        $this->config->load('number_formats');
        $number_formats = $this->config->item('number_formats');

        // Save input if request is POSt
        if ($this->input->post('settings')) {
            $settings = $this->input->post('settings');

            $settings = $this->handleTaxRateDecimalPlaces($settings);

            // Build array of all settings to save in a single batch operation
            $batch_settings = [];

            foreach ($settings as $key => $value) {
                if (str_contains($key, 'field_is_password') || str_contains($key, 'field_is_amount')) {
                    // Skip all meta fields
                    continue;
                }

                if (isset($settings[$key . '_field_is_password']) && empty($value)) {
                    // Password field, but empty value, let's skip it
                    continue;
                }

                if (isset($settings[$key . '_field_is_password']) && $value !== '') {
                    // Encrypt passwords but don't save empty passwords
                    $batch_settings[$key] = $this->crypt->encode(mb_trim($value));
                } elseif (isset($settings[$key . '_field_is_amount'])) {
                    // Format amount inputs
                    $batch_settings[$key] = standardize_amount($value);
                } else {
                    // Security: Validate logo filename settings to prevent pa
...[truncated]...

### application/modules/clients/models/Mdl_client_notes.php
<?php

if ( ! defined('BASEPATH')) {
    exit('No direct script access allowed');
}

/*
 * InvoicePlane
 *
 * @author		InvoicePlane Developers & Contributors
 * @copyright	Copyright (c) 2012 - 2018 InvoicePlane.com
 * @license		https://invoiceplane.com/license.txt
 * @link		https://invoiceplane.com
 */

#[AllowDynamicProperties]
class Mdl_Client_Notes extends Response_Model
{
    public $table = 'ip_client_notes';

    public $primary_key = 'ip_client_notes.client_note_id';

    public function default_order_by()
    {
        $this->db->order_by('ip_client_notes.client_note_date DESC');
    }

    public function validation_rules()
    {
        return [
            'client_id' => [
                'field' => 'client_id',
                'label' => trans('client'),
                'rules' => 'required',
            ],
            'client_note' => [
                'field' => 'client_note',
                'label' => trans('note'),
                'rules' => 'required',
            ],
        ];
    }

    public function db_array()
    {
        $db_array = parent::db_array();

        $db_array['client_note_date'] = date('Y-m-d');

        return $db_array;
    }

    /**
     * @param int $id
     */
    public function delete($id): bool
    {
        parent::delete($id);

        // For Ajax Check if deletion was successful
        return true;
    }
}

### application/modules/quotes/views/partial_quote_table.php
<div class="table-responsive">
    <table class="table table-hover table-striped">

        <thead>
        <tr>
            <th><?php _trans('status'); ?></th>
            <th><?php _trans('quote'); ?></th>
            <th><?php _trans('created'); ?></th>
            <th><?php _trans('due_date'); ?></th>
            <th><?php _trans('client_name'); ?></th>
            <th class="amount last"><?php _trans('amount'); ?></th>
            <th><?php _trans('options'); ?></th>
        </tr>
        </thead>

        <tbody>
<?php
$quote_idx                    = 1;
            $quote_count      = count($quotes);
            $quote_list_split = $quote_count > 3 ? $quote_count / 2 : 9999;

            foreach ($quotes as $quote) {
                // Convert the dropdown menu to a dropup if quote is after the invoice split
                $dropup = $quote_idx > $quote_list_split;
                ?>
            <tr>
                <td>
                    <span class="label <?php echo $quote_statuses[$quote->quote_status_id]['class']; ?>">
                        <?php echo $quote_statuses[$quote->quote_status_id]['label']; ?>
                    </span>
                </td>
                <td>
                    <a href="<?php echo site_url('quotes/view/' . $quote->quote_id); ?>"
                       title="<?php _trans('edit'); ?>">
                        <?php echo $quote->quote_number ? htmlsc($quote->quote_number) : $quote->quote_id; ?>
                    </a>
                </td>
                <td>
                    <?php echo date_from_mysql($quote->quote_date_created); ?>
                </td>
                <td>
                    <?php echo date_from_mysql($quote->quote_date_expires); ?>
                </td>
                <td>
                    <a href="<?php echo site_url('clients/view/' . $quote->client_id); ?>"
                       title="<?php _trans('view_client'); ?>">
                        <?php _htmlsc(format_client($quote)); ?>
                    </a>
                </td>
                <td class="amount last">
                    <?php echo format_currency($quote->quote_total); ?>
                </td>
                <td>
                    <div class="options btn-group<?php echo $dropup ? ' dropup' : ''; ?>">
                        <a class="btn btn-sm btn-default dropdown-toggle" data-toggle="dropdown"
                           href="#">
                            <i class="fa fa-cog"></i> <?php _trans('options'); ?>
                        </a>
                        <ul class="dropdown-menu">
               
...[truncated]...

### application/modules/import/models/Mdl_import.php
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
class Mdl_Import extends Response_Model
{
    public $table = 'ip_imports';

    public $primary_key = 'ip_imports.import_id';

    public $expected_headers = [
        'clients.csv' => [
            'client_name',
            'client_address_1',
            'client_address_2',
            'client_city',
            'client_state',
            'client_zip',
            'client_country',
            'client_phone',
            'client_fax',
            'client_mobile',
            'client_email',
            'client_web',
            'client_vat_id',
            'client_tax_code',
            'client_active',
        ],
        'invoices.csv' => [
            'user_email',
            'client_name',
            'invoice_date_created',
            'invoice_date_due',
            'invoice_number',
            'invoice_terms',
        ],
        'invoice_items.csv' => [
            'invoice_number',
            'item_tax_rate',
            'item_date_added',
            'item_name',
            'item_description',
            'item_quantity',
            'item_price',
        ],
        'payments.csv' => [
            'invoice_number',
            'payment_method',
            'payment_date',
            'payment_amount',
            'payment_note',
        ],
    ];

    public $primary_keys = [
        'ip_clients'       => 'client_id',
        'ip_invoices'      => 'invoice_id',
        'ip_invoice_items' => 'item_id',
        'ip_payments'      => 'payment_id',
    ];

    /**
     * Mdl_Import constructor.
     */
    public function __construct() {}

    public function default_select()
    {
        $this->db->select("SQL_CALC_FOUND_ROWS ip_imports.*,
            (SELECT COUNT(*) FROM ip_import_details WHERE import_table_name = 'ip_clients' AND ip_import_details.import_id = ip_imports.import_id) AS num_clients,
            (SELECT COUNT(*) FROM ip_import_details WHERE import_table_name = 'ip_invoices' AND ip_import_details.import_id = ip_imports.import_id) AS num_invoices,
            (SELECT COUNT(*) FROM ip_import_details WHERE import_table_name = 'ip_invoice_items' AND ip_import_details.import_id = ip_imports.import_id) AS num_invoice_items,
            (SELECT COUNT(*) FROM ip_import_details WHERE import_tab
...[truncated]...

### application/views/errors/cli/error_general.php
<?php

defined('BASEPATH') || exit('No direct script access allowed');

echo "\nERROR: ",
$heading,
"\n\n",
$message,
"\n\n";

### application/helpers/redirect_helper.php
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

/**
 * Redirect the user to a given URL.
 *
 * @param string $fallback_url_string
 * @param bool   $redirect
 *
 * @return mixed
 */
function redirect_to($fallback_url_string, $redirect = true)
{
    $CI = & get_instance();

    $redirect_url = ($CI->session->userdata('redirect_to')) ? $CI->session->userdata('redirect_to') : $fallback_url_string;

    $CI->session->unset_userdata('redirect_to');

    if ($redirect) {
        redirect($redirect_url);
    }

    return $redirect_url;
}

/**
 * Sets the current URL in the session.
 */
function redirect_to_set(): void
{
    $CI = & get_instance();
    $CI->session->set_userdata('redirect_to', $CI->uri->uri_string());
}

### application/modules/projects/controllers/Projects.php
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
class Projects extends Admin_Controller
{
    /**
     * Projects constructor.
     */
    public function __construct()
    {
        parent::__construct();

        $this->load->model('mdl_projects');
    }

    /**
     * @param int $page
     */
    public function index($page = 0)
    {
        $this->mdl_projects->paginate(site_url('projects/index'), $page);
        $projects = $this->mdl_projects->result();

        $this->layout->set(
            [
                'filter_display'     => true,
                'filter_placeholder' => trans('filter_projects'),
                'filter_method'      => 'filter_projects',
                'projects'           => $projects,
            ]
        );
        $this->layout->buffer('content', 'projects/index');
        $this->layout->render();
    }

    public function form($id = null)
    {
        if ($this->input->post('btn_cancel')) {
            redirect('projects');
        }

        if ($this->mdl_projects->run_validation()) {
            $this->mdl_projects->save($id);
            redirect('projects');
        }

        if ($id && ! $this->input->post('btn_submit') && ! $this->mdl_projects->prep_form($id)) {
            show_404();
        }

        $this->load->model('clients/mdl_clients');

        $this->layout->set(
            [
                'project' => $this->mdl_projects->get_by_id($id),
                'clients' => $this->mdl_clients->where('client_active', 1)->get()->result(),
            ]
        );

        $this->layout->buffer('content', 'projects/form');
        $this->layout->render();
    }

    public function view($project_id)
    {
        if ($this->input->post('btn_cancel')) {
            redirect('projects');
        }

        $this->load->model('projects/mdl_projects');
        $project = $this->mdl_projects->get_by_id($project_id);

        if ( ! $project) {
            show_404();
        }

        $this->load->model('tasks/mdl_tasks');

        $this->layout->set([
            'project'       => $project,
            'tasks'         => $this->mdl_projects->get_tasks($project->project_id),
            'task_statuses' => $this->mdl_tasks->statuses(),
        ]);
        $this->layout->buffer('content', 'projects/view');
     
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

### application/modules/products/views/partial_product_table_modal.php
<div class="table-responsive">
    <table id="products_table" class="table table-hover table-bordered table-striped">
        <tr>
            <th>&nbsp;</th>
            <th><?php _trans('product_sku'); ?></th>
            <th><?php _trans('family_name'); ?></th>
            <th><?php _trans('product_name'); ?></th>
            <th><?php _trans('product_description'); ?></th>
            <th class="amount"><?php _trans('product_price'); ?></th>
        </tr>
        <?php foreach ($products as $product) { ?>
            <tr class="product">
                <td class="text-left">
                    <input type="checkbox" name="product_ids[]"
                           value="<?php echo $product->product_id; ?>">
                </td>
                <td nowrap class="text-left">
                    <b><?php _htmlsc($product->product_sku); ?></b>
                </td>
                <td>
                    <b><?php _htmlsc($product->family_name); ?></b>
                </td>
                <td>
                    <b><?php _htmlsc($product->product_name); ?></b>
                </td>
                <td>
                    <?php echo nl2br(htmlsc($product->product_description)); ?>
                </td>
                <td class="amount">
                    <?php echo format_currency($product->product_price); ?>
                </td>
            </tr>
        <?php } ?>

    </table>
</div>

### application/modules/guest/views/quotes_view.php
<?php
$global_discount = $quote->quote_discount_percent > 0 ? format_amount($quote->quote_discount_percent) . '%' : format_currency($quote->quote_discount_amount);
if ($quote_tax_rates) {
    $global_taxes = [];
    foreach ($quote_tax_rates as $quote_tax_rate) {
        $global_taxes[] = $quote_tax_rate->quote_tax_rate_name . ' (' . format_amount($quote_tax_rate->quote_tax_rate_per
...[truncated]...