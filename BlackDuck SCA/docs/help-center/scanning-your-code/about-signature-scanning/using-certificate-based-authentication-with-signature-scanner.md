---
title: "Using certificate-based authentication with Signature Scanner"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-certificate-based-authentication-with-signature-scanner.html"
content_id: "DgDEJK9JGVORS1j6K219sQ"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:10.852388+00:00"
content_hash: "93ccec5b5ac4dbb7d877338994d55f4ced9ae3a325dd2f66a7db8b8d05239b88"
---

# Using certificate-based authentication with Signature Scanner

HUB-6464,6463, 6465You can use a client certificate, also known as a signed key pair, to authenticate to a TLS-enabled server.

From the command line, enter the **--tlscert** <*certFile*> and optionally the **--tlskey** <*keyFile*> parameters. These two parameters represent both the signed public key and the private key, respectively, used to authenticate to the TLS-enabled server.

Optionally you can specify the **--tlscertpass** parameter to force a password prompt for the client certificate or use the BD_HUB_CLIENTCERT_PASS environment variable to specify the password for the private key. Click here for more information.

## Examples

The following are examples of using certificate-based authentication with a certificate that does and does not include a separate private key file.

Note that:

- The examples show only required parameters.
- The key is encrypted and the BD_HUB_CLIENTCERT_PASS environment variable has been set. Therefore, the **--tlscertpass** parameter is not included.

To use a certificate that does not includes the private key (that is, a key store):

1. Open a command prompt.
2. Go to the directory where Signature Scanner is installed.

   **Linux/MAC OS X**:

   `/opt/blackduck/hub/scan.cli-2026.7.1``/scan.cli-2026.7.1``/bin`

   **Windows**:

   `C:\scan.cli-2026.7.1``\scan.cli-2026.7.1``\bin`
3. Run the following command to configure and initiate the scan.

   **Linux/Mac OS X**:

   ```
   ./scan.cli.sh --host <host> --port <port> --tlskey <keyFile> --tlscert <certFile> <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat --host <host> --port <port> --tlskey <keyFile> --tlscert <certFile> <scan_path>
   ```

To use a certificate that includes the private key (that is, a key store):

1. Open a command prompt.
2. Go to the directory where Signature Scanner is installed.

   **Linux/MAC OS X**:

   `/opt/blackduck/hub/scan.cli-2026.7.1``/scan.cli-2026.7.1``/bin`

   **Windows**:

   `C:\scan.cli-2026.7.1``\scan.cli-2026.7.1``\bin`
3. Run the following command to configure and initiate the scan.

   **Linux/Mac OS X**:

   ```
   ./scan.cli.sh --host <host> --port <port> --tlscert <certFile> <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat --host <host> --port <port> --tlscert <certFile> <scan_path>
   ```

Signature Scanner sends the scan data to the Black Duck server. Log in to Black Duck to map the component scan to a project, which adds the identified components to the project BOM.
