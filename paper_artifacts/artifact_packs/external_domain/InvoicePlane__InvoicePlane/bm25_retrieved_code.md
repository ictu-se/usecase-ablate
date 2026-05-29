# README-derived retrieval query
InvoicePlane InvoicePlane ## README.md
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

For a **detailed installation guide**, including prerequisites and trouble
...[truncated]...

# BM25 selected code snippets
### README.md
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
- #1381 - E-invoicing field migration and
...[truncated]...

### INSTALLATION.md
# Installation Guide

Follow the instructions below to install InvoicePlane on your preferred platform.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
   - [Using the .zip File (Production)](#1-using-the-zip-file-production)
   - [Cloning the Repository (Development)](#2-cloning-the-repository-development)
3. [Development Workflow](#development-workflow)
   - [Prepare: Initial Setup](#prepare-initial-setup)
   - [StartMeUp: Start Development Environment](#startmeup-start-development-environment)
   - [Workflow: Daily Development](#workflow-daily-development)
4. [Platform-Specific Instructions](#platform-specific-instructions)
   - [Windows](#windows)
   - [macOS](#macos)
   - [Linux](#linux)
5. [Docker Installation](#docker-installation)
6. [Post-Installation](#post-installation)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- **Web Server:** Apache or Nginx
- **PHP:** Version **8.2 or higher** (PHP 8.3 and 8.4 supported)
- **Database:** MariaDB
- **For Development:** Docker (recommended), Composer, Yarn/npm

---

## Installation Methods

### 1. Using the .zip File (Production)

This method is recommended for production deployments:

1. **Download:**
   - Get the latest version from the [InvoicePlane website](https://www.invoiceplane.com/).

2. **Extract:**
   - Unzip the package and upload the contents to your web server.

3. **Configuration:**
   - Rename `ipconfig.php.example` to `ipconfig.php`.
   - Edit `ipconfig.php` and set your base URL and database credentials.

4. **Setup:**
   - Navigate to `http://your-domain.com/index.php/setup` in your browser and follow the on-screen instructions.

---

### 2. Cloning the Repository (Development)

This method is recommended for development and contributing to InvoicePlane:

See [Development Workflow](#development-workflow) section below for detailed steps.

---

## Development Workflow

This section outlines the three-phase workflow for developing InvoicePlane:

### Prepare: Initial Setup

The **Prepare** phase sets up your development environment for the first time.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/InvoicePlane/InvoicePlane.git
   cd InvoicePlane
   ```

2. **Install PHP Dependencies:**
   ```bash
   composer install
   ```
   This installs all PHP packages defined in `composer.json`.

3. **Install JavaScript Dependencies:**
   ```bash
   yarn install
   ```
   This installs all frontend dependencies (Bootstrap, jQuery, etc.).

4. **Build Frontend Assets:**
   ```bash
   yarn build
   ```
 
...[truncated]...

### AGENTS.md
# AGENTS.md — Instructions for AI Coding Agents

This file provides context and instructions for AI coding agents (GitHub Copilot, Claude, etc.) working on the InvoicePlane codebase.

## Project overview

InvoicePlane is a **self-hosted, open-source invoicing application** built with **PHP and CodeIgniter 3**. It is not a Laravel application. There is no Artisan CLI, no Eloquent ORM, and no `artisan migrate`.

- **Framework:** CodeIgniter 3
- **PHP:** 8.2+
- **Database:** MySQL / MariaDB
- **Build tools:** Yarn (frontend), Composer (backend)
- **PDF generation:** mPDF
- **Email:** PHPMailer

## Repository layout

```
application/
  config/           CI3 configuration files
  helpers/          Global helper functions
  language/         i18n strings
  libraries/        Custom CI3 libraries (Cryptor, etc.)
  modules/          Feature modules (CodeIgniter HMVC)
    clients/
    invoices/       Invoice management
    guest/          Public-facing invoice and quote views
    mailer/         Email sending (PHPMailer wrapper)
    settings/
    setup/          Database migration wizard
    ...
  views/            Shared views and PDF/public templates
assets/
  core/js/scripts.js
  core/css/
.github/
  workflows/        GitHub Actions (see table below)
  scripts/          Helper scripts for CI (phpstan parser)
  actions/          Composite actions (setup-php-composer)
pint.json           Code style configuration (Pint / PHP CS Fixer)
phpstan.neon        Static analysis configuration
ipconfig.php.example  Application configuration template
CHANGELOG.md
UPGRADE.md
AGENTS.md           (this file)
.junie/guidelines.md  Extended development guidelines
```

## Framework conventions

| Concept | CodeIgniter 3 Pattern |
|---------|----------------------|
| Controller base | `Admin_Controller`, `Guest_Controller` |
| Model | Extends `CI_Model`; use `$this->db->*()` |
| View | Plain PHP template files with `html_escape()` for output |
| Helper loading | `$this->load->helper('helper_name')` |
| Input | `$this->input->post()`, `$this->input->get()` — never `$_POST` directly |
| Configuration | Constants defined in `ipconfig.php` (not `.env`) |
| URL routing | `application/config/routes.php` |
| Database | Active Record / Query Builder — no raw SQL string concatenation |

## Security rules

These rules must not be broken.

1. **No filesystem scanning for template whitelists.** Template names are defined in hardcoded constants in `Mdl_Templates`. Scanning the filesystem (e.g. with `directory_map()`) to build an allowed list creates an RCE vulnerability.

2. **No unvalidated re
...[truncated]...

### CHANGELOG.md
# Changelog

All notable changes to InvoicePlane will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.7.2] - 2026-04-06

### Security

**CRITICAL: Fixed Broken Authentication - Password reset tokens now expire (#TBD)**
- Password reset tokens now expire after a configurable time (default: 15 minutes)
- Added `user_passwordreset_token_expiry` database column to track token creation time
- Tokens are automatically invalidated after expiration
- Prevents indefinite token validity that could lead to account takeover
- Expired tokens are automatically cleared from the database
- Configuration option `PASSWORD_RESET_TOKEN_EXPIRY_MINUTES` added to ipconfig.php.example

---

**HIGH: Fixed Arbitrary File Deletion via Path Traversal - CVSSv3 7.1 (CVE Pending)**

Authenticated administrators could delete arbitrary files on the server through path traversal sequences in logo filename settings. An attacker could set a malicious logo filename (e.g., `../../config/database.php`) via the settings page, then trigger deletion through the remove_logo endpoint.

**Vulnerability Details:**
- **CWE-22:** Improper Limitation of a Pathname to a Restricted Directory
- **Attack Vector:** Authenticated administrator could exploit path traversal
- **Impact:** Application failure, data loss, denial of service through file deletion

**Root Cause:**
1. Settings save functionality accepted arbitrary logo filenames without validation
2. The `remove_logo()` function used database values directly for file deletion
3. No path traversal detection or directory confinement checks

**Fix Implementation:**
- **Added input validation on settings save** (lines 78-87 in Settings.php)
  - Logo filenames validated using `validate_safe_filename()` before saving to database
  - Path traversal sequences rejected with error logging
  - Invalid filenames blocked with user-friendly error message
  
- **Added type parameter validation** (lines 272-282 in Settings.php)
  - Logo type restricted to allow-list: `['invoice', 'login']`
  - Invalid types logged and rejected
  - Prevents arbitrary type parameter injection
  
- **Added comprehensive file access validation** (lines 293-323 in Settings.php)
  - Multi-layer validation using `validate_file_access()` helper
  - Files must be within `./uploads/` directory (directory confinement)
  - Path traversal sequences detected and blocked
  - Null byte injection prevented
  - Absolute path attempts rejected
  -
...[truncated]...

### UPGRADE.md
# Upgrade Guide

This guide provides instructions for upgrading InvoicePlane to newer versions.

## Table of Contents

- [Instructions to upgrade to 1.7.2 from 1.7.0 / 1.7.1](#instructions-to-upgrade-to-172-from-170--171)
- [Instructions to upgrade to 1.6.3 from 1.6.2](#instructions-to-upgrade-to-163-from-162)
- [Instructions to upgrade to 1.6.0 from 1.5.11](#instructions-to-upgrade-to-160-from-1511)

---

## Instructions to upgrade to 1.7.2 from 1.7.0 / 1.7.1

> **This is a critical security release.** v1.7.0 and v1.7.1 contain a Remote Code
> Execution vulnerability (CVSSv3 9.9). Upgrade immediately. Consult
> [MIGRATION_GUIDE_v1.7.2.md](MIGRATION_GUIDE_v1.7.2.md) for a full pre-upgrade security
> audit checklist.

### Security fixes in this release

| Severity | Vulnerability | Details |
|----------|--------------|---------|
| **Critical** | Remote Code Execution via dynamic template whitelist (bypass of v1.7.1 LFI fix) | [SECURITY_ADVISORY_RCE_FIX.md](SECURITY_ADVISORY_RCE_FIX.md) |
| **Critical** | Broken authentication – password reset tokens never expired | CHANGELOG.md |
| **High** | Open redirect via unvalidated `HTTP_REFERER` | [ADDITIONAL_SECURITY_FIXES_v1.7.2.md](ADDITIONAL_SECURITY_FIXES_v1.7.2.md) |
| **Medium** | SQL query hardened in guest payments | ADDITIONAL_SECURITY_FIXES_v1.7.2.md |
| **Medium** | `HTTP_REFERER` injection in AJAX filter controllers | ADDITIONAL_SECURITY_FIXES_v1.7.2.md |
| **Medium** | PHPMailer SMTP debug output logged unsanitized (log injection) | CHANGELOG.md |
| **Medium** | `phpmail_send()` masked send failures by always returning `true` | CHANGELOG.md |
| **Low** | Binary data corruption in `Cryptor::decryptString()` (`mb_strlen`/`mb_substr`) | CHANGELOG.md |
| **Low** | GitHub Actions `GITHUB_TOKEN` over-broad permissions | CHANGELOG.md |

### Behavioral changes that may require action

The following changes alter observable behavior or API contracts. Review each one before
upgrading.

#### 1. `phpmail_send()` now returns `false` on delivery failure

**Who is affected:** Installations with custom code that calls `phpmail_send()` directly and
relies on its return value.

**Before (v1.7.0–1.7.1):** `phpmail_send()` always returned `true`, even when the underlying
SMTP/sendmail call failed. Delivery failures were silently dropped.

**After (v1.7.2):** `phpmail_send()` returns the actual boolean result — `true` on success,
`false` on failure. Failed sends now set a flash error message for the user.

**Action required:** If your custom code calls `phpmail_send()`, update it to check the return
value:

```php
// Bef
...[truncated]...

### RELEASE_NOTES_v1.7.2_PR_TABLE.md
# InvoicePlane v1.7.2 — Pull Request & Release Summary

This document lists all pull requests resolved in the **v1.7.2** release cycle, together with
any linked GitHub issues and associated security advisories. It is intended as the source of
truth for the README / CHANGELOG entry once v1.7.2 goes final.

> **Note:** Security advisories will be formally published after the final v1.7.2 release.
> CVE identifiers marked *Pending* will be updated once assigned.

> **Sort order:** All sections are ordered by PR number (ascending). The Security Fixes section
> is ordered by severity (most critical first), then CVSS score (descending), then PR number
> (ascending) within each tier. The Security Advisories Reference table follows the same rule.

---

## Table of Contents

1. [Security Fixes](#security-fixes)
2. [Bug Fixes](#bug-fixes)
3. [Features & Improvements](#features--improvements)
4. [Performance & Code Quality](#performance--code-quality)
5. [Infrastructure & CI](#infrastructure--ci)
6. [Security Advisories Reference](#security-advisories-reference)

---

## Security Fixes

> Sorted by: Severity DESC → CVSS DESC → PR ID ASC within each tier.

| PR | Title | Linked Issue | Security Advisory / CVE | CVSS | Severity |
|----|-------|-------------|--------------------------|------|----------|
| [#1505](https://github.com/InvoicePlane/InvoicePlane/pull/1505) | Fix RCE vulnerability in template system — replace `directory_map()` whitelist with static constants; fix 5 open-redirect instances; add `security_helper.php` | — | [SECURITY_ADVISORY_RCE_FIX.md](SECURITY_ADVISORY_RCE_FIX.md) — CVE Pending | 9.9 | 🔴 CRITICAL |
| [#1506](https://github.com/InvoicePlane/InvoicePlane/pull/1506) | CodeRabbit auto-fixes for #1505: correct `security_helper.php` (stacked follow-up) | — | See #1505 | — | 🔴 CRITICAL (follow-up) |
| [#1516](https://github.com/InvoicePlane/InvoicePlane/pull/1516) | Comprehensive XSS fixes across InvoicePlane — 32 vulnerabilities across 17 view files in 4 modules | — | — CVE Pending | 8.0 | 🔴 HIGH |
| [#1482](https://github.com/InvoicePlane/InvoicePlane/pull/1482) | Fix IDOR, CSRF, and SQL injection vulnerabilities in guest controllers | — | — CVE Pending | 7.5 | 🔴 HIGH |
| [#1494](https://github.com/InvoicePlane/InvoicePlane/pull/1494) | Replace weak PRNG in password reset tokens with `random_bytes(32)` (256-bit entropy) | — | Related to [CVE-2021-29023](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29023) | 7.5 | 🔴 HIGH |
| [#1481](https://github.com/InvoicePlane/InvoicePlane/pull/1481) | Fix SQL injection in tax rate decimal places se
...[truncated]...

### MIGRATION_GUIDE_v1.7.2.md
# Migration Guide: Upgrading to v1.7.2 (RCE Fix)

This guide helps administrators safely upgrade from vulnerable versions (v1.7.0, v1.7.1) to v1.7.2 which fixes a critical Remote Code Execution vulnerability.

## Pre-Upgrade Security Audit

**IMPORTANT:** Before upgrading, check if your installation has already been compromised.

### 1. Check for Malicious Template Files

List all files in template directories:

```bash
cd /path/to/invoiceplane

# List invoice templates (public)
ls -la application/views/invoice_templates/public/

# List invoice templates (PDF)
ls -la application/views/invoice_templates/pdf/

# List quote templates (public)
ls -la application/views/quote_templates/public/

# List quote templates (PDF)
ls -la application/views/quote_templates/pdf/
```

**Expected Files Only:**

Invoice Templates (Public):
- `InvoicePlane_Web.php`
- `.gitignore`

Invoice Templates (PDF):
- `InvoicePlane.php`
- `InvoicePlane - paid.php`
- `InvoicePlane - overdue.php`
- `.gitignore`

Quote Templates (Public):
- `InvoicePlane_Web.php`
- `.gitignore`

Quote Templates (PDF):
- `InvoicePlane.php`
- `.gitignore`

**WARNING: If you find ANY other PHP files, they are potentially malicious and should be investigated immediately.**

### 2. Check Database for Suspicious Template Settings

```sql
-- Connect to your InvoicePlane database
mysql -u your_username -p your_database_name

-- Check all template settings
SELECT setting_key, setting_value 
FROM ip_settings 
WHERE setting_key LIKE '%template%';
```

**Expected Values:**
- `public_invoice_template`: `InvoicePlane_Web`
- `public_quote_template`: `InvoicePlane_Web`
- `pdf_invoice_template`: `InvoicePlane`
- `pdf_invoice_template_paid`: `InvoicePlane - paid`
- `pdf_invoice_template_overdue`: `InvoicePlane - overdue`
- `pdf_quote_template`: `InvoicePlane`
- `email_invoice_template`: (various, should be from email templates)
- `email_quote_template`: (various, should be from email templates)

**WARNING: If any PDF or public template setting contains an unexpected value, investigate immediately.**

### 3. Review Web Server Logs

Check for suspicious access patterns:

```bash
# Check Apache access logs
grep -i "evil\|shell\|cmd\|exec\|system" /var/log/apache2/access.log | tail -50

# Check for unusual query parameters
grep "guest/view/invoice" /var/log/apache2/access.log | grep -i "[\?&][a-z0-9]=.*[;&|<>]" | tail -20

# Check error logs for template-related errors
grep "template" /var/log/apache2/error.log | tail -20
```

### 4. Check Recent File Modifications

Find recently modified PHP files:

```bash
cd /path/to/invoic
...[truncated]...

### CONTRIBUTING.md
# Contributing to InvoicePlane

Thank you for considering contributing to InvoicePlane! Your support is invaluable in improving and maintaining this project. Whether you're reporting bugs, suggesting features, writing code, or helping others, your contributions are welcome.

## Table of Contents

1. [How Can I Contribute?](#how-can-i-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Features](#suggesting-features)
   - [Code Contributions](#code-contributions)
   - [Documentation](#documentation)
   - [Translations](#translations)
   - [Community Support](#community-support)
2. [Development Guidelines](#development-guidelines)
   - [Coding Standards](#coding-standards)
   - [Commit Messages](#commit-messages)
3. [Getting Started with Development](#getting-started-with-development)
4. [Community and Support](#community-and-support)
5. [Code of Conduct](#code-of-conduct)

---

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug, please report it by [opening an issue](https://github.com/InvoicePlane/InvoicePlane/issues) and include:

- **Description:** A clear and concise description of the bug.
- **Steps to Reproduce:** Detailed steps to reproduce the issue.
- **Expected Behavior:** What you expected to happen.
- **Actual Behavior:** What actually happened.
- **Screenshots:** If applicable, add screenshots to help explain the problem.
- **Environment:** Information about your environment (e.g., operating system, browser, InvoicePlane version).

---

### Suggesting Features

To suggest a new feature, please [open an issue](https://github.com/InvoicePlane/InvoicePlane/issues) and include:

- **Feature Description:** A clear and concise description of the feature.
- **Use Case:** Explain why this feature would be useful.
- **Additional Context:** Any other context or screenshots that might help.

---

### Code Contributions

If you'd like to contribute code:

1. **Fork the Repository:** Click the "Fork" button at the top right of the [repository page](https://github.com/InvoicePlane/InvoicePlane).
2. **Clone Your Fork:**
   ```sh
   git clone https://github.com/your-username/InvoicePlane.git
   ```
3. **Create a Branch:**
   ```sh
   git checkout -b feature/your-feature-name
   ```
4. **Make Your Changes:** Implement your feature or fix.
5. **Commit Your Changes:**
   ```sh
   git commit -m "Brief description of your changes"
   ```
6. **Push to Your Fork:**
   ```sh
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request:** Go to the original repository and [open a pull request](https://github.com/Invoi
...[truncated]...

### index.php
<?php

/**
 * DO NOT EDIT THIS FILE!
 * Make a copy of the ipconfig.php.example file, rename the copy to 'ipconfig.php' and set your settings in this file.
 */

/*
 *---------------------------------------------------------------
 * LOAD DOTENV
 *---------------------------------------------------------------
 */

if ( ! file_exists('ipconfig.php')) {
    exit('The <b>ipconfig.php</b> file is missing! Please make a copy of the <b>ipconfig.php.example</b> file and rename it to <b>ipconfig.php</b>');
}

require __DIR__ . '/vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__, 'ipconfig.php');
$dotenv->load();

/**
 * Small helper function to allow defaults for the getenv function.
 *
 * @param string $env_key
 * @param mixed  $default
 *
 * @return mixed
 */
function env($env_key, $default = null)
{
    if (isset($_ENV[$env_key])) {
        return $_ENV[$env_key];
    }

    return $default;
}

/**
 * Small helper function to get bool values for the env setting.
 *
 * @param string $env_key
 * @param string $default
 */
function env_bool($env_key, $default = 'false'): bool
{
    return env($env_key, $default) === 'true';
}

// Enable debug mode if set
define('IP_DEBUG', env_bool('ENABLE_DEBUG'));
// Settings Invoices Sumex panel - Since v1.6.3
define('SUMEX_SETTINGS', env_bool('SUMEX_SETTINGS'));
// Where post sumex xml to get pdf - Since v1.5.0 - See https://github.com/InvoicePlane/InvoicePlane/pull/453
define('SUMEX_URL', env('SUMEX_URL'));

/*
 *---------------------------------------------------------------
 * APPLICATION ENVIRONMENT
 *---------------------------------------------------------------
 *
 * You can load different configurations depending on your
 * current environment. Setting the environment also influences
 * things like logging and error reporting.
 *
 * This can be set to anything, but default usage is:
 *
 *     development
 *     testing
 *     production
 *
 * NOTE: If you change these, also change the error_reporting() code below
 */
define('ENVIRONMENT', $_SERVER['CI_ENV'] ?? 'development');

/*
 *---------------------------------------------------------------
 * ERROR REPORTING
 *---------------------------------------------------------------
 *
 * Different environments will require different levels of error reporting.
 * By default development will show errors but testing and live will hide them.
 */
switch (ENVIRONMENT) {
    case 'development':
        error_reporting(-1);
        ini_set('display_errors', 1);
        break;

    case 'testing':
    case 'production':
        ini_set('display_errors', 0);
 
...[truncated]...

### application/helpers/XMLconfigs/README.md
## How to: Add e-Invoice configuration and template generator

> You can find and download more e-invoice examples in [InvoicePlane-e-invoices repository](https://github.com/InvoicePlane/InvoicePlane-e-invoices).

---

<details>

<summary>

#### File name rules

</summary>

_To implement a new e-invoicing xml system, there are 2 files that need to be placed in their respective folder._

> Add the configuration file (`Shortidv10.php`) in `helpers/XMLconfigs/` folder (here)

> and the generator file (`Shortidv10Xml.php`) in the [`libraries/XMLtemplates/`](../../libraries/XMLtemplates/) folder.

**Configuration filename (XML helper)**

```
Filename: 'Shortidv10.php'  -> "Shortid" + "version" + ".php" : max 25 characters (without ".php")
                            (preferably without spaces " ", dots ".", hyphen "-", underscore "_" or special characters)
```

**Generator filename (XML template)**

```
Filename: 'Shortidv10Xml.php'  -> Same name of configurator file with "Xml"
                               -> Don't respect this rule if the "generator" option is set. (Use an other template to make XML).
```

_It is important to make the file names as short as possible and preferably use only numbers and letters._

_Each **country** has its format **specifications** and version on which it is best to base the shortened name._

---

</details>

<details>

<summary>

#### Configuration rules

</summary>

_**Required**_

> The Variable `$xml_setting` name is mandatory and it's an array and contain at minima this 4 keys

```
'full-name'   => 'E-Invoice v1.0', // String : CII / UBL version name. Visible in the client edit form (drop-down selector in e-invoice panel)
'countrycode' => 'EX',             // String : Associated countrycode (if available in your native language country list)
'embedXML'    => false,            // Bool   : To embed the Xml file in Pdf set to true (for 'ZUGFeRD' and similar)
'XMLname'     => '',               // String : Name of the embedded in a CII Pdf Xml file (if not, leave empty)
```

_Optional_

```
'generator'   => 'Einvoicev10',       // String : Name of the Xml file generator without 'Xml' and '.php' extension (optional)
'options'     => ['Opt1' => 'param'], // Mixed (String|Array|Object) : If you need variables or specific codes transmit to generator (Optional)
```

_Special_

```
'legacy_calculation' => true, // Bool   : Only if you need the Legacy Calculation (Optional)
                              // Notes  : Need to Override the default lively set to false "when the client use eInvoice" (Scope: Invoice/Quote view & pdf gener
...[truncated]...

### .junie/PR-1441-security-dry-analysis.md
# Security and DRY Analysis for PR #1441

## Overview

This document provides a comprehensive analysis of the security vulnerabilities addressed and DRY (Don't Repeat Yourself) principles applied in Pull Request #1441.

**PR Title:** Refactor input sanitization to follow DRY principles and fix log injection vulnerabilities  
**Related Issue:** Feedback on PR #1439  
**Files Modified:** 5 files, +72 insertions, -23 deletions

---

## Security Vulnerabilities Addressed

### 1. Log Injection Vulnerabilities

**Severity:** Medium  
**Impact:** Attackers could inject fake log entries by including newline characters in user input

#### Affected Files

1. `application/modules/settings/controllers/Settings.php` (2 instances)
2. `application/helpers/pdf_helper.php` (2 instances)

#### Vulnerability Details

**Before:** User-controlled filenames and template names were logged directly without sanitization:

```php
// Settings.php - Line 120 (vulnerable)
log_message('warning', 'SVG upload attempt blocked for invoice_logo by user ' . 
    $this->session->userdata('user_id') . ': ' . $_FILES['invoice_logo']['name']);

// Settings.php - Line 142 (vulnerable)
log_message('warning', 'SVG upload attempt blocked for login_logo by user ' . 
    $this->session->userdata('user_id') . ': ' . $_FILES['login_logo']['name']);

// pdf_helper.php - Line 89 (vulnerable)
$safe_invoice_template = preg_replace('/[[:^print:]]/', '', (string) $invoice_template);
log_message('error', 'Invalid PDF invoice template parameter: ' . $safe_invoice_template . ', using default');

// pdf_helper.php - Line 313 (inconsistent)
log_message('error', 'Invalid PDF quote template: ' . hash_for_logging($quote_template) . ', using default');
```

**Attack Scenario:**
```php
// Attacker uploads file named: "evil.svg\nSUCCESS: Admin user granted"
// Log would show:
// WARNING: SVG upload attempt blocked for invoice_logo by user 5: evil.svg
// SUCCESS: Admin user granted
```

#### Fix Applied

**After:** All user-controlled data is sanitized before logging using the new `sanitize_for_logging()` helper:

```php
// Settings.php - Fixed
log_message('warning', 'SVG upload attempt blocked for invoice_logo by user ' . 
    $this->session->userdata('user_id') . ': ' . 
    sanitize_for_logging(basename($_FILES['invoice_logo']['name'])));

// pdf_helper.php - Fixed (both instances now consistent)
log_message('error', 'Invalid PDF invoice template parameter: ' . 
    sanitize_for_logging($invoice_template) . ', using default');
```

**Defense:** The `sanitize_for_logging()` function strips carriage return (`\r`) and 
...[truncated]...

### TRANSLATIONS.md
# Translating InvoicePlane

InvoicePlane is a multilingual application, and we rely on community contributions to keep translations up to date. If you want to help translate InvoicePlane into your language, follow this guide.

## 🌍 Where Are Translations Managed?

All translations for InvoicePlane are hosted on **[Crowdin](https://crowdin.com/)** under the project **FusionInvoice**.

## 🔹 How to Contribute

1. **Sign up for a Crowdin account** at [crowdin.com](https://crowdin.com/).
2. **Request access to the FusionInvoice project** by searching for `FusionInvoice`.
3. **Choose a language** from the available options. Languages follow **short codes** (e.g., `en`, `de`, `fr`).
4. **Start translating** missing strings or improving existing ones.
5. **Submit your translations** for review.

## 📜 Translation Guidelines

- Follow existing terminology to ensure consistency.
- Do **not** translate placeholders like `{invoice_number}` or `{client_name}`.
- Keep the formatting intact, especially in Markdown or HTML-based text.
- If unsure, ask in the **InvoicePlane Community Forums** before making significant changes.

## 🛠️ Technical Details

- Translations are stored in `.php` language files inside `application/language/`.
- Directory is long form of the language, **lowercase** ('english', 'german', 'french')
- Each language has its **own folder** (`application/language/english/`, `application/language/german/`, etc.).
- The structure inside each folder should match the default **english (`english`) translation**.

## 💡 Need Help?

If you have any questions, post in the **[InvoicePlane Community Forums](https://community.invoiceplane.com/)** or ask in our translation discussions on Crowdin.

---
*Thank you for helping make InvoicePlane accessible to a global audience!*

### SECURITY_DOCS_README.md
# Security Documentation - Arbitrary File Deletion Vulnerability

This directory contains comprehensive documentation for the arbitrary file deletion vulnerability (CVE pending) discovered and fixed in InvoicePlane v1.7.2.

## Quick Reference

| Document | Purpose | Audience |
|----------|---------|----------|
| **SECURITY_ADVISORY_ARBITRARY_FILE_DELETION.md** | Complete security advisory with technical details | Security researchers, administrators |
| **CVE_REQUEST_SUMMARY.md** | CVE allocation request guide and templates | CVE requesters, security teams |
| **CHANGELOG.md** | Release notes with vulnerability details | All users |
| **verify_file_deletion_fix.php** | Automated test script | System administrators, developers |

## Vulnerability Summary

**Type:** Arbitrary File Deletion via Path Traversal (CWE-22)  
**Severity:** HIGH (CVSS v3.1 Score: 7.1)  
**Status:** Fixed in v1.7.2  
**CVE ID:** Pending allocation  

### Impact

An authenticated administrator could delete arbitrary files on the server by exploiting path traversal sequences in logo filename settings, potentially causing:
- Application failure (deletion of config files)
- Data loss (deletion of application or user files)
- Denial of service

### Quick Fix

**Users:** Upgrade to InvoicePlane v1.7.2 or later immediately.

```bash
cd /path/to/invoiceplane
git fetch origin
git checkout v1.7.2
```

**Verification:** Run the verification script to confirm the fix:

```bash
php verify_file_deletion_fix.php
```

## Documents Overview

### 1. Security Advisory

**File:** `SECURITY_ADVISORY_ARBITRARY_FILE_DELETION.md`

**Contents:**
- Vulnerability description and technical analysis
- Attack scenarios and proof of concept
- Fix implementation details with code examples
- Defense-in-depth layers explained
- Remediation instructions for users and developers
- Verification testing procedures
- Timeline and disclosure information

**Use this document for:**
- Understanding the vulnerability in detail
- Learning about the fix implementation
- Getting remediation instructions
- Security auditing and verification

### 2. CVE Request Summary

**File:** `CVE_REQUEST_SUMMARY.md`

**Contents:**
- CVE request submission guide
- Pre-filled request templates
- CVSS v3.1 scoring breakdown
- Suggested CVE descriptions
- Contact information
- References and links

**Use this document for:**
- Requesting a CVE ID
- Submitting to CNA (CVE Numbering Authority)
- Understanding CVSS scoring
- Getting ready-to-use request templates

### 3. Verification Script

**File:** `verify_file_deletion_fix.php`

**Purpose:**
A
...[truncated]...

### application/core/XSS_Protection_Trait.php
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
 * XSS Protection Trait.
 *
 * Provides XSS filtering methods for controllers to prevent cross-site scripting attacks.
 * Used by Admin_Controller and Guest_Controller to ensure consistent input sanitization.
 */
trait XSS_Protection_Trait
{
    /**
     * Filter and sanitize POST input to prevent XSS attacks.
     *
     * This method processes all POST data and applies appropriate sanitization:
     * - HTML fields (email_template_body, body): Sanitized with HTML Purifier
     * - Bypass fields (passwords): No sanitization to allow special characters
     * - All other fields: XSS cleaned and tags stripped
     *
     * @return void
     */
    protected function filter_input(): void
    {
        // Load file_security helper early so sanitize_for_logging() is always available,
        // even when XSS modification is detected before the logging block is reached.
        $this->load->helper('file_security');

        // Fields that should bypass XSS sanitization
        $bypass_fields = [
            'user_password',      // User password fields need to allow special characters
            'user_passwordv',     // User password verification field
        ];

        // Fields that require special HTML sanitization (not bypass, but custom handling)
        $html_fields = [
            'email_template_body', // Email templates can contain HTML but need HTML Purifier
            'body',                // Email body when sending invoices/quotes
        ];

        $input           = $this->input->post();
        $xss_detected    = false;
        $xss_log_entries = [];

        // Load HTML sanitizer helper once before processing HTML fields
        $html_sanitizer_loaded = false;

        foreach ($input as $key => $value) {
            // Skip bypass fields
            if (in_array($key, $bypass_fields, true)) {
                continue;
            }

            // Handle HTML fields with HTML Purifier
            if (in_array($key, $html_fields, true)) {
                if ( ! $html_sanitizer_loaded) {
                    $this->load->helper('html_sanitizer');
     
...[truncated]...