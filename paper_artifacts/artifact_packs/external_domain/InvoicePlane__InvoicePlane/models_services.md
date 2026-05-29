# Models/services
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