---
title: "Using certificate-based authentication with Signature Scanner"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-certificate-based-authentication-with-signature-scanner.html"
content_id: "54sScmoQh56p_mhiud_ang"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:41.183056+00:00"
---

# Using certificate-based authentication with Signature Scanner

HUB-6464,6463, 6465You can use a client
certificate, also known as a signed key pair, to authenticate to a TLS-enabled
server.

From the command line, enter the **--tlscert** <*certFile*> and optionally the
**--tlskey** <*keyFile*> parameters. These two parameters represent both
the signed public key and the private key, respectively, used to authenticate to the
TLS-enabled server.

Optionally you can specify the **--tlscertpass** parameter to force a password prompt
for the client certificate or use the BD_HUB_CLIENTCERT_PASS environment variable to
specify the password for the private key. Click here for more information.

## Examples

The following are examples of using certificate-based authentication with a
certificate that does and does not include a separate private key file.

Note that:

- The examples show only required parameters.
- The key is encrypted and the BD_HUB_CLIENTCERT_PASS environment variable has
  been set. Therefore, the **--tlscertpass** parameter is not included.

To use a certificate that does not includes the private key (that is, a key
store):

1. Open a command prompt.
2. Go to the directory where Signature Scanner is installed.

   **Linux/MAC OS X**:

   `/opt/blackduck/hub/scan.cli-2026.7.0``/scan.cli-2026.7.0``/bin`

   **Windows**:

   `C:\scan.cli-2026.7.0``\scan.cli-2026.7.0``\bin`
3. Run the following command to configure and initiate the scan.

   **Linux/Mac OS
   X**:

   ```
   ./scan.cli.sh    --host <host> --port <port>  --tlskey <keyFile> --tlscert <certFile> <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat   --host <host> --port <port>  --tlskey <keyFile> --tlscert <certFile> <scan_path>
   ```

To use a certificate that includes the private key (that is, a key store):

1. Open a command prompt.
2. Go to the directory where Signature Scanner is installed.

   **Linux/MAC OS X**:

   `/opt/blackduck/hub/scan.cli-2026.7.0``/scan.cli-2026.7.0``/bin`

   **Windows**:

   `C:\scan.cli-2026.7.0``\scan.cli-2026.7.0``\bin`
3. Run the following command to configure and initiate the scan.

   **Linux/Mac OS
   X**:

   ```
   ./scan.cli.sh    --host <host> --port <port>   --tlscert <certFile> <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat   --host <host> --port <port>  --tlscert <certFile> <scan_path>
   ```

Signature Scanner sends the scan data to the Black Duck server. Log in to Black Duck to map the component scan to a project,
which adds the identified components to the project BOM.
